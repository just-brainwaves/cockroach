"""
Module  : runtime.tracing.otel_collector
Purpose : OpenTelemetry OTLP trace receiver and normaliser.
          Accepts spans from instrumented services, validates schema,
          and stores normalised traces in Postgres with project association.
Layer   : Runtime — Observability Ingestion
"""
