# Invocation intent and idempotency

**ZIP-TOOLS-INVOCATION-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/invocation.rs`

## Required implementation behavior

Bind tool/version, normalized arguments, effect digest, grant, lease, runtime deadline and request identity. Replay same receipt for identical committed request, reject payload drift.

## Acceptance

**ZIP-TOOLS-INVOCATION-T01.** Lost response preserves pending intent and cannot trigger duplicate mutation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
