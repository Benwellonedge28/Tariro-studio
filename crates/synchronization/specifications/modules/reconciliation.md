# Authoritative replica reconciliation

**ZIP-SYNCHRONIZATION-RECONCILIATION-001 · v1.0 · Owner:** Synchronization maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/synchronization/src/reconciliation.rs`

## Required implementation behavior

Compare pinned intent, apply receipt and cursor; classify confirmed, absent, conflicting or unknown. Reissue only safe operations with live grants.

## Acceptance

**ZIP-SYNCHRONIZATION-RECONCILIATION-T01.** Unknown remote apply does not trigger a duplicate write.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
