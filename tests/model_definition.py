from datetime import time
from pydantic import BaseModel, ValidationError, Field

class Reading(BaseModel):
    vibration_mm_s: float | None = None
    temp_c: float| None = None
    pressure_bar: float| None = None
    current_a: float| None = None

class GroundTruth(BaseModel):
    priority: str | None = None
    probable_fault: str | None = None
    safety_critical: bool | None = None
    requires_permit: bool | None = None
    missing_fields: list[str] | None = None

class MaintenanceEvent(BaseModel):
    event_id: str
    source: str
    received_at: str
    raw_text: str
    asset_code: str
    asset_tag: str
    readings: Reading
    ground_truth: GroundTruth
    record_id: str




