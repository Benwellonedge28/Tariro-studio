### Zipporah — Universal Agentic Engineering Infrastructure

Comprehensive System Architecture and Engineering Design Specification

| Property                        | Specification                                           |
| ------------------------------- | ------------------------------------------------------- |
| Project                         | Zipporah                                                |
| Flagship application            | Zipporah Studio                                         |
| Previous identity               | Tariro Studio                                           |
| Proposed repository             | Benwellonedge28/Zipporah                                |
| Specification version           | 1.0.0                                                   |
| Implementation language         | Safe Rust                                               |
| Architecture                    | Modular, local-first, distributed-capable               |
| Deployment                      | Native, embedded, self-hosted and optional cloud        |
| Initial hardware target         | 16 GB RAM, 900 GB SSD                                   |
| Primary market                  | Global                                                  |
| Target audience                 | Individuals, developers, organizations and institutions |
| Development philosophy          | Independent, secure, extensible and verifiable          |
| External repository integration | GitHub and other Git providers                          |
| Status                          | Proposed architecture                                   |
| Tagline                         | Build without boundaries                                |

### Part I — Strategic foundation

### 1\. Executive summary

Zipporah is a universal agentic software engineering infrastructure designed to manage the complete software development lifecycle through coordinated human, artificial and deterministic intelligence.

Unlike conventional AI coding assistants, Zipporah shall operate as a persistent engineering environment capable of understanding entire repositories, executing complex assignments, managing computational resources, coordinating specialized agents, verifying engineering outputs and maintaining software systems over extended periods.

Zipporah shall support local and remote AI inference without compulsory dependence on any particular AI provider, inference engine, programming language, operating system, repository provider or cloud platform.

It shall operate on ordinary personal computers while providing an architectural path toward workstations, private servers and distributed computing infrastructure.

Its first practical objective shall be accelerating the development of Vimbai through persistent, verified software engineering assignments.

### 2\. Strategic objectives

| ID      | Objective                                                 |
| ------- | --------------------------------------------------------- |
| OBJ-001 | Establish independent software engineering infrastructure |
| OBJ-002 | Reduce dependence on paid AI services                     |
| OBJ-003 | Support complete software development lifecycles          |
| OBJ-004 | Provide local and offline-first operation                 |
| OBJ-005 | Support arbitrary programming languages                   |
| OBJ-006 | Understand existing and future repositories               |
| OBJ-007 | Provide persistent autonomous engineering                 |
| OBJ-008 | Enforce human authorization and governance                |
| OBJ-009 | Adapt execution to available hardware                     |
| OBJ-010 | Support interchangeable AI models and providers           |
| OBJ-011 | Prevent fabricated engineering results                    |
| OBJ-012 | Provide reproducible and auditable execution              |
| OBJ-013 | Support distributed engineering infrastructure            |
| OBJ-014 | Enable controlled self-improvement                        |
| OBJ-015 | Preserve user ownership of data and intellectual property |
| OBJ-016 | Support generations of technological evolution            |

### 3\. Architectural constitution

The following requirements shall govern every Zipporah subsystem.

| Principle         | Mandatory requirement                                     |
| ----------------- | --------------------------------------------------------- |
| Memory safety     | First-party implementation shall use Safe Rust            |
| Sovereignty       | Users retain ownership and control of their environments  |
| Independence      | No compulsory external service                            |
| Privacy           | No unauthorized data transmission                         |
| Modularity        | Components communicate through documented contracts       |
| Extensibility     | New capabilities must not require foundational redesign   |
| Persistence       | Verified progress survives process interruptions          |
| Verification      | Completion claims require supporting evidence             |
| Authorization     | Every privileged operation requires appropriate authority |
| Resource safety   | All expensive operations must have enforceable limits     |
| Neutrality        | No hardcoded model, hardware or repository provider       |
| Transparency      | Decisions and operations must be inspectable              |
| Compatibility     | Public interfaces require explicit versioning             |
| Recoverability    | Failed operations must support safe recovery              |
| Offline operation | Core local capabilities work without internet access      |

Safe Rust requirements shall apply to all first-party implementation. Third-party dependencies containing unsafe Rust or native code must be explicitly audited and governed. Safe Rust alone does not guarantee complete system security.

### Part II — System architecture

### 4\. High-level architecture

### ZIPPORAH

Universal Agentic Engineering Infrastructure

Studio

CLI

Mobile

Server

SDK

Editor integrations

Application and assignment gateway

Identity · Sessions · Commands · Authorization

Agent runtime

Workflow engine

Engineering engine

Intelligence engine

Repository engine

Verification engine

Knowledge engine

Resource engine

Cross-cutting governance and security

Policy · Sandbox · Permissions · Audit · Evidence

Persistent storage

Native inference

Tool execution

Networking

Provider adapters

Distributed execution

Hardware and operating system abstraction

CPU · GPU · NPU · RAM · Storage · Network

### 5\. Architectural layers

| Layer               | Responsibility                                       |
| ------------------- | ---------------------------------------------------- |
| L0 — Hardware       | Physical and virtual computational resources         |
| L1 — Foundation     | Types, identifiers, errors and configuration         |
| L2 — Infrastructure | Storage, networking and operating system integration |
| L3 — Runtime        | Scheduling, execution and resource management        |
| L4 — Intelligence   | Models, inference, reasoning and context             |
| L5 — Agents         | Agent lifecycle and coordination                     |
| L6 — Engineering    | Software engineering capabilities                    |
| L7 — Verification   | Testing, validation and evidence                     |
| L8 — Applications   | CLI, desktop, server and mobile interfaces           |
| Cross-cutting       | Security, governance, audit and observability        |

Dependencies shall point toward foundational layers. Higher-level capabilities shall be exposed through interfaces rather than reverse dependencies.

### 6\. Supported operating modes

| Mode        | Description                                            |
| ----------- | ------------------------------------------------------ |
| Standalone  | Entire environment on one computer                     |
| Offline     | Local inference and local engineering without internet |
| Online      | Local execution with authorized online integrations    |
| Hybrid      | Local and remote intelligence                          |
| Headless    | Background execution without graphical interface       |
| Remote      | Phone or another computer controls a Zipporah node     |
| Distributed | Multiple authorized machines share workloads           |
| Embedded    | Zipporah integrated into another application           |
| Enterprise  | Multiple users, projects and governed workspaces       |
| Air-gapped  | No external network access                             |
| Research    | Controlled experimentation with models and workflows   |

### Part III — Complete repository structure

### 7\. Root directory

The following is the proposed long-term repository structure. Directories shall be introduced progressively with corresponding specifications and functional implementations, rather than creating hundreds of empty placeholder files.

```text
Zipporah/
├── .cargo/
│   └── config.toml
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── CODEOWNERS
│   └── dependabot.yml
├── applications/
├── crates/
├── extensions/
├── integrations/
├── specifications/
├── documentation/
├── configurations/
├── policies/
├── workflows/
├── schemas/
├── protocols/
├── models/
├── migrations/
├── resources/
├── examples/
├── benchmarks/
├── tests/
├── fuzz/
├── tooling/
├── packaging/
├── deployment/
├── research/
├── Cargo.toml
├── Cargo.lock
├── rust-toolchain.toml
├── rustfmt.toml
├── clippy.toml
├── deny.toml
├── AGENTS.md
├── README.md
├── OBJECTIVES.md
├── CONSTITUTION.md
├── ARCHITECTURE.md
├── REQUIREMENTS.md
├── SECURITY.md
├── GOVERNANCE.md
├── DEPENDENCIES.md
├── INTEROPERABILITY.md
├── DATA_SOVEREIGNTY.md
├── RESOURCE_MANAGEMENT.md
├── VERIFICATION.md
├── MIGRATION.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE
```

### 8\. Rust workspace

```text
crates/
├── foundation/
├── configuration/
├── identity/
├── storage/
├── events/
├── runtime/
├── resources/
├── scheduler/
├── intelligence/
├── inference/
├── models/
├── context/
├── reasoning/
├── memory/
├── knowledge/
├── search/
├── agents/
├── orchestration/
├── assignments/
├── workflows/
├── repository/
├── source-analysis/
├── engineering/
├── documentation/
├── compilation/
├── testing/
├── debugging/
├── verification/
├── research/
├── tools/
├── terminal/
├── filesystem/
├── sandbox/
├── security/
├── governance/
├── audit/
├── networking/
├── synchronization/
├── distributed/
├── providers/
├── interoperability/
├── plugins/
├── observability/
├── economics/
├── deployment/
├── maintenance/
├── evolution/
└── sdk/
```

Each major crate shall follow a consistent structure:

```text
crate-name/
├── Cargo.toml
├── AGENTS.md
├── README.md
├── DESIGN.md
├── src/
│   ├── lib.rs
│   ├── error.rs
│   ├── types.rs
│   └── ...
├── tests/
├── benches/
└── examples/
```

The structures below define the intended internal modules. They do not imply that every crate must be implemented before the first release.

### 9\. Foundation crate

Provides shared contracts without depending on higher-level subsystems.

```text
crates/foundation/src/
├── lib.rs
├── error.rs
├── result.rs
├── identity/
│   ├── mod.rs
│   ├── identifier.rs
│   ├── namespace.rs
│   └── generation.rs
├── types/
│   ├── mod.rs
│   ├── timestamp.rs
│   ├── duration.rs
│   ├── version.rs
│   ├── digest.rs
│   ├── quantity.rs
│   └── bounded.rs
├── contracts/
│   ├── mod.rs
│   ├── component.rs
│   ├── capability.rs
│   ├── lifecycle.rs
│   └── compatibility.rs
├── validation/
│   ├── mod.rs
│   ├── constraints.rs
│   └── invariant.rs
├── cancellation.rs
├── limits.rs
├── provenance.rs
└── prelude.rs
```

Responsibilities include stable identifiers, structured errors, cancellation contracts, versioning, bounded quantities and common validation.

### 10\. Configuration crate

