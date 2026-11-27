# Intake definition parsing

**ZIP-ASSIGNMENTS-SPECIFICATION-001 · v1.0 · Owner:** Assignments maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/assignments/src/specification.rs`

## Required implementation behavior

Parse typed v1 workload description from bounded source. Check required workspace, repo/base, path/network scopes, policy and resource requirements. Retain spec digest and reject unsupported field/version before planning.

## Acceptance

**ZIP-ASSIGNMENTS-SPECIFICATION-T01.** Invalid scope or unknown mandatory field cannot allocate an execution lease.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
