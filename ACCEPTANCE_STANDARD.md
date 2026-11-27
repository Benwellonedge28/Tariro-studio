# Component and release acceptance

**ZIP-ACC-001 · v1.0 · Owner:** Verification and release maintainers. **Maturity:** D4 candidate.

Separate design gate, implementation gate and release gate. Design requires complete component and file contracts, consistency checks and independent review. Implementation requires matching Safe Rust interfaces, tests and linkage to requirements. Release requires the implementation evidence plus platform qualification, signed artifacts, backup/restore, rollback and release authorization.

The verdict is failed if any mandatory gate fails, blocked if a mandatory gate is unresolved or lacks evidence, and passed only if all mandatory evidence covers the exact candidate. Optional gates report their status without satisfying mandatory ones. Passing local tests grants no merge or deployment capability.

Each gate records requirement IDs, fixture/environment, expected result, actual observation, verifier, reviewed digest and outcome. See [VERIFICATION.md](VERIFICATION.md) for the platform release gate catalog and [ROADMAP.md](ROADMAP.md) for sequencing.
