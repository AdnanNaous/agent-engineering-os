# Agent Engineering OS

Agent Engineering OS is a capability-first skill for turning goals into verified work. It combines research, software engineering, computer/app operation, creative production, and project continuity in environments that expose those capabilities.

It evolved from Smart Model Router. Model selection is now an optional optimization inside the work, rather than the organizing principle. The current model retains responsibility for reasoning, decomposition, architecture, research depth, tools, and verification.

## Why it exists

A durable skill should define useful outcomes, authorization boundaries, evidence standards, and continuity without freezing an advanced model into yesterday's methods. Agent Engineering OS uses live runtime capabilities and permits newer mechanisms to supersede the examples in its documentation.

It does not promise that instructions can eliminate all performance constraints. Its design avoids fixed model hierarchies, reasoning ladders, mandatory agent pipelines, and compulsory routing tables.

## Architecture

```mermaid
flowchart TD
    Goal["User intent and outcome"] --> Context["Relevant context and live capabilities"]
    Context --> Compose["Adaptive orchestration and native judgment"]
    Compose --> Work["Research, engineer, operate, or create"]
    Work --> Evidence["Observe and verify"]
    Evidence --> Work
    Evidence --> Result["Deliver the supported result"]
    Work -.-> State["Concise continuity state"]
    State -.-> Context
```

The diagram describes relationships, not a required pipeline. A simple stable question can receive a direct answer. A repository fix can involve inspection, implementation, and focused tests. A larger product can combine source research, engineering, app operation, and rendered QA.

## Capabilities

- **Research:** retrieve and inspect relevant sources, evaluate quality and disagreements, synthesize with citations, and expose material uncertainty.
- **Engineering:** understand actual repositories, implement requested changes, run appropriate checks, debug failures, and verify affected behavior.
- **Computer and app work:** operate available files, terminals, browsers, connected apps, or cloud environments and inspect resulting state.
- **Creative production:** preserve coherent visual direction, use appropriate media, track asset provenance, optimize performance, and inspect desktop/mobile output and motion.
- **Collaboration:** use real subagents or parallel work when independence, specialist context, or verification makes it worthwhile.
- **Continuity:** resume from compact evidence-backed checkpoints reconciled with live files and operations.

These are composable capabilities, not mandatory stages. The reference files are loaded only when useful.

## Install

The installable bundle is [agent-engineering-os/](agent-engineering-os/). Keep its `SKILL.md`, `agents/`, `references/`, and `assets/` together.

For a Codex environment with a supported skill installer, ask it to install the inner folder from this repository:

```text
Install the skill from https://github.com/AdnanNaous/smart-model-router/tree/main/agent-engineering-os
```

For manual installation into a Codex user-skills directory:

| Environment | Destination |
| --- | --- |
| Windows | `%USERPROFILE%\.codex\skills\agent-engineering-os\` |
| macOS / Linux | `~/.codex/skills/agent-engineering-os/` |

Follow your runtime's current skill discovery instructions. In ChatGPT environments that support personal skills, use the supported creation/import interface; publishing on GitHub alone does not install a skill. If skill loading is unavailable, provide `SKILL.md` and the relevant supporting references as instructions, with capabilities limited to that environment.

### Migration

Replace an existing local `smart-model-router` installation with the new bundle, preserving any personal modifications first. Avoid keeping both active unless you intentionally want overlapping triggers. This release changes the skill slug, UI metadata, examples, and folder links; Git history remains in the same repository.

The repository URL retains its existing slug unless it is separately renamed through supported GitHub administration tooling. The installable skill slug is `agent-engineering-os`.

## Examples

```text
$agent-engineering-os Fix the failing checkout flow in this repository.
Inspect the cause, implement the fix, and verify the affected behavior.
```

```text
$agent-engineering-os Compare current options for this architecture using
primary sources, then implement the appropriate choice in the existing app.
```

```text
$agent-engineering-os Repair the mobile layout and motion in my portfolio.
Preserve its identity and inspect the rendered result.
```

```text
$agent-engineering-os Continue from this project's checkpoint.
Reconcile it with the current files and finish the remaining authorized work.
```

You can initiate work from a phone/chat conversation. Actual execution uses available environments and tools; the skill does not create an automatic transfer to another computer, chat, or coding runtime.

## Bundle

| File | Purpose |
| --- | --- |
| [SKILL.md](agent-engineering-os/SKILL.md) | Compact operating principles and reference activation |
| [agents/openai.yaml](agent-engineering-os/agents/openai.yaml) | UI metadata and invocation example |
| [capability-orchestration.md](agent-engineering-os/references/capability-orchestration.md) | Live discovery, optional routing, portability |
| [research.md](agent-engineering-os/references/research.md) | Evidence quality, contradictions, citations |
| [software-engineering.md](agent-engineering-os/references/software-engineering.md) | Implementation, debugging, AI-agent systems, delivery |
| [computer-work.md](agent-engineering-os/references/computer-work.md) | Environment/app execution and final-state verification |
| [project-team.md](agent-engineering-os/references/project-team.md) | Useful delegation and integration |
| [continuity.md](agent-engineering-os/references/continuity.md) | Checkpoint and resumption |
| [creative-production.md](agent-engineering-os/references/creative-production.md) | Creative research and production |
| [visual-web.md](agent-engineering-os/references/visual-web.md) | Visual website implementation and inspection |
| [visual-assets-and-performance.md](agent-engineering-os/references/visual-assets-and-performance.md) | Asset provenance, optimization, rendering budgets |
| [visual-motion-and-review.md](agent-engineering-os/references/visual-motion-and-review.md) | Motion construction and observed review |
| [STATE_TEMPLATE.md](agent-engineering-os/assets/STATE_TEMPLATE.md) | Compact handoff template |

## Validation

Run `python3 tools/validate_skill.py` from the repository root to check metadata, bundle paths, invocation coherence, and relative documentation links. Run `python3 -m unittest discover -s tests` for the validator's failure cases. The validation tooling requires PyYAML (`python3 -m pip install PyYAML`) if your environment does not already provide it.

Structural checks cannot prove future model behavior, security, or successful task completion. Behavioral evaluation still requires realistic tasks and observed results. Changes should be reviewed for unnecessary prescriptions as well as correctness.

## Limits

A skill supplies instructions, not new capabilities or permissions. It cannot unlock apps, select unexposed models, change the main chat model without controls, access an unrelated device, guarantee persistence, bypass quotas, or provide paid API usage through a subscription.

Tools, access, model controls, and skill-loading support vary by runtime. Missing capabilities should produce a precise limitation and useful partial progress. Claims of execution, verification, cost, or savings require actual evidence. No skill guarantees that all code is correct or that every future model will behave identically.
