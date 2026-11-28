# Tool cancellation ownership

**ZIP-TOOLS-CANCELLATION-001 · v1.1 · Owner:** Tools maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/tools/src/cancellation.rs`

## Boundary and inputs

Accept a scoped authorized cancel bound to the original invocation attempt and current generation. Record the stop through the owning journal and signal the qualified adapter or supervising owner. A dropped observer releases only its wait. New effects stop at their live gate after cancellation.

## Behavior and failure handling

Retain verified outcomes accepted before cancellation. If dispatch may have occurred, classify the result unresolved until trusted reconciliation. Local adapters verify cleanup before releasing holds. Exact stop replay returns one accepted decision and cannot create another tool invocation.

## Acceptance

**ZIP-TOOLS-CANCELLATION-T01.** Cancel after an external synthetic commit but before delivery. Verify the existing receipt survives and duplicate dispatch remains barred. Cancel before claim and verify zero calls.
