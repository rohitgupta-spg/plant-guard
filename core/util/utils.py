import logging, json
from pydantic import BaseModel
from typing import Set, Type

from core.util.config import settings
from core.util.logging import setup_custom_logger


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)


"""
    Helper function to return the asset from list of registered assets
    Parameters:
        - asset_tag: Asset Tag
    Returns:
        - asset: Asset details
"""
def get_asset(asset_tag: str) -> dict | None:
    asset = None

    try:
        path = settings.assets
        with (open(path, "r", encoding="utf-8") as fa):
            asset_registry = json.load(fa)
            log.info(f"Loaded {len(asset_registry)} asset records.")
    except FileNotFoundError:
        log.error(f"File not found at {path}")

    asset = [
        record for record in asset_registry
        if record.get("asset_tag") == asset_tag
    ].pop(0)

    if not asset:
        log.error(f"Asset TAG '{asset_tag}' not found as registered asset.")

    return asset


"""
    Helper function to return the rate at which downtime cost of an asset can be calculated
    Parameters:
        - asset_tag: Asset Tag
    Returns:
        - downtime_rate: Hourly rate of downtime
"""
def get_downtime_rate(asset_tag: str) -> float | None:
    downtime_rate = None
    asset = get_asset(asset_tag)

    try:
        path = settings.assets
        with (open(settings.criticality_definition, "r", encoding="utf-8") as fc):
            crit_def = json.load(fc)
            log.info(f"Loaded {len(crit_def)} criticality definition records.")
    except FileNotFoundError:
        log.error(f"File not found at {path}")

    if crit_def:
        criticality = asset["criticality"]

        try:
            for crit in crit_def:
                if crit["criticality"] == criticality:
                    downtime_rate = float(crit["hourly_downtime_cost_inr"])
                    break
        except (KeyError, ValueError) as e:     # to handle missing key or converting incompatible datatype issues
            log.error(f"Error fetching downtime rate for asset:{asset_tag} validation_error:{e}")

    return downtime_rate


"""
    Helper function to recursively crawl and extract all attributes (fields) of a model including nested classes
    Parameters:
        - model: Model object whose fields need to be listed
    Returns:
        - fields: List of fields
"""
def get_all_fields(model: Type[BaseModel], prefix: str = "") -> Set[str]:
    fields = set()
    for field_name, field_info in model.model_fields.items():
        current_path = f"{prefix}{field_name}" if prefix else field_name
        fields.add(current_path)

        # Get the underlying field type (handling Optional/Union wrappers)
        field_type = field_info.annotation
        if hasattr(field_type, "__args__"):  # Unwraps Optional[Type] or Union[Type, None]
            args = [arg for arg in field_type.__args__ if arg is not type(None)]
            if args:
                field_type = args[0]

        # If the nested field is another Pydantic model, recurse into it
        if isinstance(field_type, type) and issubclass(field_type, BaseModel):
            fields.update(get_all_fields(field_type))

    return fields
