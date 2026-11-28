# Explicit environment mapping

**ZIP-CONFIGURATION-ENVIRONMENT-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/environment.rs`

## Boundary and inputs

Read only variables in the trusted installation's allowlist. Each entry binds one exact name, one registry key and a typed parser. Validate the map before reading the environment. Two names mapping to one key, an unregistered key, or mappings to privilege, egress grants or secret values fail closed. Check each mapping's permitted source classes in the [registry](schema.md).

## Behavior and failure handling

Obtain one immutable snapshot of approved values from the injected reader. Missing variables contribute absence. Present values use the same registered type and range as other preferences, with an explicit text grammar recorded in the allowlist. For a supported Boolean accept exact lowercase true or false. For U64 accept canonical ASCII decimal with checked conversion and no surrounding whitespace. Enums match an exact declared tag. Exclude secret references and composite values from this mapping. Reject malformed or oversized mapped values under the layer byte budget. Use a deterministic key order. Ignore unrelated variables without logging names or enumerating them into the layer. A supplied preference cannot bypass [mandatory intersections](overrides.md).

## Acceptance

**ZIP-CONFIGURATION-ENVIRONMENT-T01.** Give the adapter an unapproved egress variable and a registered scalar preference. Only the scalar enters the layer. Test duplicate mappings, a malformed scalar and an over-budget value. Verify only the stable canonical key and source class are revealed.
