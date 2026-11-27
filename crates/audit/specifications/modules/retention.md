# Evidence-preserving reclamation

**ZIP-AUDIT-RETENTION-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/retention.rs`

## Required implementation behavior

Apply policy cutoff after pinned evidence/retention checks. Delete only with approved signed or verifiable segment checkpoint and bounded execution.

## Acceptance

**ZIP-AUDIT-RETENTION-T01.** Pinned release segment survives pruning and earliest cursor updates atomically.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
