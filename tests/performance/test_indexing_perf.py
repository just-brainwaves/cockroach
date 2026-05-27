"""
Tests   : tests.performance.test_indexing_perf
Purpose : Indexing pipeline performance benchmarks.
          Measures files/sec throughput, embedding latency P99, and
          Neo4j write performance at 1k / 10k / 100k file scale.
          Regressions > 15% fail CI.
"""
