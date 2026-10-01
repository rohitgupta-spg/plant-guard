import logging, json
from core.util.config import settings
from core.util.utils import get_asset, get_downtime_rate
from core.util.logging import setup_custom_logger


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)



"""
    API to fetch historical sensor data (vibration, temperature, pressure & current) for a specific asset.
    Use this tool to analyze trends or identify anomaly patterns over time.
    Parameters:
        - asset_tag: Asset Tag
        - hours_back: How many hours back to look at
    Returns:
        - dict: Sensor records    
"""
def get_sensor_history(asset_tag: str, hours_back: int = 24) -> dict | None:
    asset_sensor_records = None

    try:
        path = settings.telemetry
        with (open(path, "r", encoding="utf-8") as fs):
            sensor_history = json.load(fs)
            log.info(f"Loaded {len(sensor_history)} sensor records.")
    except FileNotFoundError:
        log.error(f"File not found at {path}")

    #Check a valid entry of asset in asset register
    asset_detail = get_asset(asset_tag)

    #Only if valid entry found, build a sensor history
    if asset_detail:
        log.debug(f"Asset TAG '{asset_tag}' is found registered asset as {asset_detail} asset register.")

        asset_sensor_records = [
            record for record in sensor_history
            if record.get("asset_tag") == asset_tag and record.get("hour_index") <= hours_back
        ]
        if not asset_sensor_records:
            log.error(f"Asset TAG '{asset_tag}' doesnt have any sensor data.")
            return {"error": f"Asset TAG '{asset_tag}' doesnt have any sensor data."}
        else:
            log.info(f"Found {len(asset_sensor_records)} sensor records.")

    return {
        "asset_tag": asset_tag,
        "hours_retrieved": hours_back,
        "telemetry_log": asset_sensor_records
    }


"""
    Calculates the financial loss incurred as downtime cost if an asset is out of operation for a given duration.
    Use this tool to analyze trends or identify anomaly patterns over time.
    Parameters:
        - asset_tag: Asset Tag
        - estimated_downtime_hours: No. of hours of downtime
    Returns:
        - dict: Total downtime cost along with asset details     
"""
def calculate_downtime_cost(asset_tag: str, estimated_downtime_hours: float) -> dict:

    asset = get_asset(asset_tag)
    hourly_rate = get_downtime_rate(asset_tag)
    total_cost = hourly_rate * estimated_downtime_hours

    return {
        "asset_id": asset_tag,
        "criticality": asset["criticality"],
        "downtime_hours": estimated_downtime_hours,
        "hourly_cost_inr": hourly_rate,
        "total_estimated_loss_usd": total_cost
    }


"""
    API to fetch current stock level, supplier lead time, and pricing for a specific spare part number.
    Use this to determine if parts are immediately available for a repair job.
    Parameters:
        - part_number: Part Number
    Returns:
        - dict: Part details and stock availability     
"""
def check_spare_parts_inventory(part_number: str) -> dict:
    try:
        path = settings.inventory
        with (open(path, "r", encoding="utf-8") as fi):
            inventory = json.load(fi)
            log.info(f"Loaded {len(inventory)} inventory records.")
    except FileNotFoundError:
        log.error(f"File not found at {path}")

    part = [
        record for record in inventory
        if record.get("part_number") == part_number
    ].pop(0)

    if not part:
        return {"error": f"Part number '{part_number}' not found in inventory."}

    return {
        "part_number": part_number,
        "description": part["description"],
        "in_stock": part["on_hand"],
        "in_stock_status": "AVAILABLE" if part["on_hand"] > 0 else "OUT_OF_STOCK",
        "lead_time_days": part["lead_time_days"],
        "unit_cost_inr": part["unit_cost_inr"]
    }


"""
    API to fetch technician schedule for a given skill to identify the available technicians.
    Use this to determine if technicians are available to do the repair job.
    Parameters:
        - required_skill: Required skill
    Returns:
        - dict: Technician availability details
"""
def get_technician_schedule(required_skill: str) -> dict:
    """
    Retrieves available technicians filtered by their trade/skill type.
    Use this to schedule personnel for specific repair tasks.
    """
    matching_techs = [
        tech for tech in TECHNICIAN_SCHEDULE
        if tech["skill"].lower() == required_skill.lower() and tech["available"]
    ]

    return {
        "required_skill": required_skill,
        "available_technicians_count": len(matching_techs),
        "available_staff": matching_techs
    }