"""
Module  : domain.models.analysis
Purpose : Analysis aggregate. Encapsulates a debugging session with its context, agent outputs, findings, and resolution status.
Layer   : Domain — Core Model (Framework-Independent)
"""
from dataclasses import dataclass, field
from datetime import datetime
