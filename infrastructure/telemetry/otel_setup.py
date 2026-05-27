"""
Module  : infrastructure.telemetry.otel_setup
Purpose : OpenTelemetry SDK setup for Cockroach's own observability.
          Instruments FastAPI routes, SQLAlchemy queries, and Redis calls.
          Exports traces to OTLP endpoint (configurable — Jaeger, Grafana Tempo, etc.)
Layer   : Infrastructure — Self-Observability
"""
