# Immutable observed result

**ZIP-VERIFICATION-EVIDENCE-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/evidence.rs`

Raw observations are untrusted until validated. Evidence binds evidence ID, plan and candidate digests, gate and requirement ID, input/fixture digest, policy revision, runner and version, trusted assessor identity, attempt ID, tool or assessor receipt, observed output digest and length, environment identity, verdict and scope. Provider observations additionally bind repository, exact commit and provider check/run identity. Seal using a qualified versioned codec. Credentials and unrestricted output are excluded.

Persist validated evidence through scoped Storage as immutable data with a unique evidence ID. Equal bytes under the same identity replay. Different bytes under the same identity conflict and cannot replace observations. Emit an explicit status for executed pass or failure, blocked, unavailable, skipped, cancelled or not run. A claimed executed result requires a verified receipt and an observed output reference, even if that observed output is an empty bounded artifact. Reconcile uncertain persistence by its original identity. Preserve all attempts and their provenance when the selected attempt changes.

**ZIP-VERIFICATION-EVIDENCE-T01.** Mismatch observed digest and declared seal. The result cannot satisfy a gate. Replay a matching evidence identity without duplication.
