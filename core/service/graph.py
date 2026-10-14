import logging, sqlite3, json
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer
from networkx.classes import is_empty

from core.datamodel.maintenance_event import MaintenanceEvent
from core.datamodel.recommendation import Recommendation
from core.datamodel.state import State
from core.util.config import settings
from core.util.logging import setup_custom_logger
from core.service.llm import extract
from core.service.rag import retrieve
from core.service.memory import (log_episode, recall_episodes, asset_profile, recall_procedures, format_memory_context, MemoryUnavailable)


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)


#Custom serializer directly to the checkpointer's serde argument to explicitly handle json.dumps and json.loads
class StrictTextJSONSerializer:
    def dumps(self, obj):
        # Convert LangGraph state to clean text string
        return json.dumps(obj).encode('utf-8')

    def loads(self, data):
        # Read back the text string safely
        return json.loads(data.decode('utf-8'))


def _log(s, outcome, approved_by=None):
    try:
        log_episode(s["event"], s["recommendation"]["action"], outcome, approved_by)
        return outcome
    except MemoryUnavailable:
        log.error(f"Memory Unavailable: {s['event']}")
        return f"{outcome} (NOT LOGGED: memory unavailable, flag for human)"


def intake(s):
    return {"event": extract(MaintenanceEvent, s["raw"]).model_dump()}


def root_cause(s):
    e = s["event"]
    query = e["probable_fault"] or e["raw_text"]
    try:
        history = recall_episodes(e["asset_tag"], n=5)
        facts   = asset_profile(e["asset_tag"])
        procs   = recall_procedures(e["asset_code"], query)
    except MemoryUnavailable:
        history = facts = procs = "UNAVAILABLE"      # distinct from "no history"
    return {"history": history, "facts": facts, "procedures": procs,
            "sources": retrieve(query, e["asset_code"])}


def recommend(s):
    ctx = "\n\n".join(f"[{p['doc']}#{p['section']}] {p['text']}" for p, _ in s["sources"])
    prompt = f"""Event: {s['event']}\nHistory: {format_memory_context(s["history"], s["facts"], s["procedures"])}\nSources:\n{ctx}
        Propose ONE maintenance action using only the sources. Return JSON:
        {{"action": str, "safety_critical": bool, "citations": ["doc#section"], "action_tags": [str]}}
        If the sources are insufficient, return action "INSUFFICIENT_SOURCES" with empty citations."""

    rec = extract(Recommendation, prompt)      # a Pydantic model for Recommendation
    return {"recommendation": rec.model_dump()}


def route(s):
    if s["event"]["sensor_suspect"]:            return "human_review"
    # if (not s["recommendation"]["safety_critical"]
    #         and len(s["recommendation"]["citations"]) == 0
    #         and s["recommendation"]["action"] == 'INSUFFICIENT_SOURCES'):   return "human_review"
    if s["recommendation"]["safety_critical"]:  return "approval"
    return "autolog"


def approval(s):
    #ToDo: need to work on the human approval piece where the pipeline interrupted and to be resumed by human-in-loop
    # d = interrupt({"needs_signoff": s["recommendation"]})
    # return {"approved": bool(d.get("approved")), "approved_by": d.get("approver")}
    return {"approved": True, "approved_by": "grohit"}


def autolog(s):
    return {"result": _log(s, "auto")}

def human_review(s):
    return {"result": _log(s, "human_review")}

def refuse(s):
    return {"result": _log(s, "refuse")}

def execute(s):
    outcome = "executed" if s["approved"] else "rejected by human"
    return {"result": _log(s, outcome, s.get("approved_by"))}


"""Entry point to the app execution"""
def kick_off(text: str, cfg: dict):
    log.debug("Now defining Stategraph for the pipeline execution")

    #Now creating a state graph and transitions from each node via respective edge
    g = StateGraph(State)
    for n, f in [("intake", intake), ("root_cause", root_cause), ("recommend", recommend),
                 ("approval", approval), ("autolog", autolog), ("human_review", human_review), ("execute", execute), ("refuse", refuse)]:
        g.add_node(n, f)

    #The fixed linear part: start → intake → root_cause → recommend.
    g.add_edge(START, "intake")
    g.add_edge("intake", "root_cause")
    g.add_edge("root_cause", "recommend")

    #The conditional flow i.e. after recommend go as per the node.
    g.add_conditional_edges("recommend", route, ["approval", "autolog", "human_review", "refuse"])

    #The unconditional flow
    g.add_edge("approval", "execute")

    for n in ("autolog", "human_review", "execute", "refuse"):
        g.add_edge(n, END)

    #check_point = SqliteSaver(sqlite3.connect(settings.checkpointer_db, check_same_thread=False))
    conn = sqlite3.connect(
        settings.checkpointer_db,
        check_same_thread=False,
        detect_types=sqlite3.PARSE_DECLTYPES  # for matching underlying raw binary data types
    )
    check_point = SqliteSaver(
        conn=conn,
        serde=JsonPlusSerializer()
    )
    app = g.compile(checkpointer=check_point)
    log.debug("Stategraph compiled from the last checkpoint")

    return app.invoke({"raw": text}, cfg)                    # stops at the interrupt
    #ToDo: need to work on the piece where the pipeline interrupted (likely due to SAFETY critical) to be resumed
    # As the above code stops at the interrupt, the below code should pop-up a dialog-box to user for approval to resume
    app.invoke(Command(resume={"approved": True}), cfg)      # a human resumes it later