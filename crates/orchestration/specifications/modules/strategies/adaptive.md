# Resource-aware replan

**ZIP-ORCHESTRATION-STRATEGIES-ADAPTIVE-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/strategies/adaptive.rs`

## Boundary and inputs

Read a pinned graph, applicable ceilings and fresh capacity or pressure evidence. Enumerate only bounded alternatives allowed by the assignment's committed quality, locality and permitted effects. Order equivalent fitting options by approved rank then stable identity. An unavailable required measurement yields a blocked proposal.

## Behavior and failure handling

Propose a new reviewable graph revision when an alternative fits. Retain completed evidence and settle affected active attempts under their original intents. Enlarged scope, weaker quality or changed locality requires an independently authorized revised plan. Neither pressure nor replan budget authorizes a provider call. Apply through the assignment revision check and normal scheduler admission.

## Acceptance

**ZIP-ORCHESTRATION-STRATEGIES-ADAPTIVE-T01.** Induce memory pressure with one valid smaller local option and one higher-scoring remote option outside scope. Select the local option. Remove it and verify a blocked result and zero remote calls.
