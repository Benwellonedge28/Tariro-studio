# Bounded redacted agent measurements

**ZIP-AGENTS-METRICS-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/metrics.rs`

## Boundary and inputs

Collect bounded role class, lifecycle state, outcome code and elapsed-duration observations from trusted runtime signals. Require an admitted sink envelope and stable enumerated dimensions. Derive duration only within one trusted monotonic clock domain. Treat accepted observation replay as the existing event rather than a new transition.

## Behavior and failure handling

Exclude private prompts, raw tool output, repository paths, exact agent IDs, credentials and arbitrary labels. Downstream sink failure cannot change accepted state or block mandatory audit. Record a bounded drop signal when available. Export requires the owning observability policy, while durable receipts stay under audit and journal contracts.

## Acceptance

**ZIP-AGENTS-METRICS-T01.** Inject canary prompt content and many unique agent identifiers. Verify the same bounded series set, no disclosed canary, and normal state progression after sink failure.
