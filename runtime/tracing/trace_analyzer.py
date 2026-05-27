"""
Module  : runtime.tracing.trace_analyzer
Purpose : Analyses collected trace trees for failure and performance patterns.
          Detects: broken causality chains, missing spans (silent failures),
          slow critical paths, and cross-service error propagation.
Layer   : Runtime — Observability Analysis
"""
