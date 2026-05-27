"""
Module  : apps.api.middleware.rate_limit
Purpose : Per-user, per-endpoint rate limiting middleware backed by Redis.
          Protects expensive AI and indexing endpoints from overuse.
          Uses sliding-window counters with configurable limits per tier.
Layer   : Application — Traffic Control
"""
from starlette.middleware.base import BaseHTTPMiddleware
