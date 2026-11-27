# Security design

Report vulnerabilities privately to the repository owner using a verified contact mechanism. Never post credentials or sensitive reproductions in a public issue. Use redacted incident identifiers until a private reporting channel is confirmed.

| Trust crossing | Required controls | Failure behavior |
| --- | --- | --- |
| Repository, model or tool output → gateway | Parse into data or typed proposal; verify grant independently | Reject authority inferred from content |
| Gateway → workspace | Scope by stable repository identity, root handle and normalized relative path | Deny links, escapes and races |
| Agent → terminal | Structured executable and arguments, isolated process tree, clean environment and deadline | Deny if required isolation unavailable |
| Node → external endpoint | Policy-approved purpose, host, resolved network, data classes and TLS identity | Default deny and stop on revalidation failure |
| App → credential store | Opaque references, short-lived minimum-scope credentials, adapter-only resolution | Block effect if keyring unavailable |
| Plugin/model/package → install | Verify digest, origin, signature where required, accepted dependency/license decision | Quarantine staged bytes |
| Remote client → daemon | Authenticated transport, principal and workspace binding, revocation check | Refuse expired or mismatched session |

Audit grant, revoke, effect intent, effect outcome, policy changes, export and suspend events. During an incident, pause writes; revoke scoped grants and credential references; record relevant hashes, timestamps and actors; secure evidence; reconcile uncertain external operations; rotate credentials through their owner; verify recovery before resuming.
