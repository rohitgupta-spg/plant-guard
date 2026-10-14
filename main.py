import logging
from tabulate import tabulate

from core.util.config import settings
from core.util.logging import setup_custom_logger
from core.util.utils import validate
from core.datamodel.maintenance_event import MaintenanceEvent
from core.service.rag import retrieve
from core.eval.run_eval import run


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)


def init():

    ## validate all the maintenance events are in adherence with schema; filter out invalid_events at this stage
    valid_events, invalid_events = validate(settings.events, MaintenanceEvent)
    log.info(f"Quick break-up as {len(valid_events)} valid events and {len(invalid_events)} invalid events, listed below with respective failure message:")
    log.info("\n"+tabulate(invalid_events, headers="keys", tablefmt="fancy_grid"))

    ## persist technicians & technician calendar using supermemory (semantic & episodic)
    # persist_data_to_memory(settings.technician_calendar, "episodic", "shift_start")

    ## register all the tools developed with LLM framework

    ## build RAG pipeline with Manuals and SOPs
    # build_index()
    # for payload, score in retrieve("bearing vibration alarm setpoint", asset_class="MANUAL-PUMP-CENT"):
    #     print(round(score, 2), payload["doc"], payload["section"])



if __name__ == '__main__':

    init()
    run()
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

    # chunking()
    # embedding_indexing()

    # technician_available = get_available_technician("Mechanical", "2026-08-10", 'B')
    # log.info("\n" + tabulate(technician_available, headers="keys", tablefmt="fancy_grid"))
    # pprint(technician_available, width=300)
