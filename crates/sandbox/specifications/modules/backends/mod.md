# Backend negotiation dispatch

**ZIP-SANDBOX-BACKENDS-MOD-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/backends/mod.rs`

## Boundary and inputs

Resolve the selected platform adapter from an enrolled backend identity, edition, host capability snapshot and immutable profile. Filter candidates by current qualification of every mandatory control. Select among fitting approved adapters in configured order with a stable identity tie-break. Probing provides an observation and never a launch right.

## Behavior and failure handling

Return an unsupported-control decision when no qualified candidate fits. Never relabel optional, unavailable or untested controls as enforced. A type, host name or version string is insufficient qualification. Bind preparation and inspection to the same selected adapter revision, and invalidate launch if the binding changes.

## Acceptance

**ZIP-SANDBOX-BACKENDS-MOD-T01.** Provide an unavailable qualified option, an unconfined option and a fitting qualified option. Only the last may prepare. Remove its mandatory evidence and verify zero launches and no unconfined fallback.
