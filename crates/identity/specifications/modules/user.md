# Human account representation

**ZIP-IDENTITY-USER-001 · v1.1 · Owner:** Identity maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/identity/src/user.rs`

## Boundary and inputs

Represent a human user by typed principal identity and verified enrolled account binding. Keep user-editable display fields separate from authoritative role and membership records. Only the authorized account or administrator may update the applicable profile fields under expected revision.

## Behavior and failure handling

Validate field classes and disclosure preferences before atomically applying changes. Profile edits cannot change principal kind, workspace membership, roles, issuer binding or active credentials. Privileged changes require their own authenticated owner path and must preserve history. Treat concurrent conflicts as stale rather than silently merging into authority fields.

## Acceptance

**ZIP-IDENTITY-USER-T01.** Change display name to match a repository owner and verify no role, scope or principal ID changes. Race two display edits and confirm stale replacement does not cross the membership boundary.
