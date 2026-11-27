# Scoped write staging

**ZIP-FILESYSTEM-WRITER-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/writer.rs`

## Required implementation behavior

Accept content reference, expected file revision, target handle and budget. Stage privately, verify bytes and delegate publication to atomic_write.

## Acceptance

**ZIP-FILESYSTEM-WRITER-T01.** Failure during write leaves prior destination untouched.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
