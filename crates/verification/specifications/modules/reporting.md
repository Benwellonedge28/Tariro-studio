# Bounded verification report

**ZIP-VERIFICATION-REPORTING-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/reporting.rs`

## Required implementation behavior

Emit candidate/plan identity, mandatory and optional verdicts, missing gates and safe evidence references. Distinguish not run, skipped and executed.

## Acceptance

**ZIP-VERIFICATION-REPORTING-T01.** Report generation cannot synthesize tests or redact a failure into success.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
