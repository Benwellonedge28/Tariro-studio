# Workflow failure and block codes

**ZIP-WORKFLOWS-ERROR-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/error.rs`

```rust
#[non_exhaustive]
#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum WorkflowError {
    InvalidDefinition,
    UnsupportedVersion,
    UnsupportedCapability,
    MissingInput,
    Cycle,
    ExpansionLimit,
    Overflow,
    Denied,
    DeadlineExceeded,
    StaleCheckpoint,
    Conflict,
    InvalidArtifact,
    OutcomeUnknown,
    Unavailable,
    Cancelled,
}
```

Reject invalid shape, unknown schema, scope denials and compile failures before dispatch. A missing or invalid bound yields ExpansionLimit if its policy value cannot admit expansion. Checked integer failure yields Overflow. Verify current access before exposing workflow or artifact identity. Keep raw secrets, artifact text and unrelated scope outside diagnostics. At runtime distinguish a definitive no-effect failure from OutcomeUnknown. Unknown outcomes require original-ID reconciliation. A timeout or denied follow-on permission does not retract an already committed result.

**ZIP-WORKFLOWS-ERROR-T01.** Exceed expanded-node limits or integer representation bounds and verify typed error before scheduling any node.
