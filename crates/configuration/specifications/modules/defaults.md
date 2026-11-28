# Versioned baseline defaults

**ZIP-CONFIGURATION-DEFAULTS-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/defaults.rs`

## Boundary and inputs

Accept a trusted artifact descriptor for the base defaults, declared byte budget, expected digest and schema registry. The launcher supplies the descriptor and budget. Parse with [bounded parser](parser.md), verify the digest over the exact bytes and select the exact declared base edition before normalizing. Raw source failures never replace an already active snapshot.

## Behavior and failure handling

Validate all required keys once and reject unknown or duplicate entries. For supported v1 input delegate the only qualified migration to [migration](migration.md). A current v2 release baseline must validate directly and must never call the v1 migration as a fallback. Import defaults and resolved key origins as one typed layer. A missing field, digest mismatch, unsupported edition or unrepresentable value blocks the candidate. The input path and contents are not public diagnostics.

## Acceptance

**ZIP-CONFIGURATION-DEFAULTS-T01.** Remove a required limit from v2, provide a v1 source plus a verified v2 baseline, and corrupt the baseline bytes. Observe denial, complete staged migration and denial respectively. Verify a previous snapshot is retained on a failed reload.
