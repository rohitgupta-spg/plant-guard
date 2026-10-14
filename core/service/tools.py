import logging
import pandas as pd

from typing import cast
from langchain_core.tools import tool
from core.util.logging import setup_custom_logger


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)


T = {n: pd.read_csv(f"./data/plantguard/mock_api/{n}.csv") for n in
     ["telemetry", "inventory", "asset_criticality", "technician_calendar", "technicians"]}


"""
    API to fetch historical sensor data (vibration, temperature, pressure & current) for a specific asset.
    Use this tool to analyze trends or identify anomaly patterns over time.
    Parameters:
        - asset_tag: Asset Tag
        - hours_back: How many hours back to look at
    Returns:
        - dict: Sensor records    
"""
def get_sensor_history(asset_tag: str, hours_back: int = 24) -> list[dict]:
    df = T["telemetry"].query("asset_tag == @asset_tag").tail(hours_back)
    return df.drop(columns=["seeded_fault"], errors="ignore").to_dict("records")
    # seeded_fault is ground truth: never expose it to the agent!


@tool("get_sensor_history_tool")
def get_sensor_history_tool(asset_tag: str, hours_back: int = 24) -> list[dict]:
    """API to fetch historical sensor data (vibration, temperature, pressure & current) for a specific asset."""
    return get_sensor_history(asset_tag, hours_back)


"""
    Calculates the financial loss incurred as downtime cost if an asset is out of operation for a given duration.
    Use this tool to analyze trends or identify anomaly patterns over time.
    Parameters:
        - asset_tag: Asset Tag
        - estimated_downtime_hours: No. of hours of downtime
    Returns:
        - dict: Total downtime cost along with asset details     
"""
def calculate_downtime_cost(asset_tag: str, estimated_downtime_hours: float) -> float:
    row = T["asset_criticality"].query("asset_tag == @asset_tag").iloc[0]

    # if we need the range of min & max cost that may occur for a given downtime, else return the value with downtime_rate
    # lo, hi = row["downtime_cost_min_inr_per_hour"], row["downtime_cost_max_inr_per_hour"]
    # return {"min_inr": lo * estimated_downtime_hours, "max_inr": hi * estimated_downtime_hours}

    rate = row["downtime_cost_per_hour_inr"]
    return float(rate * estimated_downtime_hours)


@tool("calculate_downtime_cost_tool")
def calculate_downtime_cost_tool(asset_tag: str, estimated_downtime_hours: float) -> float:
    """Calculates the financial loss incurred as downtime cost if an asset is out of operation for a given duration."""
    return calculate_downtime_cost(asset_tag, estimated_downtime_hours)


"""
    API to fetch current stock level, supplier lead time, and pricing for a specific spare part number.
    Use this to determine if parts are immediately available for a repair job.
    Parameters:
        - part_number: Part Number
    Returns:
        - dict: Part details and stock availability     
"""
def check_spare_parts_inventory(part_number: str) -> dict:
    r = T["inventory"].query("part_number == @part_number")
    log.debug(f"Loaded {len(r)} records for part number {part_number}")

    # if we need to build the schema of part details to return then fetch the part, else return as-is
    # part = r.iloc[0]

    return r.iloc[0].to_dict() if len(r) else {"error": "part not found"}


@tool("check_spare_parts_inventory_tool")
def check_spare_parts_inventory_tool(part_number: str) -> dict:
    """To fetch current stock level, supplier lead time, and pricing for a specific spare part number."""
    return check_spare_parts_inventory(part_number)


"""
    API to fetch technician schedule for a given skill to identify the available technicians.
    Use this to determine if technicians are available to do the repair job.
    Parameters:
        - required_skill: Required skill
        - required_shift: Required shift
        - required_date: Required date
    Returns:
        - dict: List of available Technician with details
"""
def get_available_technician(required_skill: str, required_date: str, required_shift: str) -> list[dict]:
    cal = T["technician_calendar"].query("date == @required_date and shift == @required_shift and available_hours > 0")
    tech = T["technicians"]
    m = cal.merge(tech, on="technician_id")
    return m[m.primary_skill.eq(required_skill) | m.secondary_skill.eq(required_skill)].to_dict("records")


@tool("get_available_technician_tool")
def get_available_technician_tool(required_skill: str, required_date: str, required_shift: str) -> list[dict]:
    """To fetch technician schedule for a given skill to identify the available technicians."""
    return check_spare_parts_inventory(required_skill,  required_date, required_shift)


TOOLS = [get_sensor_history_tool, calculate_downtime_cost_tool, check_spare_parts_inventory_tool, get_available_technician_tool]

# tools = [
#     {
#         "type": "function",
#         "function": {
#             "name": "get_sensor_history_tool",
#             "description": "Fetch historical sensor data (vibration, temperature, pressure & current) for a specific asset",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "asset_tag": {"type": "string"},
#                     "hours_back": {"type": "integer", "default": 24}
#                 },
#                 "required": ["asset_tag"]
#             }
#         }
#     },
#     # Define remaining tools...
# ]