```text
crates/configuration/src/
├── lib.rs
├── error.rs
├── schema.rs
├── loader.rs
├── parser.rs
├── defaults.rs
├── environment.rs
├── overrides.rs
├── validation.rs
├── migration.rs
├── profiles/
│   ├── mod.rs
│   ├── minimal.rs
│   ├── lightweight.rs
│   ├── standard.rs
│   ├── workstation.rs
│   ├── server.rs
│   └── distributed.rs
├── user.rs
├── project.rs
├── organization.rs
├── security.rs
├── inference.rs
└── resources.rs
```

Configuration precedence shall be deterministic. User and project configuration must not override mandatory security policies.

### 11\. Identity crate

```text
crates/identity/src/
├── lib.rs
├── error.rs
├── principal.rs
├── user.rs
├── agent.rs
├── service.rs
├── device.rs
├── organization.rs
├── workspace.rs
├── session.rs
├── authentication.rs
├── credentials.rs
├── federation.rs
├── delegation.rs
├── revocation.rs
└── registry.rs
```

Every operation shall be attributable to an authenticated human, agent, service or device identity.

### 12\. Storage crate

```text
crates/storage/src/
├── lib.rs
├── error.rs
├── backend.rs
├── transaction.rs
├── repository.rs
├── schema.rs
├── migration.rs
├── integrity.rs
├── encryption.rs
├── retention.rs
├── backends/
│   ├── mod.rs
│   ├── memory.rs
│   ├── redb.rs
│   ├── sqlite.rs
│   ├── filesystem.rs
│   └── remote.rs
├── objects/
│   ├── mod.rs
│   ├── content_addressed.rs
│   ├── blobs.rs
│   └── metadata.rs
├── backup/
│   ├── mod.rs
│   ├── snapshot.rs
│   ├── restore.rs
│   └── verification.rs
└── recovery/
    ├── mod.rs
    ├── journal.rs
    └── reconciliation.rs
```

Storage shall remain backend-neutral. The initial implementation should use one primary embedded database rather than requiring multiple database servers.

### 13\. Events crate

```text
crates/events/src/
├── lib.rs
├── error.rs
├── event.rs
├── envelope.rs
├── topic.rs
├── publisher.rs
├── subscriber.rs
├── dispatcher.rs
├── queue.rs
├── journal.rs
├── ordering.rs
├── replay.rs
├── deduplication.rs
├── backpressure.rs
├── dead_letter.rs
└── retention.rs
```

Provides bounded event delivery, durable event recording where required and recovery through replay.

### Part IV — Execution infrastructure

### 14\. Runtime crate

```text
crates/runtime/src/
├── lib.rs
├── error.rs
├── runtime.rs
├── builder.rs
├── lifecycle.rs
├── supervisor.rs
├── execution/
│   ├── mod.rs
│   ├── executor.rs
│   ├── worker.rs
│   ├── worker_pool.rs
│   ├── task.rs
│   ├── task_handle.rs
│   └── execution_context.rs
├── control/
│   ├── mod.rs
│   ├── cancellation.rs
│   ├── timeout.rs
│   ├── pause.rs
│   └── shutdown.rs
├── checkpoint/
│   ├── mod.rs
│   ├── checkpoint.rs
│   ├── store.rs
│   └── restore.rs
├── recovery/
│   ├── mod.rs
│   ├── retry.rs
│   ├── crash_recovery.rs
│   └── reconciliation.rs
├── isolation.rs
├── health.rs
└── metrics.rs
```

The runtime shall supervise tasks, prevent orphaned execution, persist recoverable state and support graceful shutdown.

### 15\. Resource management crate

```text
crates/resources/src/
├── lib.rs
├── error.rs
├── discovery/
│   ├── mod.rs
│   ├── cpu.rs
│   ├── gpu.rs
│   ├── npu.rs
│   ├── memory.rs
│   ├── storage.rs
│   └── network.rs
├── allocation/
│   ├── mod.rs
│   ├── allocator.rs
│   ├── reservation.rs
│   ├── quota.rs
│   └── lease.rs
├── monitoring/
│   ├── mod.rs
│   ├── utilization.rs
│   ├── thermal.rs
│   ├── battery.rs
│   └── pressure.rs
├── optimization/
│   ├── mod.rs
│   ├── adaptive.rs
│   ├── offloading.rs
│   └── eviction.rs
├── profiles.rs
├── admission.rs
├── estimation.rs
└── limits.rs
```

Zipporah must inspect available resources before accepting expensive assignments.

### 16\. Scheduler crate

```text
crates/scheduler/src/
├── lib.rs
├── error.rs
├── scheduler.rs
├── job.rs
├── queue.rs
├── priority.rs
├── dependency.rs
├── deadline.rs
├── fairness.rs
├── admission.rs
├── placement.rs
├── preemption.rs
├── retry.rs
├── backpressure.rs
├── policies/
│   ├── mod.rs
│   ├── sequential.rs
│   ├── parallel.rs
│   ├── priority.rs
│   ├── resource_aware.rs
│   └── distributed.rs
└── persistence.rs
```

Scheduling decisions must respect task dependencies, resource limits, authorization and cancellation.

### 17\. Hardware adaptation

| Profile      | RAM      | Recommended execution                   |
| ------------ | -------- | --------------------------------------- |
| Minimal      | 4 GB     | Remote inference or deterministic tasks |
| Lightweight  | 8 GB     | Small quantized models                  |
| Personal     | 16 GB    | One local model, sequential agents      |
| Standard     | 32 GB    | Larger models, controlled concurrency   |
| Workstation  | 64 GB    | Advanced local inference                |
| Professional | 128 GB+  | Multiple model workloads                |
| Distributed  | Variable | Resource-aware workload placement       |

### Initial 16 GB memory profile

### Illustrative memory allocation

### 16 GB RAM

Operating system and editor

4 GB

Quantized model weights

6 GB

Inference context and working buffers

2 GB

Zipporah runtime and indexes

1 GB

Compilation and safety reserve

3 GB

These are provisional budgets, not benchmark results. Actual model memory depends on architecture, quantization, context length and inference backend. Zipporah shall reduce concurrency or unload models when memory pressure becomes excessive.

### Part V — Artificial intelligence infrastructure

### 18\. Intelligence crate

```text
crates/intelligence/src/
├── lib.rs
├── error.rs
├── intelligence.rs
├── request.rs
├── response.rs
├── capability.rs
├── modality.rs
├── router.rs
├── selection.rs
├── fallback.rs
├── evaluation.rs
├── confidence.rs
├── structured_output.rs
├── tool_calling.rs
├── streaming.rs
├── usage.rs
├── budget.rs
├── caching.rs
└── providers/
    ├── mod.rs
    ├── local.rs
    ├── remote.rs
    ├── embedded.rs
    └── distributed.rs
```

Intelligence shall be accessed through a common interface. No agent shall directly depend on a particular commercial AI provider.

### 19\. Native inference crate

```text
crates/inference/src/
├── lib.rs
├── error.rs
├── engine.rs
├── session.rs
├── request.rs
├── response.rs
├── generation.rs
├── sampling.rs
├── streaming.rs
├── batching.rs
├── cancellation.rs
├── capabilities.rs
├── backends/
│   ├── mod.rs
│   ├── candle.rs
│   ├── mistral.rs
│   ├── ollama.rs
│   ├── llama_cpp.rs
│   ├── remote.rs
│   └── native.rs
├── hardware/
│   ├── mod.rs
│   ├── cpu.rs
│   ├── gpu.rs
│   ├── npu.rs
│   └── distributed.rs
├── memory/
│   ├── mod.rs
│   ├── allocation.rs
│   ├── kv_cache.rs
│   ├── model_cache.rs
│   └── eviction.rs
├── quantization/
│   ├── mod.rs
│   ├── formats.rs
│   ├── compatibility.rs
│   └── estimation.rs
└── metrics.rs
```

### Inference strategy

Zipporah shall initially integrate established inference engines behind interchangeable adapters. A proprietary native inference engine is a future capability, not a prerequisite for the first release.

Supported capabilities should progressively include text generation, embeddings, structured output, vision, speech, reranking, batching, context caching and distributed inference.

### 20\. Model management crate

```text
crates/models/src/
├── lib.rs
├── error.rs
├── model.rs
├── identifier.rs
├── manifest.rs
├── registry.rs
├── discovery.rs
├── download.rs
├── import.rs
├── export.rs
├── integrity.rs
├── signature.rs
├── licensing.rs
├── compatibility.rs
├── capabilities.rs
├── loader.rs
├── unloading.rs
├── cache.rs
├── lifecycle.rs
├── formats/
│   ├── mod.rs
│   ├── gguf.rs
│   ├── safetensors.rs
│   ├── onnx.rs
│   └── manifest.rs
├── tokenization/
│   ├── mod.rs
│   ├── tokenizer.rs
│   ├── vocabulary.rs
│   └── chat_template.rs
└── evaluation/
    ├── mod.rs
    ├── benchmark.rs
    ├── quality.rs
    └── performance.rs
```

Model downloads must be resumable, integrity-checked, license-aware and subject to storage limits.

### 21\. Context engineering crate

```text
crates/context/src/
├── lib.rs
├── error.rs
├── context.rs
├── builder.rs
├── window.rs
├── token_budget.rs
├── prioritization.rs
├── relevance.rs
├── compression.rs
├── summarization.rs
├── truncation.rs
├── retrieval.rs
├── deduplication.rs
├── provenance.rs
├── prompt.rs
├── template.rs
├── isolation.rs
└── cache.rs
```

Context assembly shall prioritize applicable repository instructions, assignment requirements, relevant source files, architectural decisions and verified evidence.

Retrieved content shall be treated as untrusted data, not privileged instructions.

### 22\. Reasoning crate

```text
crates/reasoning/src/
├── lib.rs
├── error.rs
├── problem.rs
├── decomposition.rs
├── planning.rs
├── constraints.rs
├── decision.rs
├── alternatives.rs
├── evaluation.rs
├── uncertainty.rs
├── reflection.rs
├── critique.rs
├── symbolic/
│   ├── mod.rs
│   ├── rules.rs
│   ├── logic.rs
│   └── solver.rs
├── hybrid/
│   ├── mod.rs
│   ├── deterministic.rs
│   └── model_assisted.rs
└── evidence.rs
```

