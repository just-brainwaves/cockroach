"""
Module  : runtime.anomaly_detection.pattern_library
Purpose : Catalogue of known production failure patterns with detection signatures.
          Includes: retry loops, cache invalidation storms, connection pool exhaustion,
          GC pressure spirals, and distributed deadlock signals.
          Patterns feed both the statistical and ML detectors.
Layer   : Runtime — Anomaly Detection
"""
