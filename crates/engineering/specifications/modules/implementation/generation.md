# Pinned candidate generation

**ZIP-ENGINEERING-IMPLEMENTATION-GENERATION-001 · v1.0 · Owner:** Engineering maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/engineering/src/implementation/generation.rs`

## Required implementation behavior

Use approved requirements, instruction bundle and scope to stage candidate changes. Record tool provenance and unresolved assumptions.

## Acceptance

**ZIP-ENGINEERING-IMPLEMENTATION-GENERATION-T01.** Out-of-scope candidate is blocked before write.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
