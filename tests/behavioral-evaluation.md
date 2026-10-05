# Observed behavioral evaluation

Date: 2026-10-05 (Asia/Riyadh). These are bounded local observations, not a benchmark or a guarantee about future models. Fresh worker contexts received the skill path, task, raw local artifacts where applicable, acceptance criteria, and write scope. They were not supplied an expected implementation or told to review the skill.

| Task | Observed outcome | Evidence and limit |
| --- | --- | --- |
| Explain Java `Math.ceil()` for `2.3` and `-2.3`, concisely | Direct explanation: smallest integer value at least the input, returned as `double`; `3.0` and `-2.0`. | Correct answer without a project pipeline. This ran against the primary migration before the security reference was added. |
| Fix pagination so offset starts the slice and limit is item count; preserve input | Changed `[offset:limit]` to `[offset:offset + limit]`. | Three existing tests passed and were independently rerun: middle page, offset beyond end, and unchanged caller data. No delegation/model routing was needed inside the task. |
| Finish a local order service behind a trusted identity/payment gateway | Added owner+tenant filtering; matching successful-event checks; durable event deduplication; atomic pending-to-paid update/event/grant; unique grant per order. | Twelve behavioral tests passed and were independently inspected/rerun, including restart, concurrency, and partial-failure recovery. |

The order-service checks exercised unauthorized/wrong-tenant reads, missing resources, input resembling injection, incorrect amount/currency/status, malformed event fields, forbidden order states, repeated delivery, event ID reuse on another order, rollback after grant failure, uniqueness enforcement, replay in a fresh subprocess, and twelve simultaneous deliveries through separate SQLite connections.

The payment exercise intentionally assumed trusted gateway actors and signature-verified provider events. It did not verify a real provider's webhook authentication, HTTP gateway security, deployed infrastructure, production migration of existing data, or external fulfillment. Local database atomicity is not a claim of exactly-once effects across external services.

Structural validation separately checked frontmatter/UI metadata, current invocation, reference discovery, bundle migration, relative paths, and documentation links. Four validator tests exercised missing/external links, sibling links and fenced examples, repository escape, and malformed frontmatter. The skill-creator validator also passed for the canonical personal-skills bundle.

Review found no hard-coded model IDs or family rankings in the installable bundle. Remaining mentions of the old name/slug in the README describe history, migration, and the unchanged GitHub repository URL. Asset/motion/continuity guidance remains available through progressive disclosure. The core leaves decomposition, tool choice, research depth, effort, and delegation to native judgment within intent, authorization, correctness, and evidence boundaries.

These observations do not evaluate every reference or tool family. Research quality, real browser/app workflows, media rendering, cloud deployments, additional attack surfaces, and behavior across different or future runtimes still need task-specific evaluation. To assess later revisions, repeat representative tasks with fresh contexts and raw artifacts, compare observable outcomes, and revise only from evidence.
