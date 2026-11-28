# Planner role

**ZIP-AGENTS-ROLES-PLANNER-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/planner.rs`

## Boundary and inputs

Compile an immutable task DAG from the pinned goal, authorized scope, checked inputs, expected outputs, required prerequisites and approved budgets. Bind each node to stable role, write scope, acceptance criterion and evidence owner. Check bounds, missing nodes, cycles and conflicting write assumptions before returning the graph.

## Behavior and failure handling

Order nodes canonically, track alternative proposals separately and flag scope expansions or weakened requirements for consideration by the owning authority. A selected task still requires runtime admission and capability checks. The approved plan revision rather than prose from a worker governs execution.

## Acceptance

**ZIP-AGENTS-ROLES-PLANNER-T01.** Permute a complete input and compare stable outputs. Remove a mandatory prerequisite and verify no graph is accepted. Propose a new protected path and verify it remains pending required authority.
