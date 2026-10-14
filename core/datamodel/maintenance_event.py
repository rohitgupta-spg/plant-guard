from typing import Literal
from pydantic import BaseModel
from core.datamodel.reading import Reading
from core.datamodel.ground_truth import GroundTruth

class MaintenanceEvent(BaseModel):
    event_id: str
    source: Literal["sensor_alarm", "shift_log", "inspection", "operator_report"]
    received_at: str
    raw_text: str
    asset_code: str
    asset_tag: str
    readings: Reading | None
    ground_truth: GroundTruth = GroundTruth()
    probable_fault: str | None = None
    priority: Literal["P1", "P2", "P3", "P4"] = "P3"
    safety_critical: bool = False
    requires_permit: bool = False
    missing_fields: list[str] = []
    sensor_suspect: bool = False
    suspect_reasons: list[str] = []
    record_id: str