"""
Module  : infrastructure.sandbox.executor
Purpose : Sandboxed execution orchestrator — abstracts Docker (Phase 1) and
          Firecracker microVM (future upgrade) behind a common Executor interface.
          Enforces timeout policies and captures stdout/stderr/exit-code.
Layer   : Infrastructure — Security Sandbox
"""
