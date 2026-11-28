# Terminal failure outcomes

**ZIP-TERMINAL-ERROR-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/error.rs`

## Boundary and inputs

Expose stable typed invalid-input, executable denial, policy denial, launch refusal, timeout, output limit, explicit cancellation, exit failure, unknown effect and cleanup-incomplete dispositions. Retain scoped safe references. Keep process output and native diagnostic strings separate from public error messages.

## Behavior and failure handling

Track verbosity, exit status, stream completeness and process-tree cleanup independently. A nonzero exit does not establish effect absence. Truncated output cannot prove success. Ambiguous dispatch or cleanup leaves original obligations under supervision. Fail authorization before disclosing process existence.

## Acceptance

**ZIP-TERMINAL-ERROR-T01.** Make a benign fixture reach the output limit and exit nonzero. Verify both observations remain attributable and the terminal status cannot be presented as successful or fully captured.
