import re, logging, hashlib, json, time, os

from langchain_community.document_loaders import PyMuPDFLoader, PyPDFLoader, BSHTMLLoader, CSVLoader
from core.util.config import settings
from core.util.logging import setup_custom_logger
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct, PayloadSchemaType
from collections import Counter


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)
_base = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")   # reads GOOGLE_API_KEY


# Global variables
BATCH, PAUSE = 90, 60   # <=100 requests/min: embed 90 texts, then pause 60s
CACHE_DIR = ".embcache"
PAPER_CHUNKS = 60
CHUNKS = []
# PDF_PAGES = 9   # cap pages of the paper


#####
# To in-memory load the PDF document at a given location
#####
def load_pdf(path):
    try:
        docs = PyMuPDFLoader(path).load()
    except Exception as e:
        log.error(f"PyMuPDFLoader failed on {path}: {e} -> PyPDFLoader fallback")
        docs = PyPDFLoader(path).load()
    return docs


#####
# To join the text and create a single clean string
#####
def clean_ws(text) -> str:
    return re.sub(r"[ \t]+", " ", re.sub(r"\n{3,}", "\n\n", text)).strip()


#####
# To create a consolidated text of list of PDF documents that need to be ingested
#####
def ingest_pdf(path: str, doc_list: list, doc_type: str) -> str:
    full_text = ""
    try:
        for doc in doc_list:
            docs = load_pdf(path+doc)
            full_text += clean_ws(docs)
        log.info(f"Total {len(full_text):,} chars to ingest for {doc_type}")
    except Exception as e:
        log.error("Error ingesting {} pages: {}".format(doc_type, e))

    return full_text


#####
# To iteratively add the split data in a CHUNK array
#####
def add_chunks(texts, source, doc_type):
    for t in texts:
        t = t.strip()
        if t:
            CHUNKS.append({"cid": len(CHUNKS), "text": t, "source": source, "doc_type": doc_type})


#####
# To ingest manuals and standard operating procedures stored at a given location
#####
def ingest_manuals_sops() -> str:
    manuals=settings.manuals_sops_list.split(",")
    manual_text=ingest_pdf(settings.manuals_and_sops, manuals, "Manuals")
    return manual_text


#####
# To concatenate text with model name & run through hash function, so same text always gives same key that can be found again
# Purpose of including model name is if models are switched later, old cached vectors won't be wrongly reused.
#####
def _ckey(text):  return hashlib.sha1(("gemini-embedding-001::" + text).encode("utf-8")).hexdigest()


#####
# To check if given text is already embedded
#####
def _cget(text):
    p = os.path.join(CACHE_DIR, _ckey(text) + ".json")
    if os.path.exists(p):
        with open(p) as f:
            return json.load(f)
    return None


#####
# To write the given vector into a JSON file
#####
def _cput(text, vec):
    with open(os.path.join(CACHE_DIR, _ckey(text) + ".json"), "w") as f:
        json.dump(vec, f)


#####
# To back-off before reattempting the request, when we hit the Rate limiting barriers
#####
def _with_backoff(fn):
    for attempt in range(5):
        try:
            return fn()
        except Exception as e:
            if "429" in str(e) and attempt < 4:
                time.sleep(2 ** attempt)   # 1,2,4,8s backoff on rate limits
            else:
                raise


#####
# To create and return the list of vectors (in same order) for the given list of chunks
# Embeds many texts; cache hits cost nothing, misses are embedded in throttled batches.
#####
def embed_texts(texts):
    out, todo = [None] * len(texts), []
    for i, t in enumerate(texts):
        v = _cget(t)
        out[i] = v
        if v is None:
            todo.append(i)
    if todo:
        log.info(f"  {len(todo)} new chunks to embed ({len(texts) - len(todo)} served from ./{CACHE_DIR}).")
    for b in range(0, len(todo), BATCH):
        idx = todo[b:b + BATCH]
        vecs = _with_backoff(lambda: _base.embed_documents([texts[i] for i in idx]))
        for i, v in zip(idx, vecs):
            out[i] = v
            _cput(texts[i], v)
        if b + BATCH < len(todo):
            log.info(f"Embedded {b + len(idx)}/{len(todo)}; pausing {PAUSE}s (rate limit)")
            time.sleep(PAUSE)
    return out


#####
# To embed the user's search question
# Embedding models treat documents (the stuff you store) and queries (what users ask) slightly differently, hence two separate methods.
#####
def embed_query(text):
    v = _cget(text)
    if v is None:
        v = _with_backoff(lambda: _base.embed_query(text))
        _cput(text, v)
    return v


#####
# To split the consolidated data into multiple chunks
#####
def chunking() -> None:
    splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=120)

    add_chunks(splitter.split_text(ingest_manuals_sops())[:PAPER_CHUNKS], "Vindhya Precision Works", "Manuals")

    log.info("Total chunks created: ", len(CHUNKS))
    top_chunk=CHUNKS[0]
    log.info("\nSample manual chunk:\n", top_chunk["text"][:280])


#####
# To embed and index the chunks of data and stored as a collection into vector database
#####
def embedding_indexing() -> None:
    EMBED_DIM = len(embed_query("dimension probe"))  # gemini-embedding-001 -> 3072
    client = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
    COLLECTION = "plant-guard_manuals"

    if client.collection_exists(COLLECTION):
        client.delete_collection(COLLECTION)

    client.create_collection(
        COLLECTION,
        vectors_config=VectorParams(size=EMBED_DIM, distance=Distance.COSINE)
    )

    client.create_payload_index(
        collection_name=COLLECTION,
        field_name="doc_type",
        field_schema=PayloadSchemaType.KEYWORD
    )

    log.info(f"Embedding {len(CHUNKS)} chunks (first run throttled + cached; re-runs instant)...")
    vecs = embed_texts([c["text"] for c in CHUNKS])

    # Upload points in batches to avoid Qdrant write timeout
    BATCH_SIZE = 20

    points = [
        PointStruct(id=c["cid"], vector=vecs[c["cid"]], payload=c)
        for c in CHUNKS
    ]

    for i in range(0, len(points), BATCH_SIZE):
        batch = points[i:i + BATCH_SIZE]
        client.upsert(COLLECTION, points=batch, wait=True)

        log.info(f"Uploaded {min(i + BATCH_SIZE, len(points))}/{len(points)} chunks")

    log.info(f"Indexed {len(CHUNKS)} chunks into Qdrant (dim={EMBED_DIM}).")