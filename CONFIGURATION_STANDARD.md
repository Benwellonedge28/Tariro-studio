# Centralized configuration standard

**ZIP-CFG-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D4 candidate.

Configuration manifests live under `configurations/schemas`, `defaults`, `profiles`, `resources`, `security`, `inference`, `scheduling`, `storage`, `networking`, `providers`, `governance`, `assignments` and `migrations`. Edition 1 uses versioned TOML input and a typed normalized snapshot. Profiles such as minimal, personal, workstation, server, enterprise and distributed are preferences for a class of deployment.

1. Resolve schema major/minor and reject duplicate or unrecognized keys at active boundaries.
2. Load typed defaults and selected profile, then permitted user preferences.
3. Apply mandatory constitution, system, organization, workspace and assignment restrictions by intersection. Exact restrictions must agree; effective allow sets intersect; maximums take the minimum; required sets form a union. Deny an empty or inconsistent policy domain.
4. Apply runtime optimization within the resulting grant. Runtime cannot expand policy, recreate missing credentials or infer egress permission.
5. Validate cross-field constraints and produce an immutable snapshot with per-key origin, policy revision and digest. Activate atomically or keep the prior valid snapshot. A mandatory revocation supersedes retained snapshots for future effects.

A key registry entry includes name, owner, schema type, unit, bound class, source, validation, required dependencies, reload impact and whether it can apply to in-flight work. Export only redacted snapshots and never store credential values in configuration. Treat unsupported major versions as unsupported and validate staged migrations before activation. Test invalid override, tight policy, reload failure, concurrent readers and rollback.
