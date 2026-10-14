import uuid, logging
from core.service.graph import kick_off
from core.util.logging import setup_custom_logger
from autologging import traced

# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)

@traced
def pipeline(text: str) -> dict:
    cfg = {"configurable": {"thread_id": f"eval-{uuid.uuid4().hex[:8]}"}}
    log.debug(f"Now processing {text} as part of thread {cfg['configurable']['thread_id']}")

    return kick_off(text, cfg)   # this points to our milestone M8 entry point: guards → RAG answer or graph run