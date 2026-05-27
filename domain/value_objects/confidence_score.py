"""
Module  : domain.value_objects.confidence_score
Purpose : ConfidenceScore immutable value object (0.0–1.0).
          Encapsulates validation, comparison operators, and human-readable
          labels: Critical (>0.85), High (>0.70), Medium (>0.50), Low (≤0.50).
Layer   : Domain — Value Objects
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ConfidenceScore:
    value: float

    def __post_init__(self):
        if not 0.0 <= self.value <= 1.0:
            raise ValueError(f"Confidence must be 0.0–1.0, got {self.value}")

    @property
    def label(self) -> str:
        if self.value > 0.85: return "Critical"
        if self.value > 0.70: return "High"
        if self.value > 0.50: return "Medium"
        return "Low"
