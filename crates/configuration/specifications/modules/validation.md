# Configuration validation and activation

**ZIP-CFG-VAL-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D4 candidate. **Planned source:** `crates/configuration/src/validation.rs`.

Expose `validate(candidate: TypedConfig, registry: &KeyRegistry, restrictions: &PolicyDomain) -> Result<ResolvedConfig, ConfigError>`. The owned candidate includes schema version, selected profiles, per-key typed values and origins. Return immutable effective values, bounds and a canonical redacted digest. Error carries a stable code, validated key identifier and source class. Never put raw layer bytes or secret values in the error.

Validate schema major and key existence before type/range. Validate profile overrides against the owner catalog, including units and positivity. Reject contradictory mutual exclusions, default page size exceeding max and incompatible policy intersections. Exact restrictions must agree. For derived keys require finite admission estimate and fresh qualified capability. Effective maxima cannot exceed any active policy ceiling. Form a new generation and atomically activate only once all fields pass.

Secrets are opaque identifiers; resolve them within adapters. Typed options missing required enforcement produce a disabled capability or fail the profile according to its requirement class. Existing snapshots remain immutable; revocation is checked separately before effects. See [configurations](../../../../configurations/README.md).

CFG-VAL-T01 tests unknown key, duplicate input, invalid unit and failed reload. T02 tests explicit zero versus absence and lower/upper policy intersections. T03 races readers against activation and verifies they see a complete generation. T04 proves two valid profiles use one binary.
