"""
Module  : apps.api.middleware.logging
Purpose : Structured request/response logging middleware.
          Emits JSON-format access logs via structlog with:
          request_id, method, path, status_code, duration_ms, user_id.
Layer   : Application — Observability
"""
from starlette.middleware.base import BaseHTTPMiddleware
