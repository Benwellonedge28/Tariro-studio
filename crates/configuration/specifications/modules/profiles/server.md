# Server profile rules

**ZIP-CONFIGURATION-PROFILES-SERVER-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/profiles/server.rs`

## Boundary and inputs

Apply the validated [server manifest](../../../../../configurations/profiles/server.toml) for headless, resource-admitted scheduling and local best-fit inference. Its derivation markers ask Resources for finite model and agent slot bounds. Audit and retention remain governed by their approved configuration, and services consume the profile as preference data only.

## Behavior and failure handling

Select a local service binding only where process configuration already permits it. For a non-loopback listener require approved bind scope, service identity and networking policy at the server composition boundary. Activation of this profile leaves deployment and listener creation to that boundary. Unknown or stale resource evidence denies affected new work while verified cleanup remains independently possible.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-SERVER-T01.** Activate server preferences under local-only policy and verify no non-loopback bind. Supply an authorized non-loopback configuration with an invalid service identity and verify denial. Test separate capacity-limited scheduling on two qualified host snapshots.
