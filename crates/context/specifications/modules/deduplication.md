# Content deduplication with trust

**ZIP-CONTEXT-DEDUPLICATION-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/deduplication.rs`

## Required implementation behavior

Deduplicate only within compatible trust and scope records; retain all required provenance links. Duplicates cannot drop mandatory authority metadata.

## Acceptance

**ZIP-CONTEXT-DEDUPLICATION-T01.** Identical text from policy and untrusted source keeps separate trust identities.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
