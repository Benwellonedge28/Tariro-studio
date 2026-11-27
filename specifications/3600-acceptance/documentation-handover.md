# First documentation workflow handover

**ZIP-DOC-E2E-001 · v1.0 candidate · Owners** Documentation, Assignments and Verification maintainers

Implement and qualify the first Zipporah documentation workflow against a disposable repository. A one-file smoke profile exercises each handoff under a separate one-file grant. The 30-file reference profile exercises persistence and exact-count policy using synthetic files patterned on the Vimbai assignment. A live provider run uses separately authorized test-repository scope. Adding an example project to the test configuration confers no access to its repository.

## Exact handoffs

| Boundary | Required input and owner | Durable output and consumer guard |
| --- | --- | --- |
| Inspect → plan | Repository supplies stable repository ID, full base commit, tree, complete instruction bundle and exact editable path set | Assignments freezes a plan digest, named requirements and ordered units. No plan proceeds with an unchecked relevant instruction scope. |
| Author → review | Documentation receives one current unit, expected preimage, pinned source and admitted bounds | Verification checks exact staged bytes, authoritative source references and role-specific gates. A future anchor is recorded as an explicit seal obligation. |
| Review → checkpoint | Assignments receives current revision and worker epoch, accepted unit evidence and object digest | One transaction commits the verified artifact, prefix, receipt and outbox event. Uncommitted or uncertain bytes do not advance progress. |
| Recover → continue | Recovery reads the original snapshot, immutable plan, operation IDs and current authority | Reconcile old ownership and effects, verify contiguous prefix, then schedule the first unverified unit with a fresh lease. |
| Checkpoint → seal | Documentation and Verification compare every recorded unit with the actual staged tree and approved grant | Seal only the exact complete authorized diff, final-tree links and passing candidate-bound evidence. A verified short batch awaits explicit revised authority. |
| Seal → draft | Repository receives the reviewed seal and live scope, expected refs and separate stable push and PR intents | Confirm push before claiming PR creation. Reconcile a lost reply under original identity. Capture exact head, base, draft flag, effect marker and actual check IDs. |
| Draft → accept | Verification receives candidate- and commit-bound receipts and mandatory checks | Assignments may complete only when all required observations pass and no outstanding obligation remains. A published draft can exist while acceptance stays blocked. |

## Fixture execution protocol

Use [end-to-end fixtures](../../contracts/acceptance/documentation/end-to-end-fixtures.json). Prepare a dedicated bare or local disposable repository with reproducible tree contents, a checked-in nested `AGENTS.md`, source text and deterministic planned Markdown bytes. Preserve an unrelated file and an out-of-scope implementation file. Pin fixture inputs and tool/adapter versions before test start. Inject deliberate failures using adapters in a qualified harness. Reset each case to the same starting snapshot as its declared profile.

Observe state from durable sources. The fixture stage labels describe handover observations, including a sealed tree or published draft. They do not introduce new Assignment state tags. Record the authoritative Assignment state separately when gathering evidence. At document 17 kill execution after the checkpoint transaction is independently visible and before the next unit dispatch. Restore the same store, not a recreated assignment. For external response loss, have the test adapter record the successful effect before suppressing only its response. First snapshot provider observations, then assert invocation counts. An empty provider search with uncertain prior settlement must keep the original intent unresolved. For a live smoke run, use a new authorized branch, test scope and current adapter capabilities.

## Evidence and limits

The [evidence manifest](../../contracts/acceptance/documentation/evidence-manifest.schema.json) identifies the run, fixture revision, profile, environment class, owner, policy and per-case result. Reference-model, sandbox-adapter and live-provider runs are distinct. A fixture can pass when the system reports an expected denial, but record the actual system outcome separately from the test verdict. Observed passes and failures require a nonempty evidence list, structured observations and an execution receipt. Skipped and unavailable cases require reasons. Never promote a reference-model run into an end-to-end implementation result.

A release evaluator checks fixture membership, no duplicate case IDs, current revisions and artifact bytes, then compares each mandatory case with observed evidence. Implementation qualification needs an actual sandbox run of all applicable mandatory cases. Live provider behavior needs its own scoped run and receipts. Independent design approval records the reviewer and exact reviewed Git revision under [design completeness](../../DESIGN_COMPLETENESS.md).

## Remaining design decisions

The first implementation requires a qualified Rust storage adapter, approved source and review codecs, a deterministic author/reviewer test adapter and qualification of the provider's conditional or approved pre/post effect model. CLI contract and versioning decisions remain owned by the [command reference](../../documentation/cli/commands.md). The workflow can be qualified through composed service ports while the CLI is in development. Record each unresolved decision and its owner before independent sign-off.
