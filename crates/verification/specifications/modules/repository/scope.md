# Change authorization proof

**ZIP-VERIFICATION-REPOSITORY-SCOPE-001 · v1.1 candidate · Owner** Verification maintainers

**Planned source** `crates/verification/src/repository/scope.rs`

Independently compare complete sealed diff against the effective signed or trusted scope and reviewed instruction interpretation. Check allowed root via component containment, operation, mode, reviewed file type and each old and new pathname. Verify both sides of a move. Documentation-only mode admits regular Markdown creates and modifications within scope, subject to the repository's control-path rules. Missing grant or inaccessible instructions blocks verification. A passing verification receipt attests its checked scope and cannot authorize later effects by itself.

**ZIP-VERIFICATION-REPOSITORY-SCOPE-T01.** A move from an allowed source to a disallowed target fails. A generic grant cannot approve privileged configuration paths.
