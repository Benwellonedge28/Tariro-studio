# User preference overlay

**ZIP-CONFIGURATION-USER-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/user.rs`

## Boundary and inputs

Accept a bounded immutable preference layer from a trusted source bound to the selected user and installation. Parse edition and fields through the Configuration pipeline. Registry source permissions restrict which typed preferences are writable. Keep opaque reference identifiers distinct from values and never resolve credentials here.

## Behavior and failure handling

Refuse unauthorized keys, stale identity bindings and unsupported preference migrations. Accept an obsolete field only through an explicitly registered verified migration that retains source provenance. Apply permitted user preferences in [precedence order](overrides.md). A user preference cannot widen egress, lower a mandatory quality floor or add a privileged operation. The [loader](loader.md) alone can activate a fully checked snapshot.

## Acceptance

**ZIP-CONFIGURATION-USER-T01.** Submit an allowed local presentation preference, a forbidden operation, and a value below a mandatory quality floor. Verify the permitted input resolves, the unauthorized and conflicting candidates fail, and the previous active snapshot stays available.
