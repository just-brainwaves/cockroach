"""
Module  : runtime.log_correlation.log_ingester
Purpose : Structured log ingestion and normalisation.
          Accepts structlog / JSON-format logs, normalises field names,
          extracts trace IDs, user IDs, and service names for correlation.
Layer   : Runtime — Log Intelligence
"""
