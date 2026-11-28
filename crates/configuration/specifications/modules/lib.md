# Public configuration boundary

**ZIP-CONFIGURATION-LIB-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/lib.rs`

## Boundary and inputs

Declare the module tree in the [crate design](../../DESIGN.md) and forbid unsafe code. Expose typed configuration data, authorized layer inputs, resolve, and the redacted error interface. Export immutable snapshots with read-only accessors so downstream consumers cannot alter effective policy or provenance. Keep parsers, raw layers, migration internals and activation synchronization inside the crate.

## Behavior and failure handling

The first-party dependency is Foundation. Application composition supplies input readers, trust verification, active policy and credential-reference capability observations through typed interfaces. Library import does not read environment, open files, perform credential lookup or activate a global snapshot. Separate pure resolution from explicit activation owned by the [loader](loader.md). Public types follow the compatibility contract and exclude concrete adapter types.

## Acceptance

**ZIP-CONFIGURATION-LIB-T01.** Compile a bounded synthetic downstream configuration consumer with only the approved edge. Use reader spies and verify importing or constructing the interface performs zero I/O. Verify the consumer cannot edit fields in a resolved snapshot or use an internal parser constructor.
