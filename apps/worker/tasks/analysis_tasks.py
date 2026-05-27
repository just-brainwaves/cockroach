"""
Module  : apps.worker.tasks.analysis_tasks
Purpose : Celery tasks for AI-powered analysis and root cause investigation.
          Runs the LangGraph debug workflow, writes findings to Postgres,
          and publishes progress events to Redis pub/sub for SSE streaming.
Layer   : Application — Background Jobs
Tasks:
  run_root_cause_analysis(analysis_id, context)
  run_architecture_analysis(project_id)
  run_security_scan(project_id)
  run_performance_analysis(project_id)
"""
from apps.worker.main import app as celery_app
