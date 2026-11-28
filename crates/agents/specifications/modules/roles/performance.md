# Performance reviewer role

**ZIP-AGENTS-ROLES-PERFORMANCE-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/performance.rs`

## Boundary and inputs

Accept a bounded benchmark plan with pinned artifact, declared workload, machine and adapter revisions, resolved policy and measurement protocol. Report exact observations and environment, distinguishing interrupted, missing or incomparable cases. Use the approved unit and normalization rule for each reported metric.

## Behavior and failure handling

Compare to a baseline only when the declared compatibility conditions hold for workload, configuration and environment. Report descriptive measurements where comparison is unavailable. No threshold, regression or capacity claim can be inferred from a noncomparable observation. Run additional measurement only under authorized resource budgets.

## Acceptance

**ZIP-AGENTS-ROLES-PERFORMANCE-T01.** Measure two fixture runs and change the hardware revision in one. Verify a noncomparable result unless an approved mapping explicitly qualifies them. An absent baseline never produces a pass.
