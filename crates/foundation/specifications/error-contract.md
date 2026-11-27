# Foundation error contract

**Maturity:** D4 candidate.

The [error module](modules/error.md) owns codes for Foundation operations. Identity parsing discriminates malformed from nil. Digest parsing distinguishes framing from unsupported algorithms. Bounds check checked arithmetic first, then compare against the inclusive limit. Cancellation waiter registration checks cancellation and capacity before allocation or sequence advancement.

Core errors carry no user content. Adapters add redacted trace context and public status mapping. A Foundation error has no automatic retry contract. Repeats must resolve the actual invalid input, exhaustion, or failed synchronization first. Additions are compatible only when caller mapping and old wire consumers tolerate an unknown failure code.
