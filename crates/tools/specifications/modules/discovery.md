# Bounded discovery of available tools

**ZIP-TOOLS-DISCOVERY-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/discovery.rs`

## Required implementation behavior

Read consented local or scoped remote registries under resource budget, report negotiation and unsupported capability explicitly. Discovery outcome creates no live grants.

## Acceptance

**ZIP-TOOLS-DISCOVERY-T01.** Offline discovery emits zero remote requests.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
