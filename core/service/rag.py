import logging
import re, pathlib
from qdrant_client import QdrantClient, models
from core.util.config import settings
from core.util.logging import setup_custom_logger
from core.util.utils import chunk_markdown
from fastembed.rerank.cross_encoder import TextCrossEncoder


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)


Q_CLIENT = QdrantClient(url=settings.qdrant_url, api_key=settings.qdrant_api_key)
RERANKER = TextCrossEncoder("Xenova/ms-marco-MiniLM-L-6-v2")
DENSE, SPARSE = "BAAI/bge-small-en-v1.5", "Qdrant/bm25"
COLLECTION = "plant-guard_manuals"


"""
    Method to upload the chunks of data and index into Vector DB.
    Parameters:
        - rebuild: On true, if collection exists then its dropped and recreated
"""
#ToDo: Remove the hardcoding of 384 sizing by dynamically probing the dimension of the model and use that
def build_index(rebuild: bool = True):
    exists = Q_CLIENT.collection_exists(collection_name=COLLECTION)

    if exists and rebuild:
        Q_CLIENT.delete_collection(collection_name=COLLECTION)
        exists = False

    if not exists:
        Q_CLIENT.create_collection(
            collection_name=COLLECTION,
            vectors_config={
                "dense": models.VectorParams(size=384, distance=models.Distance.COSINE) #384 is the output dimension of the embedding model, BAAI/bge-small-en-v1.5
            },
            sparse_vectors_config={
                "bm25": models.SparseVectorParams(modifier=models.Modifier.IDF)
            },
        )

    chunks = [c for p in pathlib.Path(settings.manuals_and_sops_md).glob("*.md") for c in chunk_markdown(p)]
    log.info(f"Total {len(chunks)} chunks created for {COLLECTION}")

    Q_CLIENT.upload_points(
        collection_name=COLLECTION,
        points=[
            models.PointStruct(
                id=i,
                vector={
                    "dense": models.Document(text=c["text"], model=DENSE),
                    "bm25": models.Document(text=c["text"], model=SPARSE),
                },
                payload=c,
            )
            for i, c in enumerate(chunks)
        ],
    )


"""
    Retrieval method using hybrid search (dense plus BM25 fused with RRF), followed by cross-encoder rerank, then a strict answer prompt that allows refusal.
    Filter by asset class so a plausible manual for the wrong asset can't win.
    Parameters:
        - query: Content to query
        - asset_class: Asset class
        - k: Limit the count of results to focus on
"""
def retrieve(query: str, asset_class: str | None = None, k=5):
    flt = models.Filter(must=[models.FieldCondition(
        key="asset_class", match=models.MatchValue(value=asset_class))]) if asset_class else None

    log.debug(f"Now retrieving manuals for asset_class {asset_class} to query sources from {COLLECTION}")
    hits = Q_CLIENT.query_points(COLLECTION,
                                 query_filter=flt,
                                 limit=20,
                                 prefetch=[models.Prefetch(query=models.Document(text=query, model=DENSE), using="dense", limit=20, filter=flt),
                  models.Prefetch(query=models.Document(text=query, model=SPARSE), using="bm25", limit=20, filter=flt)],
                                 query=models.FusionQuery(fusion=models.Fusion.RRF)).points

    scores = list(RERANKER.rerank(query, [h.payload["text"] for h in hits]))
    ranked = sorted(zip(hits, scores), key=lambda x: -x[1])[:k]
    return [(h.payload, s) for h, s in ranked]