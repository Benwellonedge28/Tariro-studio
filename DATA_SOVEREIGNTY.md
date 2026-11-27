# Data sovereignty

| Class | Examples | Default handling |
| --- | --- | --- |
| Public | Explicitly public repository data | Store locally; transmit only through authorized operations |
| Workspace confidential | Source, plans, memory, evidence | Workspace-scoped; protected storage; no external inference by default |
| Restricted | Personally identifying data and sensitive logs | Minimize, redact and require explicit destination and purpose |
| Secret | Tokens, private keys, raw credential values | OS keyring; opaque references only outside approved adapters |

Use a default-deny egress rule for every data class. Each eligible transfer records approved destination, purpose, scope, classes and retention. Apply scope filtering before ranking or serialization. Zero plaintext credentials may enter a model or durable artifact. Encrypted backups exclude live credentials and include a versioned manifest of hashes and counts.

Export only under owner authority to a chosen destination. Restore into staging, verify hashes and schema, bind a new local identity when required, and activate after a dry-run check. Purge invalidates projections and indexes before returning an outcome. Explain retention limits of immutable audit events and backup history to the operator. External telemetry and cloud sync are opt-in independently.
