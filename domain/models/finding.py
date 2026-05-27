"""
Module  : domain.models.finding
Purpose : Finding value object. A single discovered issue with: location (file+line), severity, confidence score, and fix suggestion.
Layer   : Domain — Core Model (Framework-Independent)
"""
from dataclasses import dataclass, field
from datetime import datetime
