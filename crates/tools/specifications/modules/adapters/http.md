# Scoped HTTP tool adapter

**ZIP-TOOLS-ADAPTERS-HTTP-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/adapters/http.rs`

## Boundary and inputs

Bind an approved method, destination, request and response schemas, credential scope, effective deadline and exact effect class. Use only an enrolled transport that can enforce current destination and data policy. Reserve bounded request and response bytes. A method name alone does not establish whether an operation is safe to replay.

## Behavior and failure handling

Disable automatic cross-origin forwarding. Treat a proposed redirect as a fresh destination and disclosure decision. Never forward prior origin credentials into a new origin. Mutations need a stable effect key and qualified reconciliation. A transport error or timeout does not establish absence. [RFC 9110, redirection](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.4)

## Acceptance

**ZIP-TOOLS-ADAPTERS-HTTP-T01.** Use two synthetic origins. Supply a cross-origin redirect to the unauthorized second origin and verify no second request or forwarded credential. Lose a permitted mutation response and retain the original unresolved intent.
