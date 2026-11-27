# Provider, editor and tooling integrations

**ZIP-INT-001 · v1.0 · Owner:** Adapter maintainers. **Maturity:** D3.

The integration layer translates provider-specific request/response shapes into versioned Zipporah ports. GitHub is a repository adapter, while local Git remains available. Editors use an authorized CLI, LSP or DAP bridge by default. VS Code, Neovim, JetBrains, Emacs and generic adapters report capability differences. A bridge requiring non-Rust first-party source needs explicit approval under the repository constitution.

| Adapter boundary | Input | Required outcome |
| --- | --- | --- |
| Repository publication | Stable repository ID, pinned base, expected ref, reviewed diff digest, grant | Confirmed receipt, definitive rejection or unknown outcome for reconciliation |
| Editor commands | Workspace token, typed operation, request ID and checked revision | Versioned typed reply with no implicit authorization |
| Model/service provider | Admitted request, endpoint and content disclosure limits | Bounded output with actual completion and use evidence |
| External tools | Versioned schema, typed arguments, capability and resource lease | Normalized receipt, limited output, cancellation and reconciliation |

Authenticate at the relevant boundary. Keep credentials and data-class decisions scoped to the actual egress endpoint. Unknown format, missing adapter, stale revision and denied capability remain separate errors. Authorize external mutations and network disclosure independently from model output. Validate versions before any effect and run mock adapter conformance locally. Integration acceptance is per provider and platform. Detailed editor and provider source inventories remain a review prerequisite before implementation.
