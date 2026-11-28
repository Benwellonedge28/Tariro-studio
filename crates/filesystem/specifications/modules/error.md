# Filesystem failure decisions

**ZIP-FILESYSTEM-ERROR-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/error.rs`

## Boundary and inputs

Expose stable typed errors for PathOutsideScope, InvalidComponent, UnsafeLink, StaleFile, UnsupportedIsolation, QuotaExceeded, Io and OutcomeUnknown. Distinguish platform setup failure from an ambiguous filesystem effect. Preserve authorized evidence references, with no raw host path or private metadata in public errors.

## Behavior and failure handling

Authenticate and authorize before exposing target presence or state. Before mutation distinguish definitive denied/failed actions from ambiguity after rename or durability failure. Uncertainty uses original-intent recovery. A transient I/O code is never evidence of absence or permission to weaken a path rule.

## Acceptance

**ZIP-FILESYSTEM-ERROR-T01.** Lose a qualified replace reply after the effect boundary and verify OutcomeUnknown with stable intent. Compare denial for an unauthorized existing target and an absent target and verify equivalent public output.
