# Scoped request admission

**ZIP-NETWORKING-RATE-LIMIT-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/rate_limit.rs`

## Required implementation behavior

Reserve request rate credits per configured actor/provider scope using injected monotonic time. Honor bounded retry-after without granting new scope.

## Acceptance

**ZIP-NETWORKING-RATE-LIMIT-T01.** Concurrent requests cannot exceed capacity or advance quota after denial.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
