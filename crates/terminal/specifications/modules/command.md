# Immutable execution request

**ZIP-TERMINAL-COMMAND-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/command.rs`

## Boundary and inputs

Define an immutable CommandSpec binding exact executable capability and digest, structured arguments, rooted working-directory identity, environment schema and opaque references, stream budgets, deadline basis, grant and correlation identity. Validate types and compatible units before acceptance. Include only approved digested data and credential references in review metadata.

## Behavior and failure handling

Bind the exact versioned semantics in the reviewed effect digest. A changed field relevant to execution requires new evidence and authority. Values carried in the request cannot open a shell, extend the admitted deadline or broaden path permissions. The request alone cannot create a live process.

## Acceptance

**ZIP-TERMINAL-COMMAND-T01.** Preview an authorized synthetic command, change only its arguments and try the original review digest. Reject before launch. Repeat with an unchanged binding and verify scope is still independently checked.
