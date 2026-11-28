# Stable load failures

**ZIP-CONFIGURATION-ERROR-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/error.rs`

## Boundary and inputs

Define ConfigError with a stable code, permitted source class, optional recognized registry key, and optional validated source position. Stable codes include UnsupportedSchema, UnknownKey, DuplicateKey, InvalidType, InvalidConfig, Oversize, PolicyConflict, Io and MigrationRequired. Format codes in lowercase snake case across interfaces. InvalidConfig covers integrity, representability and missing required data. Preserve detailed internal causes only behind bounded, authorized diagnostics without payload or secrets.

## Behavior and failure handling

Read and enforce byte limits before syntax and schema checks. Once parsed, check declared edition before registry membership and type/range. Report inability to read as Io, a known unavailable migration as MigrationRequired and an unsupported source edition as UnsupportedSchema. Confirm mandatory conflicts before activation. A concurrent snapshot revision change returns PolicyConflict and requires explicit resolution against the current base. No error exposes raw input text, environment names outside the approved map, secret references or filesystem paths.

## Acceptance

**ZIP-CONFIGURATION-ERROR-T01.** Inject a synthetic secret in malformed text, an unknown key spelling and a failure path. Assert safe codes and bounded locations without input leakage. Reject an unsupported edition containing a known wrong value using UnsupportedSchema before ordinary type checks.
