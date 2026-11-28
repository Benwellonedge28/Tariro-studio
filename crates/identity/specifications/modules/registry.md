# Canonical identity indexing

**ZIP-IDENTITY-REGISTRY-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/registry.rs`

## Boundary and inputs

Index stable typed principal IDs and exact qualified issuer and subject bindings through the Identity journal. Keep authoritative mapping, revision and retirement state in one scoped snapshot. Resolve lookup only after caller scope is verified. Neither a registry match nor display metadata constitutes proof.

## Behavior and failure handling

Enforce scoped uniqueness under a single transaction. An overlapping nonidentical issuer binding or duplicate stable ID conflicts without partial index writes. Return prior receipt for exact authorized replay. Retain historical epoch and retirement fences. Fail closed if any required index or mapping is inconsistent with its records after restart.

## Acceptance

**ZIP-IDENTITY-REGISTRY-T01.** Race two different principal IDs against the same issuer/subject enrollment. One mapping may commit and both indices remain aligned. Restart and verify an exact replay cannot revive a retired mapping.
