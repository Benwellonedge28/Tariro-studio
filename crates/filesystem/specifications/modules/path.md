# Typed relative path

**ZIP-FILESYSTEM-PATH-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/path.rs`

## Boundary and inputs

Accept a versioned relative repository path under caller-supplied byte and component constraints. Parse documented component boundaries and reject empty components, parent traversal, absolute or drive-qualified forms and invalid platform encodings. Keep original validated repository spelling separate from target lookup and display.

## Behavior and failure handling

Return immutable components only. Path construction does not resolve a root, follow links or grant read or write permission. Feed validated data into normalization and handle-relative resolution. Any conversion losing component identity fails rather than substituting a host-dependent interpretation.

## Acceptance

**ZIP-FILESYSTEM-PATH-T01.** Test a valid relative fixture, an absolute path, and a drive-qualified input from another platform. The last two fail before any backend call. Distinct display formatting cannot change path identity.
