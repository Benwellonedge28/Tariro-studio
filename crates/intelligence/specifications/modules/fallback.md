# Explicit fallback policy

**ZIP-INTELLIGENCE-FALLBACK-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/fallback.rs`

## Required implementation behavior

Fallback only among reviewed routes allowed for exact data and budget. Revalidate scope and classify partial requests; no remote escalation by default.

## Acceptance

**ZIP-INTELLIGENCE-FALLBACK-T01.** Missing local provider cannot activate unapproved remote fallback.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
