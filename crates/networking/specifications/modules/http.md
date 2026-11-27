# Bounded HTTP request adapter

**ZIP-NETWORKING-HTTP-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/http.rs`

## Required implementation behavior

Recheck origin, method and body classification prior to every hop. Enforce response byte/deadline limits and preserve truncation and ambiguous mutations.

## Acceptance

**ZIP-NETWORKING-HTTP-T01.** Redirect to unauthorized destination causes no new request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
