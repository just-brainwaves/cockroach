"""
Module  : apps.worker.tasks.indexing_tasks
Purpose : Celery tasks for the repository indexing pipeline.
          Orchestrates: scanner → parser → embedder → graph_builder.
          Tasks are idempotent and resumable — safe to retry on failure.
Layer   : Application — Background Jobs
Tasks:
  index_repository(project_id, repo_path)   — Full index from scratch
  reindex_changed_files(project_id, paths)  — Incremental update
  purge_project_index(project_id)           — Clean all indexed data
"""
from apps.worker.main import app as celery_app
