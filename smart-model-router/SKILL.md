---
name: smart-model-router
description: Route creative or software projects through suitable models, reasoning levels, research, production tools, visual implementation, and verified progress handoffs. Use for cost-aware agent teamwork, building an idea, or resuming long project work. Does not change the main chat model.
---

# Smart Model Router

Turn the user's thoughts into a completed result while spending model effort where it improves the outcome. Default to balanced quality and usage. Preserve the requested task: brainstorming stays brainstorming, and implementation follows only when requested or clearly implied. The user's ChatGPT subscription may make app features available, but this skill cannot unlock unavailable features, create an unlimited allowance, or assume paid API access.

## Work as a project team

For substantial projects, operate as a coordinator with actual specialist subagents. Read [references/project-team.md](references/project-team.md) for planning, collaboration, research, and app usage. Show the user a compact step plan with an owner, model, reasoning level, and expected result for each step. Use the current model for coordinator-owned work and label its settings as unchanged or unknown unless actually available; choose explicit pairs for delegated work.

Use relevant roles such as researcher, designer/planner, builder, and reviewer without spawning every role automatically. Let specialists contribute concrete findings and challenge material assumptions; synthesize their conclusions into a coherent project. Do not simulate a conversation among agents or expose private reasoning. Show decisions, brief rationales, progress, and artifacts instead. Tiny follow-ups can stay with the coordinator.

## Capability and scope

This skill explicitly requests delegation to subagents, with per-step model and reasoning selection, when useful and permitted by the current runtime. Use native subagent tools; do not create separate user-owned chats as a substitute.

A skill supplies instructions, not new runtime capabilities. Inspect the live tool schema and available model descriptions before routing. Select only supported model IDs and reasoning levels. Do not pretend to switch the main chat model, change global configuration, launch another CLI process, or introduce paid API services to simulate switching.

If delegation or model overrides are unavailable, state the limitation briefly and complete feasible work with the current model. Distinguish a requested model from a confirmed model; do not invent execution or usage evidence.

## Choose an economical route

Infer the intended outcome and constraints from the conversation. Ask only if missing information materially changes the deliverable. For substantial work, identify a few meaningful work units with observable acceptance criteria. Do not make a separate agent for each tool call or minor edit.

Choose based on ambiguity, dependencies, consequence of error, and ease of checking, rather than the label of the task alone:

| Work unit | Routing preference |
| --- | --- |
| Tiny answer or straightforward edit | Complete directly when delegation overhead would outweigh its benefit. |
| Bounded extraction, inventory, routine transformation, or well-specified implementation | Available lighter model; minimal sufficient supported reasoning. |
| Ordinary implementation or debugging with clear evidence | Available workhorse model; low or medium reasoning according to the actual reasoning needed. |
| Ambiguous architecture, subtle failures, consequential decisions, or difficult unresolved checks | Available stronger model or higher reasoning, with focused context and a concrete question. |

When these exact IDs are exposed by the runtime, consider `gpt-6-luna` for the lighter tier, `gpt-5.6-terra` for balanced straightforward work, `gpt-6-sol` for workhorse tasks, and `gpt-6-astra` for demanding judgment. Treat this mapping as a starting point, not a permanent catalog or proof of account availability. Terra's generation and tier labels alone do not establish that it uses less quota than Luna or Sol. If the live catalog changes, use its capability descriptions; never invent replacement IDs. When price or quota differences are unknown, call the choice a capability-based heuristic rather than a measured saving.

### Select model and reasoning together

For each substantial delegated work unit, choose an explicit `(model, reasoning effort)` pair. Pass both values through the supported spawn parameters; do not leave reasoning to inheritance or the model default. Reassess at meaningful phase boundaries rather than using one pair for the whole task.

For every model, consider the lowest supported effort likely to meet the acceptance criteria reliably. Sol Low and Sol Medium are normal choices, not exceptions. Do not equate coding, debugging, or multiple files with High effort. Select High only for a concrete reasoning burden, consequential uncertainty, or evidence that lower effort is insufficient. This is not a mandatory Low-to-Medium-to-High ladder: skip predictable failed attempts when the difficulty is already clear.

Model capability and reasoning effort are different dimensions. Low effort on a stronger model is not automatically worse than high effort on a lighter one, and effort labels are not comparable units of intelligence, latency, or cost across models. Do not assume Astra Low always beats Sol High, or that Luna Medium is always the cheapest successful route. Choose the pair most likely to satisfy this step's checks with acceptable total usage, including possible retries.

Use the following as initial routing heuristics when these model IDs and effort levels are available. They are not benchmark-proven rankings:

| Step characteristics | Candidate pair | Selection reason |
| --- | --- | --- |
| Mechanical extraction or a narrow transformation with obvious checks | Luna Low | Little inference is needed. |
| Bounded task with a few conditions, local reasoning, and easy verification | Luna Medium | Some reasoning is useful without broad synthesis. |
| Straightforward work needing a balanced model with clear checks | Terra Low or Medium, if available | Try its stated capabilities when the work is easy to verify; do not assume a measured price advantage. |
| Clear implementation or localized bug fix where Sol's capability is useful but the approach is straightforward | Sol Low | Stronger model capability can be useful without prolonged deliberation. |
| Clear but detailed task with many local conditions | Luna High or Sol Medium | Use Luna when complexity stays local; prefer Sol when requirements interact or a weaker attempt is likely to need rework. |
| Ordinary implementation spanning several components | Sol Medium | Balance coherent implementation with moderate deliberation. |
| Known goal requiring a long chain of reasoning, interacting edge cases, or difficult debugging | Sol High | The main need is deeper sustained reasoning within a reasonably clear problem. |
| Short but ambiguous decision needing broad synthesis or stronger judgment | Astra Low | The main need is model capability rather than a long reasoning chain. |
| Broad ambiguity combined with substantial dependencies or difficult tradeoffs | Astra Medium or High | Both capability and deliberation matter; prefer High when Medium is unlikely to resolve the reasoning reliably. |

