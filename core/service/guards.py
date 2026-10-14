import logging
from core.util.logging import setup_custom_logger


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)


SAFETY_ACTIONS = {"loto", "isolate", "energise", "hot_work", "confined_space", "pressure_release", "bypass_interlock"}
PRESSURE_PHRASES = ("skip the paperwork", "skip lockout", "no time", "just do it", "override")

def hard_block(rec: dict, approved_by: str | None) -> tuple[bool, str]:
    if rec.get("safety_critical") and not approved_by:
        return True, "BLOCKED: safety-critical action requires human sign-off"
    if not rec.get("citations"):
        return True, "BLOCKED: unverified instruction (no manual citation)"
    if set(rec.get("action_tags", [])) & SAFETY_ACTIONS and not approved_by:
        return True, "BLOCKED: safety action without sign-off"
    return False, ""

def pressure_detected(text: str) -> bool:
    return any(p in text.lower() for p in PRESSURE_PHRASES)