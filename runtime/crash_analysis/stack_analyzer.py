"""
Module  : runtime.crash_analysis.stack_analyzer
Purpose : Analyses parsed stack frames against the knowledge graph.
          Maps frames to source symbols, identifies the true origin frame
          (skipping library/framework noise), and flags cross-service boundaries.
Layer   : Runtime — Crash Intelligence
"""
