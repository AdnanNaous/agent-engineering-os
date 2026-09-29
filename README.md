# Smart Model Router

A Codex skill for taking a substantial creative or software goal through a short, cost-aware plan and a checked result. It recommends a model and reasoning effort for each meaningful step, coordinates available subagents, and uses research, media tools, apps, plugins, and project checkpoints when they help.

The skill includes its visual-web and continuity workflows in one folder. It can consider Luna, Terra, Sol, and Astra when those models are exposed by the current runtime. It does not switch the main chat's model or Plan mode, unlock tools, guarantee quota savings, or provide paid API access.

## Install in Codex

Ask Codex:

```text
$skill-installer Install the skill from https://github.com/AdnanNaous/smart-model-router/tree/main/smart-model-router
```

The installer places the skill under your Codex skills directory. It stops if a folder with the same name already exists. Use it in a new turn after installation.

For a manual installation, download or clone this repository, then copy the inner [`smart-model-router/`](smart-model-router/) folder to your Codex user skills directory:

| System | Destination |
| --- | --- |
| Windows | `%USERPROFILE%\.codex\skills\smart-model-router\` |
| macOS / Linux | `~/.codex/skills/smart-model-router/` |

The destination should contain `SKILL.md`, `agents/`, `references/`, and `assets/` directly. Keep those supporting directories together. Start a new Codex turn so it can discover the installed skill.

## Use it

```text
$smart-model-router Build an interactive portfolio section inspired by thoughtful game environments. Research references, choose an efficient model and reasoning level for each step, implement it, and inspect the result.
```

```text
$smart-model-router Continue my project from its checkpoint, verify the current files, and finish the remaining work.
```

The router only uses models and tools actually available in the running session. When subagent model selection is unavailable, it can still plan and work with the current model, but cannot execute a model switch. A proposed route is not a measured cost saving.

## Use with ChatGPT or another AI

Publishing this repository does not automatically install it into ChatGPT or another assistant. If your product exposes skill upload, package the inner `smart-model-router/` folder as a ZIP with that folder at the top level and upload it through the product's Skills interface. Availability and supported tools vary by product and account. If skill upload is unavailable, provide [`SKILL.md`](smart-model-router/SKILL.md) and the relevant reference files in a conversation as instructions; model switching and agent delegation will only work if that environment provides those controls.

For developers building an agent with OpenAI APIs, follow the [official skills documentation](https://developers.openai.com/api/docs/guides/tools-skills) for the skill-loading method supported by that runtime. API usage is separate from a ChatGPT subscription.

## Contents

- [`SKILL.md`](smart-model-router/SKILL.md): routing, model and effort selection, delegation, and links to focused workflows.
- [`references/creative-production.md`](smart-model-router/references/creative-production.md): research, inspiration, media, and technology choices.
- [`references/visual-web.md`](smart-model-router/references/visual-web.md): visual web production and rendered-site review.
- [`references/continuity.md`](smart-model-router/references/continuity.md): checkpoint and resume procedure.
- [`assets/STATE_TEMPLATE.md`](smart-model-router/assets/STATE_TEMPLATE.md): project checkpoint template.