Reasoning outputs shall expose actionable decisions, assumptions and evidence. Internal model reasoning shall not be treated as proof of correctness.

### Part VI — Persistent intelligence

### 23\. Memory crate

```text
crates/memory/src/
├── lib.rs
├── error.rs
├── memory.rs
├── record.rs
├── scope.rs
├── store.rs
├── retrieval.rs
├── consolidation.rs
├── compression.rs
├── deduplication.rs
├── expiration.rs
├── forgetting.rs
├── encryption.rs
├── provenance.rs
├── isolation.rs
├── layers/
│   ├── mod.rs
│   ├── working.rs
│   ├── session.rs
│   ├── episodic.rs
│   ├── semantic.rs
│   ├── procedural.rs
│   ├── project.rs
│   ├── repository.rs
│   ├── organization.rs
│   └── archival.rs
└── synchronization.rs
```

Memory shall be explicitly scoped. Information from one repository or organization must not automatically become accessible to another.

### 24\. Knowledge crate

```text
crates/knowledge/src/
├── lib.rs
├── error.rs
├── entity.rs
├── relationship.rs
├── graph.rs
├── ontology.rs
├── schema.rs
├── extraction.rs
├── ingestion.rs
├── validation.rs
├── inference.rs
├── query.rs
├── traversal.rs
├── provenance.rs
├── versioning.rs
├── conflict.rs
├── domains/
│   ├── mod.rs
│   ├── software.rs
│   ├── architecture.rs
│   ├── dependencies.rs
│   ├── documentation.rs
│   └── organizational.rs
└── persistence.rs
```

The knowledge graph shall represent software entities, relationships, dependencies, decisions and supporting sources.

### 25\. Search crate

```text
crates/search/src/
├── lib.rs
├── error.rs
├── query.rs
├── index.rs
├── document.rs
├── ingestion.rs
├── lexical/
│   ├── mod.rs
│   ├── tokenizer.rs
│   ├── inverted_index.rs
│   └── ranking.rs
├── semantic/
│   ├── mod.rs
│   ├── embeddings.rs
│   ├── vector.rs
│   ├── similarity.rs
│   └── index.rs
├── hybrid/
│   ├── mod.rs
│   ├── fusion.rs
│   └── reranking.rs
├── code_search.rs
├── filters.rs
├── incremental.rs
└── persistence.rs
```

Search shall support exact text, lexical ranking, semantic similarity, symbol search and hybrid retrieval.

### Part VII — Agentic engineering infrastructure

### 26\. Agent runtime crate

```text
crates/agents/src/
├── lib.rs
├── error.rs
├── agent.rs
├── identity.rs
├── manifest.rs
├── capabilities.rs
├── lifecycle.rs
├── state.rs
├── context.rs
├── execution.rs
├── communication.rs
├── mailbox.rs
├── registry.rs
├── factory.rs
├── supervision.rs
├── delegation.rs
├── collaboration.rs
├── evaluation.rs
├── permissions.rs
├── limits.rs
├── roles/
│   ├── mod.rs
│   ├── coordinator.rs
│   ├── researcher.rs
│   ├── architect.rs
│   ├── planner.rs
│   ├── documentation.rs
│   ├── developer.rs
│   ├── reviewer.rs
│   ├── tester.rs
│   ├── debugger.rs
│   ├── security.rs
│   ├── database.rs
│   ├── performance.rs
│   ├── devops.rs
│   ├── release.rs
│   ├── compliance.rs
│   ├── maintenance.rs
│   ├── repository.rs
│   └── auditor.rs
└── metrics.rs
```

Agent roles are logical identities. Multiple agents may share one inference model while retaining separate permissions, context and execution state.

### 27\. Orchestration crate

```text
crates/orchestration/src/
├── lib.rs
├── error.rs
├── orchestrator.rs
├── coordination.rs
├── team.rs
├── swarm.rs
├── delegation.rs
├── routing.rs
├── negotiation.rs
├── conflict_resolution.rs
├── consensus.rs
├── voting.rs
├── escalation.rs
├── execution_graph.rs
├── dependency_graph.rs
├── strategies/
│   ├── mod.rs
│   ├── sequential.rs
│   ├── parallel.rs
│   ├── hierarchical.rs
│   ├── collaborative.rs
│   ├── debate.rs
│   ├── independent_review.rs
│   └── adaptive.rs
└── supervision.rs
```

Consensus among AI agents shall not substitute for testing, authorization or independently verifiable evidence.

### 28\. Assignment management crate

```text
crates/assignments/src/
├── lib.rs
├── error.rs
├── assignment.rs
├── identifier.rs
├── specification.rs
├── requirements.rs
├── scope.rs
├── authorization.rs
├── plan.rs
├── task.rs
├── subtask.rs
├── dependency.rs
├── milestone.rs
├── progress.rs
├── state.rs
├── transitions.rs
├── persistence.rs
├── checkpoint.rs
├── recovery.rs
├── cancellation.rs
├── pause.rs
├── resume.rs
├── batching.rs
├── acceptance.rs
├── evidence.rs
├── result.rs
└── reporting.rs
```

### Assignment lifecycle

Submitted

Validated

Authorized

Planned

Scheduled

Executing

Verifying

Completed

Additional states

Paused

Blocked

Failed

Cancelled

Awaiting approval

Recovering

Every transition shall be validated and durably recorded. An assignment must never transition to completed solely because an AI agent claims success.

### 29\. Workflow engine

```text
crates/workflows/src/
├── lib.rs
├── error.rs
├── workflow.rs
├── definition.rs
├── parser.rs
├── compiler.rs
├── validation.rs
├── stage.rs
├── step.rs
├── condition.rs
├── dependency.rs
├── execution.rs
├── branching.rs
├── looping.rs
├── parallelism.rs
├── variables.rs
├── artifacts.rs
├── approval.rs
├── checkpoint.rs
├── retry.rs
├── compensation.rs
├── rollback.rs
├── versioning.rs
├── registry.rs
└── reporting.rs
```

Workflow execution shall support sequential, parallel, conditional, hierarchical and event-driven pipelines.

### Example assignment definition

```toml
[assignment]
name = "Vimbai design documentation"
repository = "Benwellonedge28/Vimbai"
mode = "documentation-only"
persistent = true

[instructions]
discover_agents_md = true
respect_nested_instructions = true
inspect_existing_designs = true

[scope]
allowed_extensions = ["md"]
implementation_changes = false
delete_files = false

[execution]
strategy = "sequential"
checkpoint_per_file = true
maximum_concurrent_agents = 1

[batching]
files_per_pull_request = 30
exact_batch_size = true
incomplete_final_batch = "await-approval"

[verification]
require_independent_review = true
require_source_references = true
require_integration_details = true
reject_placeholder_content = true
validate_repository_diff = true

[git]
create_branch = true
create_pull_request = true
automatic_merge = false

[security]
require_scoped_authorization = true
allow_credential_disclosure = false
```

This is an illustrative proposed configuration format. Its schema must be formally specified before implementation.

### Part VIII — Repository intelligence

### 30\. Repository crate

```text
crates/repository/src/
├── lib.rs
├── error.rs
├── repository.rs
├── discovery.rs
├── workspace.rs
├── manifest.rs
├── snapshot.rs
├── indexing.rs
├── instructions/
│   ├── mod.rs
│   ├── discovery.rs
│   ├── agents_md.rs
│   ├── hierarchy.rs
│   ├── precedence.rs
│   └── validation.rs
├── git/
│   ├── mod.rs
│   ├── clone.rs
│   ├── fetch.rs
│   ├── branch.rs
│   ├── worktree.rs
│   ├── commit.rs
│   ├── diff.rs
│   ├── merge.rs
│   ├── rebase.rs
│   ├── history.rs
│   ├── remote.rs
│   ├── tag.rs
│   └── conflict.rs
├── providers/
│   ├── mod.rs
│   ├── github.rs
│   ├── gitlab.rs
│   ├── bitbucket.rs
│   ├── forgejo.rs
│   ├── gitea.rs
│   └── local.rs
├── pull_requests/
│   ├── mod.rs
│   ├── creation.rs
│   ├── review.rs
│   ├── checks.rs
│   ├── status.rs
│   └── reconciliation.rs
├── analysis/
│   ├── mod.rs
│   ├── structure.rs
│   ├── dependencies.rs
│   ├── architecture.rs
│   ├── coverage.rs
│   ├── technical_debt.rs
│   └── placeholders.rs
└── synchronization.rs
```

GitHub shall remain a first-class integration. Zipporah shall not require users to migrate their repositories to a proprietary hosting platform.

### Repository operation requirements

| Operation        | Required control                       |
| ---------------- | -------------------------------------- |
| Read repository  | Repository access                      |
| Clone repository | Authorized storage and network access  |
| Modify file      | Assignment scope and write permission  |
| Delete file      | Explicit deletion permission           |
| Create branch    | Authorized repository scope            |
| Commit changes   | Verified diff and author identity      |
| Push branch      | Remote write authorization             |
| Create PR        | Batch and scope verification           |
| Merge PR         | Separate merge authority               |
| Force push       | Exceptional explicit authorization     |
| Change CI policy | Privileged configuration authorization |

### 31\. Source analysis crate

```text
crates/source-analysis/src/
├── lib.rs
├── error.rs
├── language.rs
├── detection.rs
├── parser.rs
├── syntax_tree.rs
├── symbol.rs
├── symbol_table.rs
├── reference.rs
├── call_graph.rs
├── dependency_graph.rs
├── control_flow.rs
├── data_flow.rs
├── type_information.rs
├── semantic.rs
├── diagnostics.rs
├── indexing.rs
├── impact_analysis.rs
├── complexity.rs
├── adapters/
│   ├── mod.rs
│   ├── tree_sitter.rs
│   ├── lsp.rs
│   ├── rust.rs
│   ├── python.rs
│   ├── javascript.rs
│   ├── typescript.rs
│   ├── java.rs
│   ├── c.rs
│   ├── cpp.rs
│   ├── go.rs
│   ├── zamani.rs
│   └── generic.rs
└── incremental.rs
```

