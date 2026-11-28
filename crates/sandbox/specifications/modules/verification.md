# Qualification and cleanup evidence

**ZIP-SANDBOX-VERIFICATION-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/verification.rs`

## Boundary and inputs

Collect qualification evidence for exact backend edition, environment, profile digest, required controls, fixture input, observed enforcement and whole-group termination. Distinguish advertised capability, verified installed control and observed production behavior. Keep fixture, policy and qualified adapter provenance immutable.

## Behavior and failure handling

Check mandatory denied path, network, bounded resources and descendant cleanup using synthetic fixtures and current evidence. A missing, failed or stale required case blocks positive qualification for the affected control. Verify authority, bounds and evidence scope before reusing an observation. Reference cases help specify behavior and leave native qualification open.

## Acceptance

**ZIP-SANDBOX-VERIFICATION-T01.** Inspect the exact scoped path denial, offline network fixture and descendant teardown results. Remove a required observation or change the backend edition and verify no production support may be claimed from the older evidence.
