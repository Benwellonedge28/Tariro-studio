# Audit-safe data reduction

**ZIP-AUDIT-REDACTION-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/redaction.rs`

## Required implementation behavior

Allowlist operational fields and redact any secret not needed for attribution; perform before persistence and hashing. Keep safe digest references only.

## Acceptance

**ZIP-AUDIT-REDACTION-T01.** Synthetic token cannot appear in serialized audit record or logs.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
