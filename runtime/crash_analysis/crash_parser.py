"""
Module  : runtime.crash_analysis.crash_parser
Purpose : Parses raw crash dumps, panics, and unhandled exception traces.
          Normalises Python tracebacks, Rust panics, JVM stack traces,
          and Node.js errors into a unified CrashEvent schema.
Layer   : Runtime — Crash Intelligence
"""