Language-specific capabilities shall be advertised through a registry. Unsupported languages shall fall back to text-based analysis with explicit limitations.

### Part IX — Software engineering capabilities

### 32\. Engineering crate

```text
crates/engineering/src/
├── lib.rs
├── error.rs
├── requirements/
│   ├── mod.rs
│   ├── extraction.rs
│   ├── specification.rs
│   ├── traceability.rs
│   └── validation.rs
├── architecture/
│   ├── mod.rs
│   ├── system.rs
│   ├── component.rs
│   ├── interfaces.rs
│   ├── dependencies.rs
│   ├── decisions.rs
│   └── validation.rs
├── implementation/
│   ├── mod.rs
│   ├── generation.rs
│   ├── editing.rs
│   ├── patching.rs
│   ├── integration.rs
│   └── validation.rs
├── refactoring/
│   ├── mod.rs
│   ├── rename.rs
│   ├── extraction.rs
│   ├── restructuring.rs
│   └── equivalence.rs
├── optimization/
│   ├── mod.rs
│   ├── performance.rs
│   ├── memory.rs
│   ├── concurrency.rs
│   └── algorithms.rs
├── review/
│   ├── mod.rs
│   ├── correctness.rs
│   ├── maintainability.rs
│   ├── security.rs
│   └── compatibility.rs
└── traceability.rs
```

### 33\. Documentation crate

```text
crates/documentation/src/
├── lib.rs
├── error.rs
├── discovery.rs
├── inventory.rs
├── classification.rs
├── requirements.rs
├── templates.rs
├── generation.rs
├── editing.rs
├── validation.rs
├── coverage.rs
├── consistency.rs
├── source_references.rs
├── traceability.rs
├── design/
│   ├── mod.rs
│   ├── architecture.rs
│   ├── subsystem.rs
│   ├── component.rs
│   ├── interface.rs
│   ├── data_model.rs
│   ├── algorithms.rs
│   ├── integration.rs
│   └── acceptance.rs
├── formats/
│   ├── mod.rs
│   ├── markdown.rs
│   ├── asciidoc.rs
│   ├── html.rs
│   └── plain_text.rs
├── diagrams.rs
├── publishing.rs
└── batching.rs
```

Every implementation-ready design document shall address purpose, scope, responsibilities, dependencies, interfaces, data structures, algorithms, error handling, security, resource requirements, integration, testing and acceptance criteria.

This subsystem should be one of Zipporah's earliest complete engineering capabilities.

### 34\. Compilation crate

```text
crates/compilation/src/
├── lib.rs
├── error.rs
├── compiler.rs
├── toolchain.rs
├── build.rs
├── target.rs
├── environment.rs
├── diagnostics.rs
├── artifacts.rs
├── reproducibility.rs
├── cache.rs
├── dependency_resolution.rs
├── adapters/
│   ├── mod.rs
│   ├── cargo.rs
│   ├── cmake.rs
│   ├── make.rs
│   ├── gradle.rs
│   ├── maven.rs
│   ├── npm.rs
│   ├── python.rs
│   ├── go.rs
│   ├── danga.rs
│   └── generic.rs
└── verification.rs
```

Zipporah shall orchestrate existing compilers and build systems. It shall not attempt to replace every programming language compiler.

### 35\. Testing crate

```text
crates/testing/src/
├── lib.rs
├── error.rs
├── discovery.rs
├── test_case.rs
├── test_suite.rs
├── generation.rs
├── execution.rs
├── fixtures.rs
├── isolation.rs
├── assertions.rs
├── coverage.rs
├── results.rs
├── regression.rs
├── property_based.rs
├── mutation.rs
├── fuzzing.rs
├── integration.rs
├── end_to_end.rs
├── performance.rs
├── security.rs
├── flaky_detection.rs
└── reporting.rs
```

### 36\. Debugging crate

```text
crates/debugging/src/
├── lib.rs
├── error.rs
├── session.rs
├── diagnostic.rs
├── reproduction.rs
├── breakpoint.rs
├── stack_trace.rs
├── variable.rs
├── execution_trace.rs
├── root_cause.rs
├── hypothesis.rs
├── repair.rs
├── validation.rs
├── replay.rs
├── adapters/
│   ├── mod.rs
│   ├── dap.rs
│   ├── gdb.rs
│   └── lldb.rs
└── reporting.rs
```

### 37\. Research crate

```text
crates/research/src/
├── lib.rs
├── error.rs
├── question.rs
├── plan.rs
├── source.rs
├── discovery.rs
├── retrieval.rs
├── extraction.rs
├── credibility.rs
├── comparison.rs
├── synthesis.rs
├── citation.rs
├── provenance.rs
├── cache.rs
├── offline_library.rs
├── providers/
│   ├── mod.rs
│   ├── web.rs
│   ├── documentation.rs
│   ├── repository.rs
│   ├── academic.rs
│   └── local.rs
└── reporting.rs
```

Research results must distinguish verified facts, source claims, assumptions and unresolved uncertainty.

### Part X — Tools and execution isolation

### 38\. Tool infrastructure

```text
crates/tools/src/
├── lib.rs
├── error.rs
├── tool.rs
├── manifest.rs
├── registry.rs
├── discovery.rs
├── invocation.rs
├── arguments.rs
├── schema.rs
├── validation.rs
├── permissions.rs
├── execution.rs
├── result.rs
├── cancellation.rs
├── timeout.rs
├── rate_limit.rs
├── auditing.rs
└── adapters/
    ├── mod.rs
    ├── native.rs
    ├── process.rs
    ├── http.rs
    ├── mcp.rs
    └── plugin.rs
```

### 39\. Terminal crate

```text
crates/terminal/src/
├── lib.rs
├── error.rs
├── command.rs
├── arguments.rs
├── environment.rs
├── process.rs
├── execution.rs
├── stdin.rs
├── stdout.rs
├── stderr.rs
├── output_limits.rs
├── timeout.rs
├── cancellation.rs
├── process_tree.rs
├── working_directory.rs
├── allowlist.rs
├── policy.rs
└── audit.rs
```

Commands shall use structured argument passing wherever possible. Untrusted model-generated text must not be interpolated directly into shell commands.

### 40\. Filesystem crate

```text
crates/filesystem/src/
├── lib.rs
├── error.rs
├── path.rs
├── normalization.rs
├── canonicalization.rs
├── scope.rs
├── permissions.rs
├── reader.rs
├── writer.rs
├── atomic_write.rs
├── directory.rs
├── traversal.rs
├── watcher.rs
├── symlink.rs
├── locking.rs
├── temporary.rs
├── snapshot.rs
├── checksum.rs
└── recovery.rs
```

Filesystem operations must prevent unauthorized directory traversal, symlink escapes and accidental modification outside the assignment workspace.

### 41\. Sandbox crate

```text
crates/sandbox/src/
├── lib.rs
├── error.rs
├── sandbox.rs
├── profile.rs
├── capability.rs
├── filesystem.rs
├── network.rs
├── process.rs
├── resource_limits.rs
├── isolation.rs
├── lifecycle.rs
├── cleanup.rs
├── backends/
│   ├── mod.rs
│   ├── linux.rs
│   ├── windows.rs
│   ├── macos.rs
│   ├── container.rs
│   └── wasm.rs
└── verification.rs
```

Native isolation shall rely on appropriate operating system facilities. If required isolation is unavailable, privileged or untrusted execution must fail closed.

### Part XI — Security, governance and verification

### 42\. Security crate

```text
crates/security/src/
├── lib.rs
├── error.rs
├── threat_model.rs
├── authentication.rs
├── authorization.rs
├── secrets/
│   ├── mod.rs
│   ├── vault.rs
│   ├── keyring.rs
│   ├── rotation.rs
│   └── redaction.rs
├── cryptography/
│   ├── mod.rs
│   ├── hashing.rs
│   ├── encryption.rs
│   ├── signatures.rs
│   ├── key_management.rs
│   └── random.rs
├── permissions/
│   ├── mod.rs
│   ├── rbac.rs
│   ├── abac.rs
│   ├── capability.rs
│   ├── inheritance.rs
│   └── revocation.rs
├── defenses/
│   ├── mod.rs
│   ├── prompt_injection.rs
│   ├── command_injection.rs
│   ├── data_exfiltration.rs
│   ├── dependency_risk.rs
│   └── secret_leakage.rs
├── supply_chain/
│   ├── mod.rs
│   ├── sbom.rs
│   ├── provenance.rs
│   ├── signatures.rs
│   └── verification.rs
└── incident_response.rs
```

### 43\. Governance crate

```text
crates/governance/src/
├── lib.rs
├── error.rs
├── constitution.rs
├── policy.rs
├── policy_engine.rs
├── decision.rs
├── rules.rs
├── constraints.rs
├── authorization/
│   ├── mod.rs
│   ├── assignment.rs
│   ├── operation.rs
│   ├── approval.rs
│   ├── delegation.rs
│   ├── expiry.rs
│   └── revocation.rs
├── oversight/
│   ├── mod.rs
│   ├── human.rs
│   ├── escalation.rs
│   ├── intervention.rs
│   └── emergency_stop.rs
├── compliance.rs
├── exceptions.rs
└── evaluation.rs
```

### Assignment-level authorization

Zipporah shall avoid unnecessary repetitive approvals by supporting narrowly scoped, expiring and revocable assignment authorizations.

An authorization must specify the principal, repository, permitted operations, file scope, network scope, spending limits, expiry and applicable approval boundaries.

Agents cannot grant themselves additional authority.

### 44\. Verification crate

