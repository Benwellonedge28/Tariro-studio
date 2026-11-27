# Read-only scoped provider discovery

**ZIP-PROVIDERS-DISCOVERY-001 · v1.0 · Owner:** Providers maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/providers/src/discovery.rs`

## Required implementation behavior

Enumerate only approved catalog or local adapters under bounded budget and scope; advertise qualified/unqualified separately.

## Acceptance

**ZIP-PROVIDERS-DISCOVERY-T01.** Discovering remote service never authorizes using it.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
