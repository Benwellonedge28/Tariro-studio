# Versioned tool manifest

**ZIP-TOOLS-MANIFEST-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/manifest.rs`

## Boundary and inputs

Validate a versioned immutable descriptor manifest naming exact tool identity, argument and result schemas, adapter edition, effect classes, maximum supported controls and trusted enrollment evidence. Normalize deterministic metadata under the declared codec and bind its approved digest. Reject duplicate identities and unsupported required fields.

## Behavior and failure handling

Require every operation to be represented by exact qualified declarations. Free-text descriptions and advertised tool metadata cannot acquire privileges. Register only after review and current scope checks. A changed manifest requires new qualification, while old records remain attributable.

## Acceptance

**ZIP-TOOLS-MANIFEST-T01.** Add an undeclared mutating operation to a valid synthetic manifest. Verify registration fails. Change the argument schema and check the new bytes do not inherit the previously reviewed digest.