```text
crates/verification/src/
├── lib.rs
├── error.rs
├── verifier.rs
├── verification_plan.rs
├── requirements.rs
├── acceptance.rs
├── evidence.rs
├── provenance.rs
├── independent_review.rs
├── reproducibility.rs
├── static_analysis.rs
├── dynamic_analysis.rs
├── formal/
│   ├── mod.rs
│   ├── specification.rs
│   ├── invariants.rs
│   ├── model_checking.rs
│   └── proof_adapter.rs
├── repository/
│   ├── mod.rs
│   ├── diff.rs
│   ├── scope.rs
│   ├── batch.rs
│   └── integration.rs
├── quality/
│   ├── mod.rs
│   ├── correctness.rs
│   ├── completeness.rs
│   ├── consistency.rs
│   └── maintainability.rs
└── reporting.rs
```

Verification must use independent execution or evidence wherever possible. A separate agent reviewing output from the same model is useful but does not guarantee independence or correctness.

### 45\. Audit crate

```text
crates/audit/src/
├── lib.rs
├── error.rs
├── record.rs
├── journal.rs
├── actor.rs
├── operation.rs
├── authorization.rs
├── evidence.rs
├── hash_chain.rs
├── integrity.rs
├── redaction.rs
├── query.rs
├── retention.rs
├── export.rs
└── verification.rs
```

Audit records should be tamper-evident, with appropriate access controls and optional signed checkpoints.

### Security threat model

| Threat                            | Primary mitigation                                  |
| --------------------------------- | --------------------------------------------------- |
| Malicious repository instructions | Instruction trust boundaries                        |
| Prompt injection                  | Data/instruction separation and capability controls |
| Credential theft                  | OS keyring, scoped credentials and redaction        |
| Unauthorized modifications        | Assignment permissions and diff validation          |
| Malicious dependencies            | Dependency auditing and provenance                  |
| Resource exhaustion               | Admission control and bounded execution             |
| Data exfiltration                 | Default-deny network policies for restricted tasks  |
| Fabricated success                | Evidence-based completion gates                     |
| Model supply-chain attacks        | Integrity checks and trusted manifests              |
| Malicious plugins                 | Sandboxed execution and capability restrictions     |
| Agent privilege escalation        | External authorization enforcement                  |
| Interrupted execution             | Durable checkpoints and reconciliation              |

### Part XII — Networking and distributed infrastructure

### 46\. Networking crate

```text
crates/networking/src/
├── lib.rs
├── error.rs
├── transport.rs
├── connection.rs
├── endpoint.rs
├── discovery.rs
├── authentication.rs
├── tls.rs
├── http.rs
├── websocket.rs
├── quic.rs
├── retry.rs
├── timeout.rs
├── rate_limit.rs
├── bandwidth.rs
├── proxy.rs
├── offline.rs
└── policy.rs
```

### 47\. Synchronization crate

```text
crates/synchronization/src/
├── lib.rs
├── error.rs
├── synchronization.rs
├── manifest.rs
├── change_set.rs
├── version.rs
├── conflict.rs
├── reconciliation.rs
├── replication.rs
├── compression.rs
├── encryption.rs
├── integrity.rs
├── checkpoint.rs
├── offline_queue.rs
└── transport.rs
```

### 48\. Distributed computing crate

```text
crates/distributed/src/
├── lib.rs
├── error.rs
├── node.rs
├── identity.rs
├── membership.rs
├── discovery.rs
├── registry.rs
├── heartbeat.rs
├── capabilities.rs
├── resources.rs
├── placement.rs
├── scheduler.rs
├── worker.rs
├── coordinator.rs
├── execution.rs
├── task_lease.rs
├── artifact_transfer.rs
├── checkpoint.rs
├── recovery.rs
├── partition.rs
├── reconciliation.rs
├── security.rs
└── metrics.rs
```

Zipporah Mesh

Private authenticated computing network

Nodes advertise resources and capabilities. Work is placed according to authorization, hardware availability, data locality and execution requirements.

Distributed execution must tolerate network partitions, worker failures, duplicate deliveries and interrupted artifact transfers. It must not assume that distributed RAM behaves as one physical memory pool.

### Part XIII — Extensibility and integration

### 49\. Providers crate

```text
crates/providers/src/
├── lib.rs
├── error.rs
├── provider.rs
├── manifest.rs
├── registry.rs
├── discovery.rs
├── capabilities.rs
├── credentials.rs
├── health.rs
├── routing.rs
├── fallback.rs
├── inference/
│   ├── mod.rs
│   ├── openai.rs
│   ├── anthropic.rs
│   ├── gemini.rs
│   ├── deepseek.rs
│   ├── ollama.rs
│   ├── local.rs
│   └── generic.rs
├── repositories/
│   ├── mod.rs
│   ├── github.rs
│   ├── gitlab.rs
│   └── generic.rs
├── storage/
├── research/
└── compute/
```

Providers shall be optional, independently configurable and replaceable.

### 50\. Interoperability crate

```text
crates/interoperability/src/
├── lib.rs
├── error.rs
├── protocol.rs
├── negotiation.rs
├── compatibility.rs
├── serialization.rs
├── json_rpc/
├── mcp/
│   ├── mod.rs
│   ├── client.rs
│   ├── server.rs
│   ├── transport.rs
│   ├── tools.rs
│   ├── resources.rs
│   └── security.rs
├── lsp/
├── dap/
├── rest/
├── grpc/
├── openapi/
└── ulabi/
```

Zipporah shall support established interoperability protocols while leaving room for future ULABI integration.

### 51\. Plugin infrastructure

```text
crates/plugins/src/
├── lib.rs
├── error.rs
├── plugin.rs
├── manifest.rs
├── registry.rs
├── loader.rs
├── installer.rs
├── lifecycle.rs
├── compatibility.rs
├── permissions.rs
├── signatures.rs
├── sandbox.rs
├── host.rs
├── wasm.rs
├── process.rs
├── marketplace.rs
└── updates.rs
```

Third-party plugins should initially execute through isolated processes or WebAssembly components rather than unrestricted native dynamic libraries.

### 52\. SDK crate

```text
crates/sdk/src/
├── lib.rs
├── error.rs
├── client.rs
├── configuration.rs
├── authentication.rs
├── assignments.rs
├── workflows.rs
├── agents.rs
├── models.rs
├── repositories.rs
├── artifacts.rs
├── events.rs
├── plugins.rs
└── streaming.rs
```

### Part XIV — Operations and evolution

### 53\. Observability crate

```text
crates/observability/src/
├── lib.rs
├── error.rs
├── logging.rs
├── tracing.rs
├── metrics.rs
├── health.rs
├── diagnostics.rs
├── profiling.rs
├── alerts.rs
├── dashboards.rs
├── redaction.rs
├── exporters.rs
└── retention.rs
```

Telemetry shall be local by default. External telemetry requires explicit configuration and authorization.

### 54\. Economics and budget management

```text
crates/economics/src/
├── lib.rs
├── error.rs
├── budget.rs
├── usage.rs
├── pricing.rs
├── estimation.rs
├── accounting.rs
├── token_usage.rs
├── compute_usage.rs
├── storage_usage.rs
├── optimization.rs
├── provider_comparison.rs
├── spending_limits.rs
└── reporting.rs
```

This subsystem shall manage AI consumption and computational expenditure, not act as a financial payment intermediary.

### 55\. Deployment crate

```text
crates/deployment/src/
├── lib.rs
├── error.rs
├── environment.rs
├── artifact.rs
├── package.rs
├── release.rs
├── signing.rs
├── verification.rs
├── strategy.rs
├── approval.rs
├── rollout.rs
├── rollback.rs
├── health_check.rs
├── providers/
│   ├── mod.rs
│   ├── local.rs
│   ├── container.rs
│   ├── server.rs
│   └── cloud.rs
└── reporting.rs
```

Production deployment shall require appropriate release authority. AI-generated code must not be automatically deployed merely because compilation succeeds.

### 56\. Maintenance crate

```text
crates/maintenance/src/
├── lib.rs
├── error.rs
├── monitoring.rs
├── dependency_updates.rs
├── vulnerability_management.rs
├── technical_debt.rs
├── regression_detection.rs
├── compatibility.rs
├── backup.rs
├── recovery.rs
├── cleanup.rs
├── lifecycle.rs
└── reporting.rs
```

### 57\. Controlled evolution crate

```text
crates/evolution/src/
├── lib.rs
├── error.rs
├── proposal.rs
├── experiment.rs
├── baseline.rs
├── evaluation.rs
├── benchmarking.rs
├── regression.rs
├── candidate.rs
├── policy.rs
├── review.rs
├── approval.rs
├── migration.rs
├── rollback.rs
└── history.rs
```

Zipporah may propose improvements to itself, but shall not silently modify its own authorization, governance or verification mechanisms.

### Part XV — Applications and interfaces

### 58\. Application directories

```text
applications/
├── cli/
│   ├── Cargo.toml
│   └── src/
│       ├── main.rs
│       ├── arguments.rs
│       ├── output.rs
│       └── commands/
│           ├── init.rs
│           ├── doctor.rs
│           ├── repository.rs
│           ├── assignment.rs
│           ├── agent.rs
│           ├── model.rs
│           ├── workflow.rs
│           ├── memory.rs
│           ├── security.rs
│           ├── server.rs
│           └── mesh.rs
├── studio/
│   ├── Cargo.toml
│   └── src/
│       ├── main.rs
│       ├── application.rs
│       ├── state.rs
│       ├── navigation.rs
│       ├── editor/
│       ├── terminal/
│       ├── workspace/
│       ├── assignments/
│       ├── agents/
│       ├── models/
│       ├── repositories/
│       ├── review/
│       ├── resources/
│       ├── settings/
│       └── components/
├── server/
│   ├── Cargo.toml
│   └── src/
│       ├── main.rs
│       ├── server.rs
│       ├── authentication.rs
│       ├── middleware/
│       ├── routes/
│       ├── sessions/
│       └── streaming/
└── mobile/
    ├── Cargo.toml
    └── src/
        ├── main.rs
        ├── connection/
        ├── dashboard/
        ├── assignments/
        ├── approvals/
        ├── notifications/
        └── settings/
```

### 59\. Zipporah Studio interface

Zipporah Studio

Local workspace

