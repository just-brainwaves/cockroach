"""
Module  : infrastructure.sandbox.docker_sandbox
Purpose : Docker-based isolated code execution sandbox.
          Spawns short-lived containers with enforced resource limits
          (CPU, memory, network-off) for safe crash reproduction and
          dynamic code validation during analysis.
Layer   : Infrastructure — Security Sandbox
"""
