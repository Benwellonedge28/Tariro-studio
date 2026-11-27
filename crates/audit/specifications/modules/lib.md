# Audit service facade

**ZIP-AUDIT-LIB-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/lib.rs`

## Required implementation behavior

Expose append, scoped query, export and verification while isolating protected storage and credential fields.

## Acceptance

**ZIP-AUDIT-LIB-T01.** Raw domain payload cannot bypass redaction via public append API.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
