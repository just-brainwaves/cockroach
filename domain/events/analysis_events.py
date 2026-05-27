"""
Module  : domain.events.analysis_events
Purpose : Domain events: AnalysisStarted, AgentStepCompleted, RootCauseFound, AnalysisCompleted, AnalysisFailed.
          Published via Redis pub/sub for real-time frontend SSE streaming.
Layer   : Domain — Event System
"""
from dataclasses import dataclass
from datetime import datetime
