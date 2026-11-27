# Architecture design contract

**ZIP-DOCUMENTATION-DESIGN-ARCHITECTURE-001 · v1.0 · Owner:** Documentation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/documentation/src/design/architecture.rs`

## Required implementation behavior

Document tiers, trust boundaries, dependency direction and operational constraints with exact component references. Distinguish approved facts and proposed architecture.

## Acceptance

**ZIP-DOCUMENTATION-DESIGN-ARCHITECTURE-T01.** Undeclared cross-layer dependency is rejected by graph evidence.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
