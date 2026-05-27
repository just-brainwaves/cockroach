"""
Module  : graph.impact_analysis.change_impact
Purpose : Analyses the production risk of a git diff or proposed code change.
          Takes a set of modified files, computes downstream impact via graph,
          and produces a risk-ranked impact report for pre-deployment review.
Layer   : Graph — Impact Analysis
"""
