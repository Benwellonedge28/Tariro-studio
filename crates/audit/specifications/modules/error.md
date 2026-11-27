# Audit failure classes

**ZIP-AUDIT-ERROR-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/error.rs`

## Required implementation behavior

Distinguish unavailable store, invalid record, chain mismatch, retention conflict, forbidden export and cursor expiry.

## Acceptance

**ZIP-AUDIT-ERROR-T01.** Privileged append failure blocks its required effect receipt.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
