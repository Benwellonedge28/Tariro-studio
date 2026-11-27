# Tool effect evidence

**ZIP-TOOLS-AUDITING-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/auditing.rs`

## Required implementation behavior

Append redacted intent/outcome with tool/version, request digest, grant and artifact identity. Do not log raw sensitive payloads.

## Acceptance

**ZIP-TOOLS-AUDITING-T01.** Failure to persist required intent prevents privileged dispatch.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
