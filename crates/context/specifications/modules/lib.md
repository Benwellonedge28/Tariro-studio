# Context construction boundary

**ZIP-CONTEXT-LIB-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/lib.rs`

## Required implementation behavior

Export authorized requests, immutable bundles and provenance; inject tokenizer and repository reads. Linking cannot fetch context.

## Acceptance

**ZIP-CONTEXT-LIB-T01.** A client can validate DTOs without opening a repository.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
