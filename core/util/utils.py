import logging, json, supermemory, time, pathlib, re
from pydantic import BaseModel, ValidationError
from typing import Set, Type

from core.datamodel.maintenance_event import MaintenanceEvent
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
    path = settings.assets

    try:
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
    path = settings.asset_criticality

    try:
        with (open(path, "r", encoding="utf-8") as fc):
            asset_crit = json.load(fc)
            log.info(f"Loaded {len(asset_crit)} asset criticality definition records.")
    except FileNotFoundError:
        log.error(f"File not found at {path}")

        try:
            for asset in asset_crit:
                if asset["asset_tag"] == asset_tag:
                    downtime_rate = float(asset["downtime_cost_per_hour_inr"])
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


"""
    Helper function to validate the passed data item against the schema of Pydantic object
    Parameters:
        - path: path to file containing data items
        - data_object_to_validate: Pydantic object to validate against
    Returns:
        - valid_records: list of valid objects
        - invalid_records: list of invalid objects with validation error
"""
#ToDo: Remove the hardcoding of MaintenanceEvent and dynamically load the target class (e.g. similar to reflection in Java)
def validate(path: str, data_object_to_validate_against: object):
    seq_no = 0
    invalid_records, invalid_fields, valid_records = [], [], []
    allowed_fields = get_all_fields(MaintenanceEvent)
    log.debug(allowed_fields)

    try:
        with (open(path) as f):
            for event_data in f.readlines():
                seq_no += 1
                try:
                    valid_event = MaintenanceEvent(**json.loads(event_data))

                    # invalid_fields = [field for field in valid_event.ground_truth.missing_fields if field not in allowed_fields]
                    # if len(invalid_fields) > 0:
                    #     log.info(invalid_fields)
                    #     invalid_records.append({"event_seq_no":str(seq_no), "validation_error":"Invalid fields in missing fields list"})
                    # else:
                    valid_records.append(valid_event)
                except (json.JSONDecodeError, ValidationError) as e:
                    log.error(f"event_seq_no:{seq_no} validation_error:{e}")
                    invalid_records.append({"event_seq_no":str(seq_no), "validation_error":str(e)})
    except FileNotFoundError:
        log.error(f"File not found at {path}")

    return valid_records, invalid_records


# Write a memory into the store (each is stored as a document, tagged with its kind).
def remember(text, kind, **extra):
    mem = supermemory.Supermemory(api_key=settings.supermemory_api_key)
    return mem.add(content=text, container_tag=settings.user_id, metadata={"type": kind, **extra})


# To save records in supermemory module for long term persistence and retrieval
def persist_data_to_memory(path: str, memory_type: str, date_column_name: str):
    try:

        with (open(path, "r", encoding="utf-8") as ds):
            dataset = json.load(ds)
            log.info(f"Loaded {len(dataset)} records to be persisted in {memory_type} memory.")

            for item in dataset:
                remember(item[0],
                         memory_type, item[0](date_column_name))
    except FileNotFoundError:
        log.error(f"File not found at {path}")


"""
    Helper function to break the text into chunks.
    Parameters:
        - path: Path of the resource to be chunked
    Returns:
        - Returns the chunks of data     
"""
def chunk_markdown(path: pathlib.Path):
    doc_id = path.stem
    for i, sec in enumerate(re.split(r"\n(?=#{1,3} )", path.read_text())):
        log.debug(f"Creating chunks for document {doc_id}")
        if sec.strip():
            # log.debug(f"Chunked text for document {sec.strip()}")
            yield {"text": sec.strip(), "doc": doc_id, "section": i,
                   "asset_class": doc_id.split("_")[0].upper()}   # for now asset class is same as manual document name


