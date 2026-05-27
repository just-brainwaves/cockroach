# Cockroach Agent System

## Agent Roster

| Agent | Trigger | Output |
|-------|---------|--------|
| CrashInvestigator | Crash dump ingested | Root cause hypothesis ranked list |
| ArchitectureAnalyst | Project scan | Architecture health report |
| ConcurrencyInspector | Runtime anomaly | Race condition / deadlock findings |
| SecurityReviewer | Manual or scheduled | Vulnerability report |
| PerformanceInvestigator | Slow trace detected | Bottleneck ranking |
| DependencyRiskAnalyzer | Dependency change | Risk assessment |

## LangGraph Workflow
```
context_retrieval → agent_dispatch → hypothesis_merge → confidence_rank → recommend
```
