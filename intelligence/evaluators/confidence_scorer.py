"""
Module  : intelligence.evaluators.confidence_scorer
Purpose : Composite confidence scoring for root cause hypotheses.
          Combines: semantic similarity score, graph path weight,
          runtime signal alignment, and LLM self-reported certainty
          into a calibrated 0.0–1.0 confidence value.
Layer   : Intelligence — Quality Assurance
"""
