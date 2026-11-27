# Bounded verification report

**ZIP-VERIFICATION-REPORTING-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/reporting.rs`

Generate a report from one authorized bounded snapshot of the plan, candidate and acceptance result. Place the exact candidate and plan digest, effective policy, final verdict and checked outcome counts in the summary. Emit mandatory and optional gates with stable ID, resolved attempt, status and scoped evidence link. Preserve failed, missing, skipped, cancelled, unavailable and historical observations as distinct conditions. Report secure redaction or truncation of display explicitly. An incomplete evaluation cannot inherit a passing cached report.

Use stable gate and finding order and bounded pages with snapshot identity. Preserve actual execution and approved reviewer identity where in scope. Plain-language explanations refer to observed evidence and cannot create checks or change verdict. A provider delivery acknowledgement and a verification pass are independent observations.

**ZIP-VERIFICATION-REPORTING-T01.** Remove an inaccessible evidence body from display without replacing a failed status. A report generated without executing any required test identifies it as not run.
