# Instruction bundle provenance

**ZIP-REPOSITORY-INSTRUCTIONS-VALIDATION-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/instructions/validation.rs`

## Required implementation behavior

Bind stable content digest, pinned commit and exact target paths. Reject truncated, skipped or unauthorized interpretation. Revalidate after head/scope change when required.

## Acceptance

**ZIP-REPOSITORY-INSTRUCTIONS-VALIDATION-T01.** Unreadable or changed instruction prevents stale approved mutation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
