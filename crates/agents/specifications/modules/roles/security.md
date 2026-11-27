# Security reviewer role

**ZIP-AGENTS-ROLES-SECURITY-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/security.rs`

## Required implementation behavior

Review threat boundaries, redacted evidence and qualified mitigations; no scope expansion from role alone.

## Acceptance

**ZIP-AGENTS-ROLES-SECURITY-T01.** Unreviewed mitigation cannot pass mandatory security condition.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
