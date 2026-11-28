# Atomic snapshot activation

**ZIP-CONFIGURATION-LOADER-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/loader.rs`

## Boundary and inputs

Accept a trusted launch context, authorized source bindings and an expected active snapshot revision. Read and verify the baseline under the bootstrap byte budget, then resolve and bound further reads using the certified layer limit intersected with trusted bootstrap or policy caps. On reload, the currently active limit also caps candidate layer reads, so the candidate cannot raise its own ingestion allowance. Optional absent layers contribute no keys. Required missing, unreadable, untrusted or invalid layers block the candidate.

## Behavior and failure handling

Take one consistent generation of source and mandatory policy references. Parse each input with [parser](parser.md), stage migration, validate permitted source classes, resolve preferences and apply policy intersections. Validate the full effective snapshot before activation. Install using a compare-and-swap of the captured active revision and current authority revision. Avoid file and adapter I/O while holding the publication lock. Cancel before the swap without changing active state. If cancellation follows the swap, return the committed generation. Readers see complete old or new revisions only.

## Acceptance

**ZIP-CONFIGURATION-LOADER-T01.** Fail reads, validation and authority checks independently under reload. Race two candidates against the same active revision. Exactly one may activate, and a stale candidate cannot overwrite it. Confirm a candidate that increases its limit cannot ingest more bytes during that reload.
