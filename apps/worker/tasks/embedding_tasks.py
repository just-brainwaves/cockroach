"""
Module  : apps.worker.tasks.embedding_tasks
Purpose : Celery tasks for generating and updating semantic embeddings.
          Batches embedding generation to maximise GPU/CPU throughput.
          Handles incremental updates when source files change post-index.
Layer   : Application — Background Jobs
Tasks:
  generate_embeddings_batch(project_id, chunks)
  update_file_embeddings(project_id, file_path)
  rebuild_vector_index(project_id)
"""
from apps.worker.main import app as celery_app
