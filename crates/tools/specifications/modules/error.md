# Tool failure vocabulary

**ZIP-TOOLS-ERROR-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/error.rs`

## Boundary and inputs

Define typed invalid arguments, unsupported descriptor, capability denial, timeout, exhaustion, adapter failure and unknown effect dispositions. Carry bounded safe request and adapter references only within caller scope. Do not expose raw input, upstream messages, protected routes or credential values.

## Behavior and failure handling

Separate definite preclaim failures from potentially committed effects. A validation error produces no adapter dispatch. An ambiguous effect or receipt write requires reconciliation by original identity. A retry requires qualified proof and current authorization. Preserve specific scoped reason without returning sensitive input fragments.

## Acceptance

**ZIP-TOOLS-ERROR-T01.** Return a schema mismatch containing a synthetic private value and verify safe error output. Lose a mutation response and confirm UnknownEffect instead of validation denial or ordinary failure.
