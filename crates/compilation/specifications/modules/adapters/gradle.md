# Gradle build adapter

**ZIP-COMPILATION-ADAPTERS-GRADLE-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/gradle.rs`

## Required implementation behavior

Pin JVM, wrapper distribution identity and lock inputs; run bounded task without implicit download or daemon reuse outside policy.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-GRADLE-T01.** Missing approved wrapper cannot fetch automatically.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
