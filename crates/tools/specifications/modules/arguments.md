# Typed tool argument parsing

**ZIP-TOOLS-ARGUMENTS-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/arguments.rs`

## Boundary and inputs

Decode bounded request bytes against the negotiated typed schema before allocating arrays, maps or derived payloads beyond their limits. Validate exact field names, scalar kinds, identifiers and path scope. Separate absent, explicit null and unsupported values according to the declared edition.

## Behavior and failure handling

Normalize deterministically for the invocation digest while preserving array order where meaningful. Reject unknown mandatory fields, duplicate keys and arbitrary command text where the schema expects typed values. Neither argument value nor normalization authorizes a path or destination. Keep payload bytes out of denial diagnostics.

## Acceptance

**ZIP-TOOLS-ARGUMENTS-T01.** Submit an arbitrary command string for a structured argument schema, a duplicate key and an over-limit list. Each fails before adapter use. Equivalent allowed maps yield the same canonical argument identity.
