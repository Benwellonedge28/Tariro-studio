# Interoperability

| Interface | Binding | Compatibility gate |
| --- | --- | --- |
| In-process | Versioned Rust contracts | Consumer compilation and stable DTO fixtures |
| Local process | Authenticated IPC and request envelopes | OS user boundary, wrong-user denial and reconnect |
| Remote API | HTTPS `/api/v1` and SSE progress | Schema, audience, replay cursor, rate and limit fixtures |
| Worker | Authenticated RPC with fenced leases | Expiry, replay and stale result rejection |
| External tool | MCP adapter | Structured schema and capability mapping |
| Editor/debugger | LSP/DAP bridges | Feature negotiation and safe argument handling |
| Plugin | Versioned Wasm component interfaces | Imports, memory, fuel and compatibility matrix |

Negotiate supported majors, minor features, size limits and authorization semantics before capability use. Unknown fields in versioned responses may be skipped; unknown required request fields fail strict validation. Never reinterpret an unknown command as a known effect. ULABI is a future optional adapter and becomes advertised after conformance tests pass.
