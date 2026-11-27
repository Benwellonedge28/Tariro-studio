# Exact remote outcome reconciliation

**ZIP-DISTRIBUTED-RECONCILIATION-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/reconciliation.rs`

## Required implementation behavior

Match effect ID, node epoch, reviewed input/output hashes and real receipt. Distinguish absent, verified, conflicting and unknown outcomes.

## Acceptance

**ZIP-DISTRIBUTED-RECONCILIATION-T01.** Conflicting receipts cause blocked rather than arbitrary selection.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
