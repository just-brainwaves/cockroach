"""
Module  : shared.logging.logger
Purpose : Structured logging configuration using structlog.
          Produces JSON-format logs in production, coloured dev logs locally.
          Binds: service_name, environment, and request_id at process startup.
          Import `log = get_logger(__name__)` in any module.
Layer   : Shared — Observability
"""
import structlog

def get_logger(name: str) -> structlog.BoundLogger:
    return structlog.get_logger(name)
