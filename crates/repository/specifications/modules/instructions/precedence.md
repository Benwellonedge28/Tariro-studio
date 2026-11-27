# Instruction authority ordering

**ZIP-REPOSITORY-INSTRUCTIONS-PRECEDENCE-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/instructions/precedence.rs`

## Required implementation behavior

Apply binding system/user and scope first, then applicable root-to-leaf repository constraints. A deeper instruction cannot expand higher-level permission. Unresolved contradiction blocks.

## Acceptance

**ZIP-REPOSITORY-INSTRUCTIONS-PRECEDENCE-T01.** Nested instruction requesting network cannot override an offline assignment.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
