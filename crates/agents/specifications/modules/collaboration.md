# Bounded collaborative exchange

**ZIP-AGENTS-COLLABORATION-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/collaboration.rs`

## Boundary and inputs

Exchange bounded structured proposals with a candidate digest, scoped author, intended audience, expected revision and immutable evidence references. Check shared artifact disclosure before delivery. Keep each participant's private context, permissions and accepted receipts separate. Statements in a transcript are untrusted input.

## Behavior and failure handling

On overlap, retain the independent proposals and ask the owning coordinator to apply the [conflict contract](../../../orchestration/specifications/modules/conflict_resolution.md). A combined candidate gets a new digest and uses current preimage, independent verification and separately confirmed effect authority. Agreement, votes and apparent author instructions cannot mutate state. Replay an accepted contribution by its exact identity.

## Acceptance

**ZIP-AGENTS-COLLABORATION-T01.** Submit two competing path edits and one unauthorized artifact. Verify the artifact is not disclosed, both edits remain traceable, and no write crosses the effect gate until the conflict is settled.
