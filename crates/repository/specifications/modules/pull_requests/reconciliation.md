# External publication reconciliation

**ZIP-REPOSITORY-PULL-REQUESTS-RECONCILIATION-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/pull_requests/reconciliation.rs`

Read-only recovery takes the original effect identity, sealed request and current scoped inspection authority. Use the immutable repository ID. Inspect the provider's durable receipt where available. Otherwise search via complete bounded pages for the recorded exact marker and source and target repositories and refs, including closed candidates when required. Read candidate details and compare pinned head and base, draft flag and sealed content. Return one of the following verdicts.

| Verdict | Required observation |
| --- | --- |
| Confirmed | One authoritative exact effect and all required observations match |
| Conflict | Multiple candidates with the recorded marker, an incompatible effect or a verified result that does not match the seal |
| Absent | Authoritative negative evidence and proof the original dispatch can no longer commit |
| Unresolved | Inspection incomplete, provider observation stale or ambiguous, or request settlement unknown |

Do not collapse multiple candidates by title or arbitrary order. A confirmed receipt may be replayed as historical evidence after a ref advances, but later effects still check live refs. An empty scan alone does not prove absence, even if all pages were read. A provider without settlement proof must keep delayed creation unresolved. A qualified replay from Absent uses the same identity and immutable payload under the original compare preconditions and current authorization. Never create, edit, close or merge during read-only recovery.

**ZIP-REPOSITORY-PULL-REQUESTS-RECONCILIATION-T01.** Two matching candidates block. One exact candidate confirms without another create. An empty result with unknown dispatch settlement blocks retry.
