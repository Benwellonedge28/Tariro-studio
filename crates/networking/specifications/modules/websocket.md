# Scoped WebSocket stream

**ZIP-NETWORKING-WEBSOCKET-001 · v1.0 · Owner:** Networking maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/networking/src/websocket.rs`

## Required implementation behavior

Authorize handshake and verify negotiated subprotocol; bound frames, message buffers and reconnects. Revocation closes admission to new sends.

## Acceptance

**ZIP-NETWORKING-WEBSOCKET-T01.** Oversize message terminates or rejects according to approved policy without unbounded growth.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
