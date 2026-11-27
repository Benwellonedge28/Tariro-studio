# CLI contracts

This page defines the target workflow and the checks required before release.

## Prerequisites and behavior

Use stable JSON output via --json and human output by default. Print structured records to stdout, diagnostics to stderr, and never expose credential material.

## Procedure

Use exit codes 0 success, 2 invalid usage, 3 denied or approval required, 4 unavailable capability or dependency, 5 failed operation, 6 conflict or stale revision, and 130 cancellation. Stateful mutations use --expected-revision where applicable; --workspace overrides must pass the same gateway checks.

## Verification and recovery

run is asynchronous unless --wait; a wait deadline does not cancel the assignment unless explicitly requested. CI uses structured status and evidence rather than matching terminal text.

[Architecture](../../ARCHITECTURE.md) · [Requirements](../../REQUIREMENTS.md)

## Command families and required operands

| Family | Commands and primary operands |
| --- | --- |
| Bootstrap | `init [--profile PROFILE]`, `doctor`, `status` |
| Repository | `repo clone SOURCE`, `inspect REPO --revision REV`, `index REPO --revision REV`, `instructions REPO --revision REV --path PATH`, `review REPO --revision REV` |
| Assignment | `assignment create --file PLAN`, then `plan/run/pause/resume/cancel/status/verify ASSIGNMENT_ID` |
| Agent | `agent list`, `inspect AGENT_ID`, `configure AGENT_ID --file MANIFEST` |
| Model | `model search QUERY`, `download MODEL_REF`, `import MANIFEST`, `load/unload/benchmark MODEL_ID` |
| Workflow | `workflow validate FILE`, `run FILE`, `replay EXECUTION_ID` |
| Memory | `memory search QUERY --scope SCOPE`, `export --scope SCOPE --output PATH`, `purge --scope SCOPE` |
| Security | `security audit --scope SCOPE`, `permissions --scope SCOPE`, `revoke GRANT_ID` |
| Server | `server start`, `server stop`; local by default |
| Mesh | `mesh join INVITATION_REF`, `mesh nodes`, `mesh status`; enabled by configured capability |

A mutation emits result type, request ID, state, revision and optional effect receipt. An error emits code, request ID, safe summary and retryability. Preserve field names and exit codes within the CLI major version.
