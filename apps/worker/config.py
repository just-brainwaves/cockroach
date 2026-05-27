"""
Module  : apps.worker.config
Purpose : Celery configuration object.
          Defines queue topology (indexing_queue, analysis_queue, runtime_queue),
          task time limits, retry backoff policy, and beat schedule
          for periodic maintenance (stale-session cleanup, re-index checks).
Layer   : Application — Worker Configuration
"""


class WorkerConfig:
    broker_url = "redis://localhost:6379/0"
    result_backend = "redis://localhost:6379/1"
    task_serializer = "json"
    task_acks_late = True            # re-queue on worker crash
    worker_prefetch_multiplier = 1   # fair dispatch for long AI tasks
    task_routes = {
        "apps.worker.tasks.indexing_tasks.*": {"queue": "indexing"},
        "apps.worker.tasks.analysis_tasks.*": {"queue": "analysis"},
        "apps.worker.tasks.runtime_tasks.*":  {"queue": "runtime"},
    }
