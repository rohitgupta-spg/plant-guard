from typing import TypedDict

class State(TypedDict, total=False):
    raw: str
    event: dict
    history: object
    facts: object
    procedures: object
    sources: list
    recommendation: dict
    approved: bool
    approved_by: str
    result: str