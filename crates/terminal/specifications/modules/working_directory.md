# Scoped cwd resolution

**ZIP-TERMINAL-WORKING-DIRECTORY-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/working_directory.rs`

## Boundary and inputs

Bind a rooted workspace directory through trusted composition without taking a new first-party Filesystem dependency. Require qualified root and directory identity, safe access mode, current scope generation and applicable lease binding. A relative string alone cannot supply a working directory.

## Behavior and failure handling

Recheck the exact admitted directory when the backend installs the process. Unavailable proof or changed target denies. Never silently use the ambient process directory. Return only bounded scoped diagnostics for denied paths.

## Acceptance

**ZIP-TERMINAL-WORKING-DIRECTORY-T01.** Replace a staged directory binding with a linked or unknown scoped target before launch. Verify no start and no fallback directory. A matching live binding still passes all other controls.
