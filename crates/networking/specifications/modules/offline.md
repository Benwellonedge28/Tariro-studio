# Offline policy enforcement

**ZIP-NETWORKING-OFFLINE-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/offline.rs`

## Required implementation behavior

Before resolver, or adapter startup, deny all external network actions if offline. Keep separately allowed local transport explicit.

## Acceptance

**ZIP-NETWORKING-OFFLINE-T01.** Synthetic offline request executes no DNS or outbound connect.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
