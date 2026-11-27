# Stable structural diff

**ZIP-REPOSITORY-GIT-DIFF-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/diff.rs`

## Required implementation behavior

Return old/new paths, modes and object IDs, type change and rename metadata under bounded scan. Authorize both paths and treat binary/symlink modes explicitly.

## Acceptance

**ZIP-REPOSITORY-GIT-DIFF-T01.** Renaming from authorized Markdown into sensitive path is denied.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
