# Rooted filesystem facade

**ZIP-FILESYSTEM-LIB-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/lib.rs`

## Boundary and inputs

Declare the [crate modules](../../DESIGN.md), forbid unsafe first-party code and expose validated paths, scoped roots, bounded reads, snapshot views and conditional mutation commands. Keep unrestricted platform handles, lock internals and unchecked constructors outside public callers.

## Behavior and failure handling

Use Foundation and Security as the approved first-party edges. Compose platform qualification and durable intent integration through injected owners. Importing or constructing a path performs no I/O or authority checks with ambient state. Actual read and mutation require a verified scope and current platform evidence.

## Acceptance

**ZIP-FILESYSTEM-LIB-T01.** Compile a consumer using a synthetic scoped read. Confirm it cannot obtain an unrestricted root or construct a verified write handle from a relative path alone.
