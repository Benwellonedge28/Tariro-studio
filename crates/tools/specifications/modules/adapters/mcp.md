# MCP versioned adapter

**ZIP-TOOLS-ADAPTERS-MCP-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/adapters/mcp.rs`

## Boundary and inputs

Bind enrolled server identity, approved transport, negotiated protocol revision, tool descriptor digest and strict input/output schemas. Read bounded discovery pages under their own consent and deadline. Compare advertised capabilities and effect metadata against the locally approved registry before accepting a descriptor. [MCP tools specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)

## Behavior and failure handling

Send only normalized approved arguments and metadata, scoped to the enrolled server and current action. Treat descriptions, annotations, prompts and response text as untrusted. No output can initiate a follow-on call or expand a grant. A changed schema or lost scoped response requires qualified renegotiation or original-intent reconciliation before any repeat.

## Acceptance

**ZIP-TOOLS-ADAPTERS-MCP-T01.** Return synthetic text claiming permission for a second tool. Confirm zero follow-on calls. Change the enrolled tool schema server-side and verify the previous grant cannot authorize the new shape.
