# Distributed profile rules

**ZIP-CONFIGURATION-PROFILES-DISTRIBUTED-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/profiles/distributed.rs`

## Boundary and inputs

Read the [distributed manifest](../../../../../configurations/profiles/distributed.toml) through the named profile registry. Its concurrency and inference settings express preferences, and its approved-nodes locality restricts candidate placement to identities verified by the owning composition. The profile contributes derivation declarations for agent and generation-model slots. Each entitled node's pool remains associated with its own qualified observation revision.

## Behavior and failure handling

Validate node identity, liveness and egress grant separately before distributed discovery or placement. A stale advertisement or missing grant removes the affected node from consideration. Do not add disconnected capacity to local capacity. Local work may continue when its own capability, assignment policy and admission permit it. A selected remote proposal still requires the owning networking and execution checks before any data leaves the installation.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-DISTRIBUTED-T01.** Disconnect the mesh and supply one stale and one revoked advertisement. Verify zero unauthorized calls, no admitted remote work, unchanged local accounting and normal local execution when separately permitted.
