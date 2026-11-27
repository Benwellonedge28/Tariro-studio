# Java source adapter

**ZIP-SOURCE-ANALYSIS-ADAPTERS-JAVA-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/adapters/java.rs`

## Required implementation behavior

Bind source level and classpath snapshot to qualified symbol resolution. Generated classes and reflection require observed evidence.

## Acceptance

**ZIP-SOURCE-ANALYSIS-ADAPTERS-JAVA-T01.** Missing classpath never fabricates a matching declaration.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
