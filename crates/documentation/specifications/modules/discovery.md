# Scoped document discovery

**ZIP-DOCUMENTATION-DISCOVERY-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/discovery.rs`

## Required implementation behavior

Read applicable repository instructions and pinned paths under cursor. Classify absent, unreadable, existent and unsupported separately.

## Acceptance

**ZIP-DOCUMENTATION-DISCOVERY-T01.** Truncated scan cannot yield definitive completeness.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
