# Resource facade

**ZIP-RESOURCES-LIB-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/lib.rs`

## Required implementation behavior

Expose demand vectors, admission, leases and discovered capability DTOs through explicit modules; composition injects host probes and policy. No admission outside the authoritative allocator.

## Acceptance

**ZIP-RESOURCES-LIB-T01.** A consumer can construct requests without triggering hardware enumeration.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
