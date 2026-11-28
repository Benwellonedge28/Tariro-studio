# Bounded strict TOML decode

**ZIP-CONFIGURATION-PARSER-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/parser.rs`

## Boundary and inputs

Consume an injected byte reader, checked finite byte limit, allowed source descriptor and cancellation observation. Enforce the byte limit during reading using checked counts. Pre-size buffers only from admitted limits and known lengths. Reject excess before parsing. Validate exact UTF-8, then decode complete TOML and reject duplicate, dotted or explicit table aliases that resolve to duplicate semantic keys. No partial parsed tree is returned after invalid syntax.

## Behavior and failure handling

Preserve declared edition, typed raw scalar kind, normalized key paths and positions needed by the [schema registry](schema.md). Preserve the distinction between integer and float nodes even for integral magnitudes. Check registered limits against the required integer node type before any JSON-shaped validation. Resolve edition and registry names after parsing. Disclose only validated positions and authorized source class on failure. Do not read include files, interpolate environment or apply configuration effects during parse.

## Acceptance

**ZIP-CONFIGURATION-PARSER-T01.** Decode at the exact byte cap and deny the next byte. Test duplicate keys expressed through alternate TOML forms, invalid UTF-8, unclosed syntax, and integral-looking float in a duration slot. Confirm neither raw bytes nor secret text appear in diagnostics.