These examples do not exclude other supported pairs. Use higher levels such as xhigh, max, or ultra only when a concrete difficulty justifies the extra effort or the user prioritizes that depth. Never infer price or quota multipliers from model names or effort labels.

On failure, distinguish insufficient deliberation from a capability mismatch. For a missed condition in an otherwise sound approach, consider increasing effort on the same model. For repeated conceptual errors or poor synthesis, consider a stronger model at a suitable effort. Fix missing context or inadequate evidence before changing either. After the hard decision is resolved, route routine follow-up work back to a lighter pair when the handoff is worthwhile.

Honor user preferences such as economy or quality first without requiring a mode selection. Economy favors fewer handoffs and narrowly scoped work. Quality first spends more on difficult reasoning and independent verification where failures would matter; it does not mean multiplying agents for everything.

## Creative production and tool routing

When the user wants a designed or built artifact, read [references/creative-production.md](references/creative-production.md) for reference research, image and motion work, technology selection, and production checks. Apply the parts that fit the deliverable. For visual web implementation, read [references/visual-web.md](references/visual-web.md) and its focused asset and motion references; they cover site inspection, medium selection, art direction, licensing, performance, accessibility, and rendered-site review. For creating or editing a skill, use the built-in `skill-creator` when available. Discover any other relevant installed plugin skill from the live catalog; do not depend on another personal skill being installed.

Plan in the current chat and use Plan mode only when the runtime exposes it and the task benefits from it; a skill cannot switch the app's collaboration mode. Use image generation, browser research, apps, and plugins only when their live tools are available and they materially improve the result. A requested technique such as WebGPU, Three.js, Rust, or GPU rendering should be evaluated against the artifact's needs, existing stack, compatibility, and performance, not adopted for novelty alone.

## Preserve progress across long projects

For a project likely to cross context, usage, or session limits, or when the user asks to continue earlier work, read [references/continuity.md](references/continuity.md). Create its project-local checkpoint early, update it at meaningful milestones and before an unfinished handoff, and keep the current objective, verified work, decisions, changed files, checks, and next action concise. When resuming, reconcile the checkpoint with the live workspace, Git state, user corrections, and actual results before continuing. A checkpoint does not authorize new external actions or guarantee automatic work after a usage reset. Skip checkpoint files for short self-contained tasks where a handoff adds no value.

## Delegate and integrate

Keep the coordinator's planning and synthesis short. Delegate the substantive work rather than solving it first and asking another model to repeat it. Use a small team matched to the project; run independent research, design exploration, or disjoint implementation in parallel when worthwhile. Run dependent steps in sequence and respect runtime concurrency limits. Teamwork should improve the result rather than maximize the number of agents.

Pass the goal, relevant source material or exact file paths, constraints, acceptance criteria, write ownership, and required evidence. Ask workers to report results, checks, and unresolved issues concisely. Instruct workers not to delegate further unless the coordinator assigns that explicitly.

If the available `spawn_agent` schema requires a limited history fork for a model override, use `fork_turns="none"` with a self-contained brief, or a supported small history window. Do not combine a full-history fork with unsupported model overrides. Follow the current schema if it differs.

Reuse a suitable worker for follow-ups requiring the same model-effort pair. Changing either setting requires a tool that actually supports that change or a newly spawned worker with a compact handoff. Give concurrent writers different file ownership and inspect changes before integration. Wait for required results before reporting completion.

## Check and escalate

Judge results against observable requirements: relevant tests for code, source checks for factual work, and completeness or output inspection for documents. A worker's confidence statement is not validation. Avoid repeating the full task solely to review it.

Escalate a failed reasoning or implementation step with its evidence, failed check, and previous attempt. Do not escalate missing credentials, unavailable files, or permission failures as though a stronger model would fix them. Default to one escalation per blocked work unit; after that, diagnose the remaining blocker rather than repeatedly spawning agents. Continue independent useful work when possible.

Do not reduce required correctness checks to meet a vague savings goal. Honor explicit user budgets; when a hard spend cap cannot be measured or enforced, say so before claiming to operate within it.

## Communicate honestly

For substantial tasks, give one short routing update naming the selected model and effort with a plain-language reason, for example: "Sol Low for this fix because the cause and expected behavior are clear." Report meaningful routing changes only. Finish with the deliverable and relevant verification. If routing occurred, briefly identify the model-effort pairs used and the reason for any escalation. Do not claim a percentage saving, actual cost, or quota reduction without reliable attributable measurements. Coordinator work, context handoffs, retries, and all workers add usage; routing optimizes a tradeoff and cannot guarantee savings or the best possible answer.

