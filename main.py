import json
import logging
from pprint import pprint
from pydantic import ValidationError, BaseModel

from core.util.logging import setup_custom_logger
from core.util.utils import get_all_fields
from core.tools import get_sensor_history, calculate_downtime_cost, check_spare_parts_inventory
from core.models.maintenance_event import MaintenanceEvent
from core.services.ingest_resources import chunking, embedding_indexing


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)



"""
    Validates sensor events log against the schema of Pydantic MaintenanceEvent object
    Parameters:
        - path: path to file containing events
    Returns:
        - valid_records: list of valid MaintenanceEvent objects
        - invalid_records: list of invalid MaintenanceEvent objects with validation error
"""
def validate_events(path):
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

                    invalid_fields = [field for field in valid_event.ground_truth.missing_fields if field not in allowed_fields]
                    if len(invalid_fields) > 0:
                        log.info(invalid_fields)
                        invalid_records.append({"event_seq_no":str(seq_no), "validation_error":"Invalid fields in missing fields list"})
                    else:
                        valid_records.append(valid_event)
                except (json.JSONDecodeError, ValidationError) as e:
                    log.error(f"event_seq_no:{seq_no} validation_error:{e}")
                    invalid_records.append({"event_seq_no":str(seq_no), "validation_error":str(e)})
    except FileNotFoundError:
        log.error(f"File not found at {path}")

    return valid_records, invalid_records


if __name__ == '__main__':

    # valid_events, invalid_events = validate_events(settings.events)
    #
    # log.info(f"Quick break-up as {len(valid_events)} valid events and {len(invalid_events)} invalid events, listed below with respective failure message:")
    # log.info("\n"+tabulate(invalid_events, headers="keys", tablefmt="fancy_grid"))
    # pprint(invalid_events, width=300)     # pretty print

    # sensor_records = get_sensor_history("VPW-CNC-MILL-01")
    # pprint(sensor_records, width=300)

    # downtime_cost = calculate_downtime_cost("VPW-CNC-MILL-01", 10)
    # pprint(downtime_cost, width=300)

    # part_inventory = check_spare_parts_inventory("VPW-P-00000")
    # pprint(part_inventory, width=300)

    chunking()
    embedding_indexing()

