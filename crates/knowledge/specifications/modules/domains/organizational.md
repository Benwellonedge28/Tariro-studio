# Scoped organization graph

**ZIP-KNOWLEDGE-DOMAINS-ORGANIZATIONAL-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/domains/organizational.rs`

## Required implementation behavior

Represent organizations, workspaces and attributed roles from verified service data. Graph records do not grant authority.

## Acceptance

**ZIP-KNOWLEDGE-DOMAINS-ORGANIZATIONAL-T01.** Organization graph lookup cannot authorize workspace access.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
