# Workspace configuration overlay

**ZIP-CONFIGURATION-PROJECT-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/project.rs`

## Boundary and inputs

Produce a typed workspace preference layer from an authorized, pinned source. Require matching workspace and project identity, a verified source revision and canonical allowed path binding supplied by composition. Resolve the content under the configuration layer byte budget. A linked or changed source that cannot be proved within the pinned scope fails before merge. Source ownership grants no organization-policy authority.

## Behavior and failure handling

Validate each key against registry source permissions. A permitted project may reduce an allowed local preference. Attempting to write egress authorization, a secret value or another installation-owned restriction yields PolicyConflict. Workspace mandatory restrictions, when separately verified, enter policy resolution from their own source. Never infer an absent preference as permission. Candidate errors leave activation to [loader](loader.md) with the previous snapshot intact.

## Acceptance

**ZIP-CONFIGURATION-PROJECT-T01.** Read a pinned workspace preference, then submit an identical file from another workspace revision and a file requesting egress. Verify only the authorized local preference participates and both denials leave the active generation and network policy unchanged.
