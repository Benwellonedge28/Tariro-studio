# Policy-bound network facade

**ZIP-NETWORKING-LIB-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/lib.rs`

## Required implementation behavior

Expose explicit transport, scoped endpoint and capability types. Import opens no listener, resolver or external connection.

## Acceptance

**ZIP-NETWORKING-LIB-T01.** Construction under offline policy emits no packets or DNS queries.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
