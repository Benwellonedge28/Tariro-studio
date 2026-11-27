# Requirement consistency and testability

**ZIP-ENGINEERING-REQUIREMENTS-VALIDATION-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/requirements/validation.rs`

## Required implementation behavior

Validate IDs, version, scope and objective checks, flag unmet input or conflicting obligations. Preserve independent review status.

## Acceptance

**ZIP-ENGINEERING-REQUIREMENTS-VALIDATION-T01.** Contradictory limits remain blocked.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
