# Implementation gate collection

**ZIP-ENGINEERING-IMPLEMENTATION-VALIDATION-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/implementation/validation.rs`

## Required implementation behavior

Gather structural checks, required tests and scope evidence; bind every observation to exact candidate and policy.

## Acceptance

**ZIP-ENGINEERING-IMPLEMENTATION-VALIDATION-T01.** Changing candidate after test invalidates the old gate.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