⑂ documentation-batch

Local inference · Safe mode

Conceptual interface layout, not an existing application screenshot.

The Studio shall provide repository exploration, editing, terminal access, agent conversations, assignment management, review panels, model management, resource monitoring, approvals, memory inspection and audit history.

### 60\. CLI command specification

```bash
zipporah init
zipporah doctor
zipporah status

zipporah repo clone
zipporah repo inspect
zipporah repo index
zipporah repo instructions
zipporah repo review

zipporah assignment create
zipporah assignment plan
zipporah assignment run
zipporah assignment pause
zipporah assignment resume
zipporah assignment cancel
zipporah assignment status
zipporah assignment verify

zipporah agent list
zipporah agent inspect
zipporah agent configure

zipporah model search
zipporah model download
zipporah model import
zipporah model load
zipporah model unload
zipporah model benchmark

zipporah workflow validate
zipporah workflow run
zipporah workflow replay

zipporah memory search
zipporah memory export
zipporah memory purge

zipporah security audit
zipporah security permissions
zipporah security revoke

zipporah server start
zipporah server stop

zipporah mesh join
zipporah mesh nodes
zipporah mesh status
```

These commands define the proposed interface, not commands that are currently executable.

### 61\. Editor integrations

```text
extensions/
├── vscode/
│   ├── manifest/
│   ├── bridge/
│   ├── commands/
│   ├── panels/
│   ├── configuration/
│   └── tests/
├── neovim/
├── jetbrains/
├── emacs/
└── generic/
```

The primary engineering runtime shall remain independent of the editor.

A conventional VS Code extension requires a JavaScript-compatible entry point. If the Safe Rust-only rule is absolute for all first-party code, Zipporah should initially integrate through CLI tasks, language servers and external processes. A minimal non-Rust editor bridge would require an explicitly approved exception.

### Part XVI — Comprehensive technology stack

### 62\. Core technology selection

| Layer                         | Proposed technology                     |
| ----------------------------- | --------------------------------------- |
| Implementation                | Stable Rust                             |
| Package management            | Cargo                                   |
| Build system                  | Cargo workspace                         |
| Async runtime                 | Tokio                                   |
| Parallel computation          | Rayon                                   |
| Error handling                | thiserror                               |
| Serialization                 | Serde                                   |
| Configuration                 | TOML                                    |
| Identifiers                   | UUID                                    |
| Time handling                 | time                                    |
| CLI                           | Clap                                    |
| Interactive terminal UI       | Ratatui                                 |
| Native desktop UI             | egui / eframe                           |
| API server                    | Axum                                    |
| HTTP client                   | Reqwest                                 |
| HTTP middleware               | Tower                                   |
| TLS                           | Rustls                                  |
| WebSocket                     | Tokio-Tungstenite                       |
| QUIC                          | Quinn                                   |
| RPC                           | Tonic / Prost                           |
| Embedded database             | redb                                    |
| Optional relational database  | SQLite / SQLx                           |
| Enterprise storage adapter    | PostgreSQL                              |
| Full-text search              | Tantivy                                 |
| Graph processing              | Petgraph                                |
| Source parsing                | Tree-sitter                             |
| Language server integration   | LSP protocol libraries                  |
| Git integration               | Controlled Git CLI or gix               |
| Local inference               | Candle                                  |
| Alternative inference         | mistral.rs                              |
| Optional inference services   | Ollama / llama.cpp                      |
| Machine learning              | Burn                                    |
| Tokenization                  | Hugging Face Tokenizers                 |
| Model storage                 | SafeTensors / GGUF                      |
| Embeddings                    | Candle-compatible models                |
| Vector indexing               | Embedded bounded vector index           |
| Plugin isolation              | WebAssembly / Wasmtime                  |
| Logging                       | Tracing                                 |
| Metrics                       | metrics                                 |
| Optional observability export | OpenTelemetry                           |
| System resource monitoring    | sysinfo                                 |
| Filesystem monitoring         | notify                                  |
| Cryptographic hashing         | BLAKE3 / SHA-256                        |
| Authenticated encryption      | RustCrypto AEAD libraries               |
| Digital signatures            | ed25519-dalek                           |
| Secret handling               | secrecy / zeroize                       |
| Credential storage            | Operating system keyring                |
| Property testing              | proptest                                |
| Concurrency testing           | Loom                                    |
| Benchmarking                  | Criterion                               |
| Fuzzing                       | cargo-fuzz                              |
| Dependency auditing           | cargo-audit                             |
| Dependency policy             | cargo-deny                              |
| SBOM                          | cargo-cyclonedx                         |
| CI/CD                         | GitHub Actions                          |
| Packaging                     | Native binaries and platform installers |
| Containers                    | Optional Podman or Docker               |

The stack is a proposed selection. Exact crate versions, licenses, platform compatibility, maintenance status and unsafe-code exposure must be audited before adoption.

### 63\. External dependency elimination

| Previous Tariro Studio dependency | Zipporah strategy                               |
| --------------------------------- | ----------------------------------------------- |
| Python                            | Safe Rust implementation                        |
| FastAPI                           | Axum                                            |
| Uvicorn                           | Tokio-based server                              |
| LiteLLM                           | Native model routing                            |
| Redis                             | Embedded persistent task and event storage      |
| Qdrant                            | Embedded semantic indexing                      |
| Ollama                            | Optional provider; embedded inference preferred |
| SearXNG                           | Optional research adapter                       |
| Docker Compose                    | Native executable with optional containers      |
| External agent frameworks         | Native agent runtime                            |
| GitHub                            | Retained                                        |

The objective is not to prohibit external software. It is to prevent external software from becoming an unavoidable dependency.

### 64\. AI model compatibility

| Model family              | Potential role                |
| ------------------------- | ----------------------------- |
| Qwen Coder                | Programming and documentation |
| DeepSeek Coder            | Software engineering          |
| DeepSeek reasoning models | Complex reasoning             |
| Llama                     | General-purpose intelligence  |
| Mistral                   | General-purpose intelligence  |
| Gemma                     | Lightweight local inference   |
| Phi                       | Small-model tasks             |
| StarCoder                 | Source code generation        |
| BGE                       | Embeddings and retrieval      |
| Whisper                   | Speech recognition            |

Actual model compatibility shall be determined through the model registry and inference backend capability negotiation.

### Part XVII — Data architecture

### 65\. Local installation layout

```text
~/.zipporah/
├── config/
│   ├── zipporah.toml
│   ├── providers.toml
│   ├── resources.toml
│   └── policies.toml
├── data/
│   ├── metadata.redb
│   ├── assignments/
│   ├── checkpoints/
│   ├── events/
│   ├── memory/
│   ├── knowledge/
│   └── indexes/
├── models/
│   ├── manifests/
│   ├── weights/
│   ├── tokenizers/
│   └── cache/
├── workspaces/
├── repositories/
├── artifacts/
├── plugins/
├── workflows/
├── audit/
├── logs/
├── backups/
└── temporary/
```

Platform-specific data directories should follow operating system conventions. Credentials shall be stored in an appropriate secure credential store, not plaintext configuration files.

### 66\. Core data entities

| Entity        | Primary information                                 |
| ------------- | --------------------------------------------------- |
| Principal     | Identity, roles and attributes                      |
| Workspace     | Owner, configuration and resource scope             |
| Repository    | Provider, location, revision and instructions       |
| Assignment    | Requirements, authorization and lifecycle           |
| Task          | Dependencies, execution state and resource limits   |
| Agent         | Identity, role, capabilities and permissions        |
| Workflow      | Versioned execution graph                           |
| Model         | Manifest, capabilities, format and integrity digest |
| Execution     | Actor, operation, timestamps and outcome            |
| Checkpoint    | Durable state and artifact references               |
| Artifact      | Content digest, provenance and storage location     |
| Evidence      | Verification method and observed results            |
| Authorization | Scope, expiry and permitted operations              |
| Audit event   | Actor, decision, action and integrity metadata      |
| Pull request  | Repository, branch, commits and remote identifier   |
| Memory record | Scope, content, provenance and retention policy     |

### 67\. Assignment persistence contract

Every assignment record must contain at minimum:

```text
Assignment
├── assignment_id
├── schema_version
├── owner_id
├── workspace_id
├── repository_id
├── base_revision
├── requirements
├── scope
├── authorization_id
├── resource_budget
├── execution_plan
├── current_state
├── state_revision
├── completed_tasks
├── pending_tasks
├── checkpoint_references
├── artifact_references
├── evidence_references
├── external_operation_records
├── created_at
└── updated_at
```

State updates shall use transactions and revision checks to prevent lost updates. External operations shall use reconciliation and idempotency mechanisms where supported.

### 68\. Suggested 900 GB storage budget

### Personal installation storage planning

### 900 GB

Operating system and applications

100 GB

AI models

150 GB

Repositories and workspaces

200 GB

Build artifacts and caches

100 GB

Memory and search indexes

50 GB

Snapshots and local backups

100 GB

Free capacity and expansion

200 GB

This allocation is illustrative. Local snapshots do not replace independent external backups.

### Part XVIII — APIs and communication protocols

### 69\. Proposed REST API

```text
/api/v1/
├── health
├── capabilities
├── sessions
├── users
├── workspaces
├── repositories
│   ├── {id}
│   ├── {id}/inspect
│   ├── {id}/instructions
│   └── {id}/pull-requests
├── assignments
│   ├── {id}
│   ├── {id}/plan
│   ├── {id}/run
│   ├── {id}/pause
│   ├── {id}/resume
│   ├── {id}/cancel
│   ├── {id}/progress
│   └── {id}/evidence
├── agents
├── workflows
├── models
├── inference
├── memory
├── knowledge
├── search
├── artifacts
├── approvals
├── permissions
├── resources
├── audit
├── plugins
├── events
└── mesh
```

The server shall bind to loopback by default. Remote access requires authentication, secure transport and explicit configuration.

### 70\. Interface requirements

