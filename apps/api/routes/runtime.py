"""
Module  : apps.api.routes.runtime
Purpose : Endpoints for ingesting and querying production runtime telemetry.
          Receives OTLP traces, structured logs, and crash dumps.
          Exposes queried anomalies, error clusters, and trace timelines.
Layer   : Application — HTTP Routes
Endpoints:
  POST   /runtime/ingest/logs    — Ingest structured log batch
  POST   /runtime/ingest/traces  — Ingest OTLP trace batch
  POST   /runtime/ingest/crash   — Ingest crash dump / panic output
  GET    /runtime/{pid}/anomalies
  GET    /runtime/{pid}/incidents
  WS     /runtime/{pid}/stream   — Live log WebSocket stream
"""
from fastapi import APIRouter
router = APIRouter()
