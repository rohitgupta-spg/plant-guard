from pydantic import BaseModel

class GroundTruth(BaseModel):
    priority: str | None = None
    probable_fault: str | None = None
    safety_critical: bool | None = None
    requires_permit: bool | None = None
    missing_fields: list[str] | None = None