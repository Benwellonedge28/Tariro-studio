# Network capacity probe

**ZIP-RESOURCES-DISCOVERY-NETWORK-001 · v1.0 · Owner:** Resources maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/resources/src/discovery/network.rs`

## Required implementation behavior

Record interface/scope and enforceable bandwidth class. No probe that makes external requests without egress grant. Unknown bandwidth does not authorize unrestricted transfer.

## Acceptance

**ZIP-RESOURCES-DISCOVERY-NETWORK-T01.** Offline profile produces no active probe traffic and zero unintended remote calls.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
