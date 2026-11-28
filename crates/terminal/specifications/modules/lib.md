# Terminal capability facade

**ZIP-TERMINAL-LIB-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/lib.rs`

## Boundary and inputs

Declare the [Terminal modules](../../DESIGN.md) with unsafe first-party code forbidden. Export typed command, process, bounded output and stop interfaces. Keep unqualified execution handles and raw platform launch APIs private. Composition supplies the qualified launch and authorization scope.

## Behavior and failure handling

Use Foundation, Sandbox and Resources as the only first-party crate dependencies. Import and typed request construction do not spawn or contact a network. There is no arbitrary command-string entry point. Interactive operation requires its own explicitly approved capability and qualified containment.

## Acceptance

**ZIP-TERMINAL-LIB-T01.** Compile a consumer using a typed command fixture. Verify no effect at construction and that arbitrary command strings or raw process IDs cannot be passed to a public spawning constructor.
