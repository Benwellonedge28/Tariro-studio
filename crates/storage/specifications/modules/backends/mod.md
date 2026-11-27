# Backend selection boundary

**ZIP-STORAGE-BACKENDS-MOD-001 · v1.0 · Owner:** Storage maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/storage/src/backends/mod.rs`

## Required implementation behavior

Map approved backend IDs to adapters only after capability validation. Keep backend-specific storage types outside public domain DTOs and differentiate unsupported from unavailable.

## Acceptance

**ZIP-STORAGE-BACKENDS-MOD-T01.** New or unknown backend ID cannot silently activate memory storage.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
