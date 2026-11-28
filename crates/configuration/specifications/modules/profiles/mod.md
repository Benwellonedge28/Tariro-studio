# Named profile dispatch

**ZIP-CONFIGURATION-PROFILES-MOD-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/profiles/mod.rs`

## Boundary and inputs

Resolve a stable profile identifier from the exact edition and registered input artifact. Map the identity to one complete validated profile and digest. Keep recognized but uninstalled profile definitions unavailable. Parse explicit overrides and derive-from-admission declarations through the [configuration registry](../schema.md). Selection is deterministic and has no platform probe or network side effect.

## Behavior and failure handling

Reject duplicate IDs, unknown keys, conflicting override and derivation for one key, and derivation unsupported by the registered key. Carry an authorized derivation marker without a numeric fallback. Remove the corresponding numeric defaults preference only where a valid marker applies. Resources performs finite derivation from qualified demand and observations under mandatory caps. Profile choice never alters an authorization grant. Keep input versions and active origins in the snapshot.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-MOD-T01.** Select unknown, recognized but missing, and registered profiles. Only the registered case resolves. Inject a key appearing in both override and derive lists. Refuse activation, preserve the prior generation, and verify that available host memory did not influence profile identity.
