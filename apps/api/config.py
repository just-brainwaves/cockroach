"""
Module  : apps.api.config
Purpose : API-level typed configuration loaded from environment variables.
          Single import point for all settings used by routes and middleware.
Layer   : Application — Configuration
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+asyncpg://user:password@localhost/cockroach"
    redis_url: str = "redis://localhost:6379/0"
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"
    secret_key: str = "dev-secret"
    environment: str = "development"
    log_level: str = "INFO"


settings = Settings()
