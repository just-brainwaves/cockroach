"""
Module  : graph.impact_analysis.blast_radius
Purpose : Computes blast radius for a given symbol, file, or service.
          Answers "If this breaks, what else breaks?" via weighted graph traversal.
          Output is a ranked list of affected artifacts with severity scores.
Layer   : Graph — Impact Analysis (Key Feature)
"""
