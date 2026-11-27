# Runtime health and launch readiness

**ZIP-RUNTIME-HEALTH-001 · v1.1 · Owner** Runtime maintainers. **Maturity** D4 candidate for local diagnostics.

**Planned source** `crates/runtime/src/health.rs`

## Read-only projection

Return a bounded snapshot containing lifecycle, liveness, launch readiness and stable reason codes. Include the locally observed lifecycle revision and the observed required port or recovery revisions when the caller has diagnostic scope. Read state from [lifecycle](lifecycle.md), validated wiring, and the supervisor's ownership and recovery view. Take the lifecycle and intake snapshot together. If concurrent closure or stale, missing or ambiguous port evidence prevents a credible positive readiness result, project not-ready. Do not wait for remote providers, enqueue tasks or reserve resources from a health read.

Liveness means the local control path answered this probe. A responding Draining or Failed instance may therefore be live. Installation readiness requires Running, open intake, a current supervisor, a readable and compatible journal and available mandatory local controls. A fenced task with durable recovery state prevents readiness for that task. It does not make unrelated work unavailable unless an installation-wide prerequisite is unresolved. Scoped diagnostics may also report a paused gate or attempt recovery as a denial reason. Scheduler eligibility, live authorization, resource admission and the final launch gate still decide each request.

Emit reason codes in this order when their conditions apply: `intake_closed`, `ownership_unavailable`, `journal_unavailable` (including incompatible schema), `containment_unavailable`, `scope_paused`, `recovery_pending`. Recheck the lifecycle revision before returning a ready snapshot. A changed revision yields a non-ready snapshot with `snapshot_changed` as its final reason. Multiple reasons may coexist. Return an empty reason list only when all required observations pass. If the requester lacks permission for scoped diagnostics, disclose only the installation's coarse readiness and liveness. Exclude path names, containment locators, provider data and task payloads. Use no unbounded detail list or independent polling requirement.

## Acceptance

**ZIP-RUNTIME-HEALTH-T01.** Inject a storage read failure and a responding control path. Observe live and not-ready with the stable journal reason. Restore storage, keep one fenced attempt and verify the affected task stays unavailable while an unrelated scope passes. Race a readiness read with intake closure and verify all subsequent reads report not-ready. Check unauthorized diagnostic output omits identifiers and that probes generate no control mutations or provider calls.
