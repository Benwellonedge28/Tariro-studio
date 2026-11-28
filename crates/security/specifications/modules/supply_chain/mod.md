# Supply-chain verification boundary

**ZIP-SECURITY-SUPPLY-CHAIN-MOD-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/supply_chain/mod.rs`

## Boundary and inputs

Compose exact artifact identity, reviewed manifest, dependency inventory, provenance, signature observations and required checks under one pinned qualification policy. Validate references and scope before handing evidence to release acceptance. Keep input integrity distinct from release authorization.

## Behavior and failure handling

Treat an unavailable mandatory observation as blocked and an observed mismatch as failed. Preserve both in the evidence. A validated signature cannot supply a missing inventory or test report. No import, scan or pure evaluation activates an artifact or initiates external fetch.

## Acceptance

**ZIP-SECURITY-SUPPLY-CHAIN-MOD-T01.** Provide a valid signature but omit required inventory. Confirm the candidate remains blocked. Restore a verified inventory and verify the same signature is still scoped to the original artifact.
