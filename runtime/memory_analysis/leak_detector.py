"""
Module  : runtime.memory_analysis.leak_detector
Purpose : Detects memory leak patterns from heap growth metrics and OOM events.
          Correlates growing allocation trends with code paths in the knowledge graph
          to identify the leaking allocation site with high precision.
Layer   : Runtime — Memory Intelligence
"""
