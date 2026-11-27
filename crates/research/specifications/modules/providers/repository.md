# Pinned repository evidence adapter

**ZIP-RESEARCH-PROVIDERS-REPOSITORY-001 · v1.0 · Owner:** Research maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/research/src/providers/repository.rs`

## Required implementation behavior

Use immutable repository ID and commit, verify path/blob and qualify scope. Partial index remains incomplete.

## Acceptance

**ZIP-RESEARCH-PROVIDERS-REPOSITORY-T01.** Reference to moved file in current head does not falsely prove historical citation.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
