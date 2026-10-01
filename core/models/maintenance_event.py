from pydantic import BaseModel
from core.models.reading import Reading
from core.models.ground_truth import GroundTruth

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