# Stable candidate scoring

**ZIP-CONTEXT-RELEVANCE-001 · v1.0 · Owner:** Context maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/context/src/relevance.rs`

## Required implementation behavior

Score only authorized candidates with pinned query and scorer/version, then sort by score and stable identity. Record omitted counters without unsafe text.

## Acceptance

**ZIP-CONTEXT-RELEVANCE-T01.** Private document similarity cannot influence visible results.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