| Interface                         | Protocol                         |
| --------------------------------- | -------------------------------- |
| Local application                 | Rust API                         |
| Local CLI to daemon               | Authenticated IPC                |
| Remote applications               | HTTPS                            |
| Streaming progress                | SSE or WebSocket                 |
| Distributed workers               | Authenticated RPC                |
| External tools                    | MCP                              |
| Language servers                  | LSP                              |
| Debuggers                         | DAP                              |
| Plugins                           | WebAssembly component interfaces |
| Future universal interoperability | ULABI adapter                    |

All public protocols require version negotiation, structured errors, request size limits, authentication and compatibility testing.

### Part XIX — Specifications and documentation

### 71\. Specification directory

```text
specifications/
├── 0000-foundation/
│   ├── objectives.md
│   ├── constitution.md
│   ├── terminology.md
│   └── architectural-principles.md
├── 0100-architecture/
│   ├── system-architecture.md
│   ├── component-boundaries.md
│   ├── dependency-rules.md
│   └── deployment-models.md
├── 0200-runtime/
├── 0300-resources/
├── 0400-intelligence/
├── 0500-inference/
├── 0600-model-management/
├── 0700-context/
├── 0800-memory/
├── 0900-knowledge/
├── 1000-agents/
├── 1100-orchestration/
├── 1200-assignments/
├── 1300-workflows/
├── 1400-repositories/
├── 1500-source-analysis/
├── 1600-engineering/
├── 1700-documentation/
├── 1800-compilation/
├── 1900-testing/
├── 2000-debugging/
├── 2100-verification/
├── 2200-tools/
├── 2300-security/
├── 2400-governance/
├── 2500-storage/
├── 2600-networking/
├── 2700-distributed/
├── 2800-interoperability/
├── 2900-plugins/
├── 3000-applications/
├── 3100-observability/
├── 3200-economics/
├── 3300-deployment/
├── 3400-maintenance/
├── 3500-evolution/
└── 3600-acceptance/
```

### 72\. Documentation directory

```text
documentation/
├── getting-started/
│   ├── installation.md
│   ├── first-assignment.md
│   └── hardware-requirements.md
├── user-guide/
├── administrator-guide/
├── developer-guide/
├── architecture/
├── api/
├── cli/
├── studio/
├── agents/
├── workflows/
├── models/
├── repositories/
├── security/
├── deployment/
├── troubleshooting/
├── tutorials/
├── examples/
├── decisions/
│   ├── ADR-0001-safe-rust.md
│   ├── ADR-0002-local-first.md
│   ├── ADR-0003-provider-neutrality.md
│   └── ADR-0004-persistent-assignments.md
└── reference/
```

### 73\. Configuration directory

```text
configurations/
├── minimal/
├── lightweight/
├── personal/
├── standard/
├── workstation/
├── server/
├── enterprise/
├── distributed/
├── offline/
├── air-gapped/
└── development/
```

Each profile shall define resource limits, available features, inference strategy, storage backend, network policy and execution concurrency.

### 74\. Policy directory

```text
policies/
├── default.toml
├── security/
│   ├── filesystem.toml
│   ├── network.toml
│   ├── terminal.toml
│   └── credentials.toml
├── governance/
│   ├── authorization.toml
│   ├── approvals.toml
│   └── delegation.toml
├── engineering/
│   ├── documentation.toml
│   ├── implementation.toml
│   ├── testing.toml
│   └── verification.toml
├── repository/
│   ├── branches.toml
│   ├── commits.toml
│   ├── pull_requests.toml
│   └── releases.toml
├── resources/
├── models/
├── plugins/
└── privacy/
```

### 75\. Reusable workflow library

```text
workflows/
├── documentation/
│   ├── repository-audit.toml
│   ├── design-document.toml
│   └── batch-documentation.toml
├── engineering/
│   ├── feature-development.toml
│   ├── bug-repair.toml
│   ├── refactoring.toml
│   └── migration.toml
├── verification/
│   ├── code-review.toml
│   ├── security-review.toml
│   └── acceptance-testing.toml
├── maintenance/
│   ├── dependency-update.toml
│   └── regression-repair.toml
├── research/
├── release/
└── self-improvement/
```

### Part XX — Testing and production readiness

### 76\. Testing directory

```text
tests/
├── unit/
├── integration/
├── end-to-end/
├── acceptance/
├── regression/
├── security/
│   ├── authorization/
│   ├── sandbox/
│   ├── prompt-injection/
│   ├── filesystem/
│   └── credential-protection/
├── reliability/
│   ├── crash-recovery/
│   ├── power-interruption/
│   ├── network-failure/
│   └── duplicate-execution/
├── resources/
│   ├── memory/
│   ├── cpu/
│   ├── storage/
│   └── concurrency/
├── compatibility/
├── distributed/
├── models/
├── repository/
├── workflows/
└── fixtures/
```

### 77\. Benchmark directory

```text
benchmarks/
├── runtime/
├── inference/
├── scheduling/
├── repository-indexing/
├── source-analysis/
├── semantic-search/
├── memory/
├── storage/
├── agent-execution/
├── assignment-recovery/
├── distributed/
└── hardware-profiles/
```

Benchmarks must record hardware, software versions, model identity, configuration, workload and measured resource usage.

### 78\. CI/CD pipelines

```text
.github/workflows/
├── format.yml
├── clippy.yml
├── unit-tests.yml
├── integration-tests.yml
├── acceptance-tests.yml
├── security-audit.yml
├── dependency-policy.yml
├── unsafe-code-policy.yml
├── documentation.yml
├── compatibility.yml
├── fuzzing.yml
├── benchmarks.yml
├── sbom.yml
├── reproducibility.yml
├── packaging.yml
└── release.yml
```

### Safe Rust enforcement

Every first-party crate shall inherit workspace lint requirements.

```toml
[workspace.lints.rust]
unsafe_code = "forbid"

[workspace.lints.clippy]
dbg_macro = "deny"
todo = "deny"
unimplemented = "deny"
```

Each member crate:

```toml
[lints]
workspace = true
```

Crate roots should additionally declare:

```rust
#![forbid(unsafe_code)]
```

This policy does not automatically extend to transitive dependencies. Dependency review and explicit exceptions are required for native or unsafe-backed libraries.

### 79\. Production acceptance gates

### Production readiness checklist

0/16

All first-party crates satisfy Safe Rust policy

No unresolved critical security findings

Repository instructions are correctly enforced

Assignment authorization cannot be bypassed

Completed assignments have verifiable evidence

Interrupted assignments recover correctly

Resource limits are enforced under pressure

Unauthorized filesystem access is prevented

Secrets are not exposed in logs or prompts

Git operations are recoverable and reconciled

Offline operation passes acceptance tests

Local inference passes hardware compatibility tests

Public interfaces are documented and versioned

Installation and upgrade procedures are verified

Backups and restoration are tested

Release artifacts have integrity verification

Acceptance criteria to verify during development. None are claimed to have passed yet.

### 80\. Initial non-functional targets

| Requirement                | Proposed target                                                    |
| -------------------------- | ------------------------------------------------------------------ |
| Idle runtime memory        | Under 500 MB, excluding loaded models and large indexes            |
| Assignment durability      | Checkpoint after every verified work unit                          |
| Cancellation               | Responsive cooperative cancellation with enforced process timeouts |
| Resource limits            | Enforced per assignment                                            |
| Repository indexing        | Incremental after initial indexing                                 |
| Offline availability       | All local-only capabilities                                        |
| Secret disclosure          | Zero authorized plaintext disclosures to model prompts             |
| Recovery                   | Resume from last durable verified checkpoint                       |
| Network access             | Explicitly governed                                                |
| Audit coverage             | All privileged operations                                          |
| Model concurrency on 16 GB | One loaded generation model initially                              |
| Data export                | Documented portable formats                                        |
| Unverified completion      | Prohibited                                                         |

Performance targets must be validated through actual hardware testing.

### Part XXI — Packaging and deployment

### 81\. Packaging structure

```text
packaging/
├── linux/
│   ├── deb/
│   ├── rpm/
│   ├── appimage/
│   └── flatpak/
├── windows/
│   ├── msi/
│   └── portable/
├── macos/
│   ├── app/
│   └── dmg/
├── android/
├── ios/
├── containers/
└── checksums/
```

### 82\. Deployment structure

```text
deployment/
├── standalone/
├── desktop/
├── headless/
├── self-hosted/
├── containers/
├── systemd/
├── windows-service/
├── distributed/
├── enterprise/
└── cloud/
```

### 83\. Supported platforms

| Platform             | Intended support                                  |
| -------------------- | ------------------------------------------------- |
| Linux x86-64         | Primary development target                        |
| Linux ARM64          | Secondary target                                  |
| Windows x86-64       | Desktop and CLI                                   |
| Windows ARM64        | Progressive support                               |
| macOS ARM64          | Desktop and CLI                                   |
| macOS x86-64         | Subject to toolchain support                      |
| Android              | Remote management and lightweight local execution |
| iOS                  | Remote management                                 |
| Web                  | Optional browser-based interface                  |
| Private servers      | Headless execution                                |
| Distributed clusters | Later-stage support                               |

Cross-platform capabilities shall be explicitly advertised. Zipporah must not claim identical functionality on platforms with different isolation, inference or execution facilities.

### Part XXII — Implementation dependency order

### 84\. Development phases

Phase 0

Repository preservation and design

Archive Tariro Studio, audit existing functionality, write foundational specifications.

Phase 1

Safe Rust foundation

Foundation, configuration, identity, storage, events and workspace CI.

Phase 2

Reliable execution

Runtime, resources, scheduler, cancellation, checkpoints and recovery.

Phase 3

Security boundaries

Authorization, filesystem scope, sandbox, terminal and auditing.

Phase 4

Repository engineering

Git, GitHub, repository discovery, AGENTS.md and source indexing.

Phase 5

AI intelligence

Model providers, inference adapters, context management and model registry.

Phase 6

Persistent agents

Assignments, workflows, agents, orchestration and memory.

Phase 7

Documentation engineering

Design generation, independent review, batching and pull requests.

Phase 8

Software engineering

