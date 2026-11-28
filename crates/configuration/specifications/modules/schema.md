# Registry and normalized types

**ZIP-CONFIGURATION-SCHEMA-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/schema.rs`

## Boundary and inputs

Own versioned key definitions and normalized data shape. KeySpec binds the dotted ID, owning component, type, unit, inclusive bounds where applicable, allowed source classes, merge rule, required edition and reload policy. The accepted kinds are Bool, U64, Enum, StringRef and Set. StringRef carries opaque validated reference identity. Resource bounds retain their declared unit. Definitions use the [key catalog](../../../../contracts/resources/budget-keys.json) and the selected family schema.

## Behavior and failure handling

Reject unsupported editions and duplicate definitions when constructing the registry. Match a declared key exactly before converting. A required key missing from a complete base defaults tree fails validation. Sparse layers express absence without substituting a value. Validate original TOML node kind before range checks. Canonicalize set order and represent known zero distinctly from missing values. TypedConfig owns normalized staged values. ResolvedConfig is immutable, containing effective values, per-key origins and configuration and policy digests. Keep secret payloads outside both.

## Acceptance

**ZIP-CONFIGURATION-SCHEMA-T01.** Check that negative and fractional values, integral-looking float nodes, repeated definitions and unknown keys cannot reach TypedConfig. Validate v1 and v2 through their exact schemas and verify the v2 runtime drain key cannot be omitted. Verify two equivalent set permutations yield equal normalized keys and values.
