# Structured redaction rules

**ZIP-SECURITY-SECRETS-REDACTION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/secrets/redaction.rs`

## Required implementation behavior

Classify fields before serialization, strip classified secrets from logs and recursively redact allowed diagnostics. Never copy raw errors without filtering.

## Acceptance

**ZIP-SECURITY-SECRETS-REDACTION-T01.** Synthetic canary absent in error, audit, telemetry, and model input.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
