# Durable redacted record

**ZIP-AUDIT-RECORD-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/record.rs`

## Required implementation behavior

Store workspace sequence, stable actor/effect/grant refs, evidence digest, timestamp and prior/current chain digest. Normalize fields before hash and reject unauthorized extras.

## Acceptance

**ZIP-AUDIT-RECORD-T01.** Equivalent authorized record yields deterministic bytes; secrets are absent.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
