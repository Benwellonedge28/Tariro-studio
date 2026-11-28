# Attribution identity

**ZIP-AUDIT-ACTOR-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/actor.rs`

## Boundary and inputs

Accept an attribution view from the authenticated composition boundary. Bind stable principal identifier, workspace, actor category and a safe provenance reference. Distinguish verified human, service and agent attribution from explicitly unattributed nonprivileged observations. A request-supplied name or role cannot supply identity.

## Behavior and failure handling

Require trustworthy attribution for privileged intent and result append. Keep role and delegation evidence as scoped references. An unauthenticated observation may be recorded only under an authorized event category that permits unknown attribution, with no fabricated principal. Omit sessions, tokens, signatures used for authentication and raw provider user records.

## Acceptance

**ZIP-AUDIT-ACTOR-T01.** Submit a forged owner label and a legitimately attributed test actor. The first cannot append a privileged intent. The second records the stable principal and safe provenance without exposing synthetic credentials.
