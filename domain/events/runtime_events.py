"""
Module  : domain.events.runtime_events
Purpose : Domain events: AnomalyDetected, CrashIngested, TraceCorrelated, IncidentOpened, IncidentResolved.
          Published via Redis pub/sub for real-time frontend SSE streaming.
Layer   : Domain — Event System
"""
from dataclasses import dataclass
from datetime import datetime
