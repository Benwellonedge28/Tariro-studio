# Explicit environment construction

**ZIP-TERMINAL-ENVIRONMENT-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/environment.rs`

## Boundary and inputs

Build a finite environment from the qualified allowlist and versioned command schema. Validate names and values, reject duplicates under target comparison semantics and enforce the total envelope. Do not inherit ambient environment, search or proxy settings. Use an explicit scoped working context.

## Behavior and failure handling

Resolve authorized credential references only through the effect-local adapter and only when the exact command and destination permit it. Failure to resolve a required reference denies before launch. Keep values out of persisted specifications and diagnostics. Do not move credentials onto arguments or standard input as a fallback.

## Acceptance

**ZIP-TERMINAL-ENVIRONMENT-T01.** Add synthetic secret and routing variables to the host environment. Confirm the synthetic child sees only the approved set. Repeat with an unavailable required reference and verify no launch.
