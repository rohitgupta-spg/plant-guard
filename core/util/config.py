from __future__ import annotations
from pydantic_settings import BaseSettings, SettingsConfigDict


"""
    Dynamically loads the environment variables from .env file stored at the project root directory.
"""
class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env", env_prefix="", extra="ignore"
    )

    events: str = ""
    evaluation_set: str = ""

    assets: str = ""
    asset_classes: str = ""
    asset_criticality: str = ""
    telemetry: str = ""
    telemetry_pressure: str = ""
    purchase_orders: str = ""
    work_orders: str = ""
    work_order_details: str = ""
    inventory: str = ""
    suppliers: str = ""
    part_suppliers: str = ""
    criticality_definition: str = ""
    criticality_matrix: str = ""
    technicians: str = ""
    technician_calendar: str = ""

    manuals_and_sops_pdf: str = ""
    manuals_and_sops_md: str = ""

    checkpointer_db: str = ""

    google_api_key: str = ""
    llm_model: str = ""
    supermemory_api_key: str = ""
    user_id: str = ""

    qdrant_api_key: str = ""
    qdrant_url: str = ""

    langfuse_secret_key: str = ""
    langfuse_api_key: str = ""
    langfuse_url: str = ""

    manuals_sops_list: str = ""
    # sops_list: str = ""



settings = Settings()
