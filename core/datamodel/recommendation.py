from pydantic import BaseModel

class Recommendation(BaseModel):
    safety_critical: bool
    citations: list
    action_tags: list
    action: str
