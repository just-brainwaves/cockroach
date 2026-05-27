"""
Module  : domain.events.project_events
Purpose : Domain events: ProjectCreated, ProjectIndexed, ProjectIndexFailed, ProjectDeleted.
          Published via Redis pub/sub for real-time frontend SSE streaming.
Layer   : Domain — Event System
"""
from dataclasses import dataclass
from datetime import datetime
