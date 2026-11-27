# Bounded authorized audit query

**ZIP-AUDIT-QUERY-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/query.rs`

## Required implementation behavior

Filter workspace and grant before scanning typed records. Use stream generation/cursor and admitted bytes/items. Do not fetch event payload to form summary.

## Acceptance

**ZIP-AUDIT-QUERY-T01.** Cross-workspace query exposes neither records nor hidden ranks.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
