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
    assets: str = ""
    telemetry: str = ""
    work_orders: str = ""
    inventory: str = ""
    evaluation_set: str = ""
    criticality_definition: str = ""
    manuals_and_sops: str = ""

    google_api_key: str = ""
    llm_model: str = ""

    qdrant_api_key: str = ""
    qdrant_url: str = ""

    langfuse_secret_key: str = ""
    langfuse_api_key: str = ""
    langfuse_url: str = ""

    manuals_sops_list: str = ""
    # sops_list: str = ""



settings = Settings()
