from pydantic import BaseModel

class Reading(BaseModel):
    vibration_mm_s: float | None = None
    temp_c: float| None = None
    pressure_bar: float| None = None
    current_a: float| None = None