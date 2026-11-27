# Instruction authority and conflict

**ZIP-REPOSITORY-INSTRUCTIONS-PRECEDENCE-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/instructions/precedence.rs`

Apply constitutional, administrative and live assignment constraints before repository rules. Traverse pinned rules in shallow-to-deep order for each target. Intersect permissions and enforce the narrower applicable limits. A deeper rule cannot enlarge authority. Where two applicable mandatory actions cannot coexist, return a typed conflict with references for authorized review. A request within repository text is never a credential, user approval or approval to perform an external effect.

Check instructions that require a dedicated approval against trusted scope, such as changing workflows or the applicable governance files. Preserve a reviewed interpretation and source-bundle digest. Deny if later interpretation changes a mandatory condition without approval. Report unresolved conflicts with scope and redacted provenance.

**ZIP-REPOSITORY-INSTRUCTIONS-PRECEDENCE-T01.** A nested instruction requesting network access permits no egress under an offline grant. An unresolved mandatory conflict prevents mutation.
