# Maven build adapter

**ZIP-COMPILATION-ADAPTERS-MAVEN-001 · v1.0 · Owner:** Compilation maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/compilation/src/adapters/maven.rs`

## Required implementation behavior

Pin JVM and Maven, scope lifecycle goals and repositories, and record offline/dependency outcomes.

## Acceptance

**ZIP-COMPILATION-ADAPTERS-MAVEN-T01.** Offline missing JAR is typed dependency failure.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
