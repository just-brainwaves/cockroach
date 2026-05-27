"""
Module  : runtime.anomaly_detection.statistical_detector
Purpose : Lightweight statistical anomaly detection for runtime metrics.
          Uses rolling z-scores and IQR to flag error rate spikes,
          latency outliers, and throughput drops — no ML overhead needed.
Layer   : Runtime — Anomaly Detection
"""
