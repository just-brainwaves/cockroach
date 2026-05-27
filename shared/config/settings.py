"""
Module  : shared.config.settings
Purpose : Global application settings — single source of truth for all
          environment-driven config. Validated at process startup with
          pydantic-settings. Import `settings` anywhere in the codebase.
Layer   : Shared — Configuration
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+asyncpg://user:password@localhost/cockroach"
    redis_url: str = "redis://localhost:6379/0"
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"
    vector_db_backend: str = "faiss"
    vector_db_path: str = "./data/faiss"
    ai_backend: str = "local"
    ai_model: str = "qwen3-coder"
    log_level: str = "INFO"
    environment: str = "development"


settings = Settings()