Implementation, compilation, testing, debugging and verification.

Phase 9

Applications

Native Studio, editor integration, server and mobile management.

Phase 10

Native independence

Embedded inference, semantic search and advanced model management.

Phase 11

Distributed infrastructure

Compute mesh, remote workers, synchronization and artifact transfer.

Phase 12

Advanced ecosystem

SDKs, marketplaces, enterprise governance and controlled evolution.

### 85\. Initial minimum viable workspace

Despite the comprehensive target architecture, the first functional release should contain a much smaller set of components.

```text
Zipporah/
├── crates/
│   ├── foundation/
│   ├── configuration/
│   ├── storage/
│   ├── runtime/
│   ├── resources/
│   ├── governance/
│   ├── repository/
│   ├── intelligence/
│   ├── assignments/
│   ├── documentation/
│   └── verification/
├── applications/
│   └── cli/
├── specifications/
├── tests/
├── Cargo.toml
└── AGENTS.md
```

Additional boundaries can initially exist as internal modules and become independent crates when justified by implementation complexity.

### 86\. Release roadmap

| Version | Release objective                              |
| ------- | ---------------------------------------------- |
| v0.0.1  | Repository transformation and specifications   |
| v0.1.0  | Safe Rust foundation and CLI                   |
| v0.2.0  | Secure repository management                   |
| v0.3.0  | Local and remote model integration             |
| v0.4.0  | Persistent assignment execution                |
| v0.5.0  | Verified documentation engineering             |
| v0.6.0  | Coding, compilation and testing                |
| v0.7.0  | Editor integration                             |
| v0.8.0  | Native Zipporah Studio                         |
| v0.9.0  | Advanced orchestration and reliability         |
| v1.0.0  | Production-ready personal engineering platform |
| v1.5.0  | Embedded inference and advanced knowledge      |
| v2.0.0  | Distributed engineering infrastructure         |
| v3.0.0  | Universal engineering ecosystem                |

These milestones represent capability progression rather than fixed release dates.

### Part XXIII — First end-to-end acceptance scenario

### 87\. Vimbai documentation assignment

Zipporah's first major acceptance scenario shall demonstrate its ability to perform your existing documentation workflow reliably.

Assignment: Complete Vimbai design documents

Documentation only · Exactly 30 files per PR · Persistent execution

* Authenticate with GitHub using scoped credentials.

* Clone Vimbai and pin the inspected repository revision.

* Discover all applicable AGENTS.md files.

* Inspect existing source files and design documents.

* Identify incomplete documentation and dependency order.

* Create an authorized assignment plan.

* Write the first design document individually.

* Verify its correctness against actual repository evidence.

* Persist the document and checkpoint.

* Repeat the process until exactly 30 eligible files are verified.

* Inspect the complete diff for unauthorized changes.

* Create a dedicated branch and commit.

* Push the branch and create a pull request.

* Record the remote pull request identifier.

* Inspect CI results and reconcile failures.

* Continue the next authorized batch.

### Mandatory acceptance conditions

| Test                                | Expected outcome                        |
| ----------------------------------- | --------------------------------------- |
| Shutdown after document 17          | Resume from last verified checkpoint    |
| Attempt to edit Rust implementation | Denied                                  |
| Attempt to include 31 files         | Batch validation fails                  |
| Only 12 eligible files remain       | Await revised batch authorization       |
| Missing repository instruction      | Execution blocked until resolved        |
| Expired GitHub authorization        | Remote operations paused                |
| Network interruption during push    | Reconcile remote state before retry     |
| Duplicate PR creation attempt       | Detect existing PR                      |
| Fabricated document references      | Verification fails                      |
| CI failure                          | Report actual failure and preserve work |
| Model exceeds memory budget         | Safely reduce workload or pause         |
| User revokes assignment             | Prevent further privileged execution    |

This scenario shall be implemented before expanding into large-scale autonomous software development.

### Part XXIV — Migration from Tariro Studio

### 88\. Migration procedure

The existing repository should be preserved and transformed rather than deleted.

| Step | Required action                                        |
| ---- | ------------------------------------------------------ |
| 1    | Inspect current repository state                       |
| 2    | Read all applicable repository instructions            |
| 3    | Inventory existing features and documents              |
| 4    | Preserve existing commit history                       |
| 5    | Create a legacy branch and archival tag                |
| 6    | Rename repository to Zipporah, subject to availability |
| 7    | Extract reusable requirements                          |
| 8    | Classify working and incomplete functionality          |
| 9    | Establish the new architecture specifications          |
| 10   | Create the Safe Rust workspace                         |
| 11   | Establish CI and security enforcement                  |
| 12   | Implement components in dependency order               |
| 13   | Verify replacement capabilities                        |
| 14   | Retire legacy implementation only after acceptance     |

### 89\. Feature migration classification

Every existing Tariro Studio feature shall receive one of the following classifications.

| Classification | Meaning                                              |
| -------------- | ---------------------------------------------------- |
| Preserve       | Existing valuable functionality or requirements      |
| Rewrite        | Required capability needing Safe Rust implementation |
| Consolidate    | Duplicate or overlapping capabilities                |
| Redesign       | Existing architectural approach is unsuitable        |
| Experimental   | Requires research and validation                     |
| Simulated      | Claims functionality without actual execution        |
| Retire         | Obsolete or unnecessary capability                   |
| Blocked        | Cannot migrate until dependencies are resolved       |

A migration register shall record the original file, classification, target subsystem, specification reference, implementation status and acceptance evidence.

### Part XXV — Future ecosystem

### 90\. Integration with independent projects

| Project  | Potential integration                    |
| -------- | ---------------------------------------- |
| Tariro   | General-purpose agent orchestration      |
| Zamani   | Language development and compilation     |
| Mambo    | Compiler and development toolchain       |
| Danga    | Package and build management             |
| ULABI    | Language-neutral interoperability        |
| SamuelDB | Optional database backend                |
| Farai OS | Native operating environment             |
| Verengai | Knowledge and information infrastructure |
| Vimbai   | Software engineering and maintenance     |

None of these projects shall become a compulsory dependency of Zipporah.

### 91\. Long-term product family

| Product             | Function                              |
| ------------------- | ------------------------------------- |
| Zipporah Core       | Foundational runtime                  |
| Zipporah Studio     | Complete engineering environment      |
| Zipporah Engine     | AI inference                          |
| Zipporah Agents     | Specialized intelligence              |
| Zipporah Memory     | Persistent knowledge                  |
| Zipporah Guard      | Security and governance               |
| Zipporah CLI        | Command-line interface                |
| Zipporah Server     | Headless execution                    |
| Zipporah Mesh       | Distributed computing                 |
| Zipporah Mobile     | Remote management                     |
| Zipporah Hub        | Model, agent and workflow marketplace |
| Zipporah SDK        | Developer integrations                |
| Zipporah Enterprise | Organizational infrastructure         |

### Part XXVI — Final engineering requirements

### 92\. Prohibited implementation practices

Zipporah shall prohibit fabricated functionality, simulated success, silent failures, uncontrolled background execution, unauthorized repository modifications, unbounded resource consumption, plaintext credential storage, mandatory telemetry, undocumented interfaces, circular dependencies, unverified deployment and unauthorized self-modification.

### 93\. Definition of done

A component shall be considered complete only when its design specification, implementation, public interfaces, integration requirements, security controls, error handling, resource constraints, tests and acceptance evidence are complete.

A file existing in the repository is not evidence that its functionality exists.

### 94\. Final architectural decisions

| Decision                     | Selection                        |
| ---------------------------- | -------------------------------- |
| Project identity             | Zipporah                         |
| Flagship application         | Zipporah Studio                  |
| Architecture                 | Modular, local-first             |
| First-party implementation   | Safe Rust                        |
| Initial inference            | Interchangeable existing engines |
| Long-term inference          | Optional native Zipporah Engine  |
| Initial storage              | Embedded database                |
| Repository hosting           | GitHub retained                  |
| Initial interface            | CLI                              |
| Desktop interface            | Native Rust application          |
| Editor integration           | Optional                         |
| Initial hardware             | Existing 16 GB laptop            |
| First engineering capability | Documentation                    |
| First practical project      | Vimbai                           |
| Development approach         | Specification-driven             |
| Security approach            | Capability-based, RBAC and ABAC  |
| Authorization                | Scoped, expiring and revocable   |
| Autonomy                     | Governed and verifiable          |
| Deployment                   | Native-first                     |
| Distributed computing        | Progressive expansion            |
| External services            | Optional                         |

### 95\. Immediate next steps

The next development assignment should establish the following foundational files, in order:

* `OBJECTIVES.md`

* `CONSTITUTION.md`

* `AGENTS.md`

* `ARCHITECTURE.md`

* `REQUIREMENTS.md`

* `SECURITY.md`

* `GOVERNANCE.md`

* `DEPENDENCIES.md`

* `DATA_SOVEREIGNTY.md`

* `RESOURCE_MANAGEMENT.md`

* `INTEROPERABILITY.md`

* `VERIFICATION.md`

* `MIGRATION.md`

* `ROADMAP.md`

* `CONTRIBUTING.md`

Afterward, each subsystem shall receive an independent, implementation-ready specification before its implementation begins.

### 96\. Specification limitations

This document establishes the proposed master architecture. It does not represent an exhaustive audit of the existing Tariro Studio repository, and no repository files have been modified.

The technology stack, hardware budgets, directory boundaries, API contracts and release milestones are architectural proposals requiring validation. Detailed subsystem specifications must subsequently define exact Rust interfaces, algorithms, database schemas, concurrency invariants, error variants and test cases.

Licensing, trademark registration, dependency versions and repository renaming remain unresolved.

### Final vision

Zipporah shall evolve into independent software engineering infrastructure capable of supporting human engineers, artificial intelligence agents and deterministic computational tools within a unified, persistent and governed environment.

It shall be capable of starting on a modest personal laptop and progressively expanding across private computing infrastructure without forcing users to abandon their existing repositories, tools, programming languages or ownership rights.

Zipporah — Build without boundaries.
