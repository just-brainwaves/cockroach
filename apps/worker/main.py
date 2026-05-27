"""
Module  : apps.worker.main
Purpose : Celery application factory for background processing.
          Configures Redis broker + result backend, sets task routing,
          concurrency, and acks-late policy for crash-safe execution.
Layer   : Application — Async Worker
"""
from celery import Celery
from apps.worker.config import WorkerConfig

app = Celery("cockroach")
app.config_from_object(WorkerConfig)
app.autodiscover_tasks(["apps.worker.tasks"])
