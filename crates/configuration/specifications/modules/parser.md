# Bounded strict TOML decode

**ZIP-CONFIGURATION-PARSER-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/parser.rs`

## Required implementation behavior

parse_layer(reader: BoundedReader, origin: LayerOrigin) -> Result<RawLayer, ConfigError>. Charge raw bytes before decode; reject duplicate TOML keys, unknown key shapes, invalid UTF-8 and trailing malformed input. Preserve byte position with no raw value in errors.

## Acceptance

**ZIP-CONFIGURATION-PARSER-T01.** Try duplicate dotted keys, malformed UTF-8 and an oversized stream.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
