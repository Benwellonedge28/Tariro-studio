# Architect role

**ZIP-AGENTS-ROLES-ARCHITECT-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/architect.rs`

## Boundary and inputs

Read the approved architecture baseline, typed component inventory and dependency graph. Return a proposal binding changed interfaces, dependency edges, compatibility assumptions and exact source revisions. Leave uncertainty and out-of-scope changes visible.

## Behavior and failure handling

Validate proposed edges against the [dependency rules](../../../../../specifications/0100-architecture/dependency-rules.md) and cycle-check the affected graph before recommending adoption. Distinguish existing implementation evidence from proposed behavior. A change to implementation, exported contract or approval boundary requires its own reviewed effect.

## Acceptance

**ZIP-AGENTS-ROLES-ARCHITECT-T01.** Introduce a cycle and an edge outside the allowed graph into two otherwise valid proposals. Both fail qualification, and the reviewed baseline stays intact.
