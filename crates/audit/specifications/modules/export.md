# Scoped audit export

**ZIP-AUDIT-EXPORT-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/export.rs`

## Required implementation behavior

Stage redacted filtered records and manifest, verify integrity and require explicit approved destination. Export is bounded and never grants decryption scope.

## Acceptance

**ZIP-AUDIT-EXPORT-T01.** Copy attempt to unapproved destination is denied before transfer.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
