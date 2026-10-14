from mcp.server.fastmcp import FastMCP
from core.util.config import settings
import pandas as pd, logging
from core.util.logging import setup_custom_logger


# First thing, Setup logging
log = setup_custom_logger(__name__, log_level=logging.DEBUG)


mcp = FastMCP("plant-guard-erp")
inv = pd.read_csv(settings.inventory_csv)
PO_APPROVAL_LIMIT_INR = 10000


@mcp.tool()
def check_stock(part_number: str) -> dict:
    """Stock level, reorder point, lead time and supplier tier for a part."""
    r = inv[inv.part_number == part_number]
    return r.iloc[0].to_dict() if len(r) else {"error": "unknown part"}

@mcp.tool()
def create_purchase_order(part_number: str, quantity: int, requested_by: str) -> dict:
    """Draft a PO. Above the limit it is created as PENDING_APPROVAL, never auto-raised."""
    r = inv[inv.part_number == part_number]
    if r.empty: return {"error": "unknown part"}
    total = float(r.iloc[0].unit_cost_inr) * quantity
    status = "PENDING_APPROVAL" if total > PO_APPROVAL_LIMIT_INR else "RAISED"
    return {"part_number": part_number, "quantity": quantity, "total_inr": total, "status": status}


if __name__ == "__main__":
    mcp.run()      # stdio transport