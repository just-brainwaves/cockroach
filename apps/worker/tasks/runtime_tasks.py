"""
Module  : apps.worker.tasks.runtime_tasks
Purpose : Celery tasks for processing incoming production telemetry.
          Handles log correlation, OTLP trace analysis, anomaly detection,
          and cross-referencing runtime signals with the knowledge graph.
Layer   : Application — Background Jobs
Tasks:
  process_log_batch(project_id, log_entries)
  analyze_trace(project_id, trace_id)
  detect_anomalies(project_id, window_seconds)
  correlate_crash(project_id, crash_event_id)
"""
from apps.worker.main import app as celery_app
