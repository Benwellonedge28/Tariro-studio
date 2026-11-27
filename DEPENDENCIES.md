# Dependency policy

Use stable Rust and a pinned toolchain, a committed dependency lockfile and declared feature sets. Start with Tokio, Serde, thiserror, Clap and redb for the minimal workspace. Admit domain-specific crates when their subsystem reaches implementation. Candidate choices in the master design are subject to package review.

For each dependency capture resolved version and source, checksum, enabled features, transitive exposure, license expression, platform matrix, vulnerabilities, maintenance ownership, unsafe or native code, build scripts and network requirements. Record acceptance or rejection in the consuming crate's implementation PR.

Use locked builds in CI. Review lockfile sources and diff; generate a CycloneDX SBOM, run advisory and policy checks against the resolved graph, and attach results to release evidence. Production profiles require review of critical findings and time-bounded exceptions. For offline build bundles, verify archive integrity before installation and ensure the package cache can satisfy a locked build without network.

Third-party services are adapters with explicit capability flags. GitHub is supported, local Git paths remain available. Optional inference services never become required for deterministic or local-only features.
