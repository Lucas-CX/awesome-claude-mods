# Awesome Claude Mods

Find a Claude Code Mod for the job in front of you: see context growth, review edit attempts, or preview a website beside your conversation. Original sources, author demos, version evidence, and practical caveats in one guide.

[简体中文](README.zh-CN.md) · [Choose by task](#choose-by-task) · [Watch demos](#watch-two-demos-here) · [First steps](#before-installing) · [Evidence](docs/EVIDENCE.md) · [Contribute](#contribute-a-useful-result)

![Awesome Claude Mods: a community guide to context monitoring, edit replay, and browser preview. Original concept previews, not runtime screenshots.](assets/cover.jpg)

**Review snapshot: 2026-10-02.** 19 catalog entries: 3 [Anthropic playground samples](#anthropic-playground-samples), 9 [community selections](#community-selections), 4 [built-in references](#built-in-implementation-references), and 3 [license-clarification candidates](#watchlist-license-clarification-needed). The X showcase adds terminal-browser, for 20 distinct mods overall. Only 5 have verified demo / announcement posts; the 19 catalog entries are not 19 installation recommendations. We checked documentation and module entry files. **We have not installed or run these mods.** “Listed” is not a security audit or a compatibility guarantee.

## Choose by task

| I want to… | Start here |
| --- | --- |
| See context growth or session usage | [Token Weather](#token-weather--anthropics) (sample) · [cctop](#cctop--tomstagl) (community) |
| Review edits or follow PR checks | [Replay Theater](#replay-theater--anthropics) (sample) · [cc-pr-tracker](#cc-pr-tracker--sezaakgun) (community) |
| Preview a website or read diagrams | [terminal-browser](#terminal-browser--a-browser-inside-claude-code) (showcase) · [claude-mermaid](#claude-mermaid--galelmalah) (community) |
| Change the waiting experience | [Mindful Claude](#mindful-claude--halluton) · [cc-arcade](#cc-arcade--sezaakgun) (community) |
| Explore model, cache, or privacy behavior | [Workflow, cost and privacy](#workflow-cost-and-privacy) (advanced experiments) |
| Build my own mod | [Official authoring and test docs](#build-your-own) · [Built-in implementation references](#built-in-implementation-references) |

New to Mods? Follow the [three first-use steps](#before-installing). The links above lead to requirements and caveats, not a one-click install list.

## Watch two demos here

Press play without leaving this README. These players use the authors' original GitHub-hosted uploads; GitHub may start them muted.

### terminal-browser · a browser inside Claude Code

Open a real browser in a Claude Code pane. **Author:** zenbu-labs / @RobKnight__. [Upstream demo and setup](https://github.com/zenbu-labs/terminal-browser/blob/main/claude-code-plugin/README.md) · [Open original video](https://github.com/user-attachments/assets/a79e7667-6fcb-49a4-9967-44d0f942102c).

https://github.com/user-attachments/assets/a79e7667-6fcb-49a4-9967-44d0f942102c

**Before trying:** Experimental; requires a separate binary and a suitable kitty-graphics terminal. See the upstream limitations.

### One sentence. One plugin. · build a masking hook

A short case study from the original Mods proposal: Claude writes, validates and loads a hook that masks secrets in tool output before the model reads it. **Author:** [@poteat](https://github.com/poteat). [Original proposal and demo](https://github.com/anthropics/claude-code/issues/91870) · [Open original video](https://github.com/user-attachments/assets/44601a4e-a4b4-4e0b-b1d2-4621293b8150).

https://github.com/user-attachments/assets/44601a4e-a4b4-4e0b-b1d2-4621293b8150

**Context:** Recorded for the September 3, 2026 proposal. This early prototype illustrates the mechanism; it is not a current installation guide or a complete privacy guarantee.

## Three places to start

Pick a workflow, watch the original demo, then read the source and caveats before trying it.

### 1. See context growth at a glance

**Token Weather** · anthropics

A compact context gauge with recent-turn history.

[Original source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather) · [Publisher demo](https://x.com/ClaudeDevs/status/2105721436270993609)

**Before trying:** Updates after turns. Its full-window percentage differs from the auto-compaction threshold.

### 2. Understand how a change unfolded

**Replay Theater** · anthropics

Step through the last editing turn, one attempted edit at a time.

[Original source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater) · [Publisher demo](https://x.com/ClaudeDevs/status/2105721439206994232)

**Before trying:** Includes denied or failed attempts; displayed diffs are truncated. Check the final Git diff too.

### 3. Preview a website beside the conversation

**terminal-browser** · zenbu-labs / @RobKnight__

Open a real browser inside a Claude Code pane.

[Original source](https://github.com/zenbu-labs/terminal-browser/tree/main/claude-code-plugin) · [Author demo](https://x.com/RobKnight__/status/2100622380439683541)

**Before trying:** Experimental. Requires a separate binary and kitty graphics support with Unicode placeholders; multiplexer and layout limits apply.

Token Weather and Replay Theater are Anthropic-published teaching samples, **not supported products**. terminal-browser is a separate community experiment featured in the [X showcase](docs/X_SHOWCASE.md).

The three [evaluation recipes](cases/README.md) turn workflow ideas into repeatable checks. They are proposed experiments, not published test results.

## Watch the original X demos

Five author or official-publisher posts, grouped by the problem they illustrate. We checked post provenance and actual mod entry points; we did not reproduce the videos or test runtime behavior. Full bilingual notes: [X showcase](docs/X_SHOWCASE.md).

- **Token Weather** · Context visibility: [original post](https://x.com/ClaudeDevs/status/2105721436270993609) (@ClaudeDevs, 2026-10-01) · [source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather)
- **Replay Theater** · Edit review: [original post](https://x.com/ClaudeDevs/status/2105721439206994232) (@ClaudeDevs, 2026-10-01) · [source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater)
- **Blast Radius** · Command impact preview: [original post](https://x.com/ClaudeDevs/status/2105721437701259338) (@ClaudeDevs, 2026-10-01) · [source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius)
- **Mindful Claude** · Interface and waiting time: [original post](https://x.com/halluton/status/2099640486130835845) (@halluton, 2026-09-14) · [source](https://github.com/halluton/Mindful-Claude)
- **terminal-browser** · Embedded browser and preview: [original post](https://x.com/RobKnight__/status/2100622380439683541) (@RobKnight__, 2026-09-17) · [source](https://github.com/zenbu-labs/terminal-browser/tree/main/claude-code-plugin)

The showcase adds terminal-browser as an experimental browser-in-a-pane example. It requires a separate binary and suitable terminal graphics support; see the caveats before installing. The three Anthropic samples are not supported products.

## Before installing

As of the review snapshot, official docs set the baseline at **Claude Code 2.1.287+**, with mods enabled by default. `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` is ignored on that baseline, including when set to `0`. Older community READMEs still contain early-access instructions. Follow [current official guidance](https://code.claude.com/docs/en/plugins/mods/overview) and the project's release notes, then verify your exact version.

1. **Choose one workflow.** Use the [task chooser](#choose-by-task), inspect the entry's caveats, and watch an original demo if available.
2. **Check before installing.** Compare your exact Claude Code version, terminal, dependencies, permissions, and license with the [compatibility checklist](docs/COMPATIBILITY.md) and upstream setup instructions. A mod can act with your account's permissions and consume model usage.
3. **Evaluate one mod in a disposable project.** Use an [evaluation recipe](cases/README.md), check the result yourself, and keep upstream disable/uninstall instructions handy. Record your version and outcome with the [review template](docs/REVIEW_TEMPLATE.md); these recipes are not completed test reports.

## Anthropic playground samples

These are examples published by Anthropic, **not supported Anthropic products**. Their upstream READMEs contain screenshots and build notes. License: [Apache-2.0](https://github.com/anthropics/claude-code-playground/blob/main/LICENSE).

Every entry below uses the same format: what it does, use case, requirements / limits, source / setup, and demo status. **No entry has been runtime-tested by this guide.**

### Token Weather · anthropics

- **What it does:** A compact, per-turn context-usage display with a recent-history chart.
- **Use case:** Notice context growth during a long conversation.
- **Requirements / limits:** Full-window percentage differs from the auto-compaction threshold; updates after turns. Competes with other AbovePrompt bands.
- **Links:** [Source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather) · [Upstream docs / setup](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/token-weather/README.md) · Demo: [Verified original post](https://x.com/ClaudeDevs/status/2105721436270993609)

### Replay Theater · anthropics

- **What it does:** Step through edit attempts from the last editing turn.
- **Use case:** Understand an editing turn before reviewing the final Git diff.
- **Requirements / limits:** Records attempted edits, including denied or failed ones; not proof of the final filesystem state. Diff views are truncated and session-local.
- **Links:** [Source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater) · [Upstream docs / setup](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/replay-theater/README.md) · Demo: [Verified original post](https://x.com/ClaudeDevs/status/2105721439206994232)

### Blast Radius · anthropics

- **What it does:** Preview the impact of selected risky Bash commands and choose whether to continue.
- **Use case:** Study a human decision step before selected risky commands.
- **Requirements / limits:** Not a security boundary: misses wrappers and shell constructs. Migration previews load project code. Upstream says later fixes have not been re-run live; only test in disposable projects.
- **Links:** [Source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius) · [Upstream docs / setup](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/blast-radius/README.md) · Demo: [Verified original post](https://x.com/ClaudeDevs/status/2105721437701259338)

## Community selections

These selections favor a clear workflow and inspectable documentation, not star counts. Each entry retains its original author. Current-runtime compatibility is untested for every entry.

### Context and session visibility

#### cctop · tomstagl

- **What it does:** A detailed dashboard for context, usage, tool activity, agents, and session state.
- **Use case:** Monitor an active coding session without switching dashboards.
- **Requirements / limits:** The basic context/cost/rate-limit pane works without the native companion; the fuller tool, file, agent and Advisor dashboard needs it. Review binary installation separately; some metrics are estimates. Follow root installation docs and plugin compatibility notes.
- **Links:** [Source](https://github.com/tomstagl/cctop/tree/main/plugin) · [Upstream docs / setup](https://github.com/tomstagl/cctop/blob/main/plugin/README.md) · [Companion setup](https://github.com/tomstagl/cctop) · Demo: No demo post verified by this guide

#### aside · JayDoubleu

- **What it does:** Ask a side question about the transcript without adding it to the main conversation.
- **Use case:** Clarify something in the transcript without interrupting the main thread.
- **Requirements / limits:** Uses model calls and the session transcript, so it can consume usage. During a running turn, a fork may reflect the previous completed turn. Read-only does not mean cost-free.
- **Links:** [Source](https://github.com/JayDoubleu/aside) · [Upstream docs / setup](https://github.com/JayDoubleu/aside/blob/main/README.md) · Demo: No demo post verified by this guide

### Review and CI

#### cc-pr-tracker · sezaakgun

- **What it does:** Keep selected GitHub pull requests, reviews, and required checks visible in the session.
- **Use case:** Keep PR reviews and required checks in view while coding.
- **Requirements / limits:** Requires authenticated gh with repository access; polls GitHub through a process. A failed refresh can leave old values visible.
- **Links:** [Source](https://github.com/sezaakgun/cc-pr-tracker) · [Upstream docs / setup](https://github.com/sezaakgun/cc-pr-tracker/blob/main/README.md) · Demo: No demo post verified by this guide

### Interface and waiting time

#### claude-mermaid · galElmalah

- **What it does:** Render supported Mermaid diagrams as terminal text art inside replies.
- **Use case:** Read supported workflow and architecture diagrams in the terminal.
- **Requirements / limits:** Not all Mermaid diagram types are supported; wide art can be clipped. Original repository URL redirected to this canonical subdirectory.
- **Links:** [Source](https://github.com/galElmalah/claude-mods/tree/main/claude-mermaid) · [Upstream docs / setup](https://github.com/galElmalah/claude-mods/blob/main/claude-mermaid/README.md) · Demo: No demo post verified by this guide

#### Mindful Claude · halluton

- **What it does:** Show a breathing animation while a turn is running.
- **Use case:** Add a quiet visual rhythm during a running turn.
- **Requirements / limits:** A UI/focus experiment; no medical-benefit claims are made here. Review conflicts with other prompt bands.
- **Links:** [Source](https://github.com/halluton/Mindful-Claude) · [Upstream docs / setup](https://github.com/halluton/Mindful-Claude/blob/main/README.md) · Demo: [Verified original post](https://x.com/halluton/status/2099640486130835845)

#### cc-arcade · sezaakgun

- **What it does:** Play small terminal games while Claude works, with a turn-aware pause.
- **Use case:** Pass waiting time with turn-aware terminal games.
- **Requirements / limits:** Needs suitable terminal input/font support. Its pet observes tool calls; presentation-only does not imply it sees no session data.
- **Links:** [Source](https://github.com/sezaakgun/cc-arcade) · [Upstream docs / setup](https://github.com/sezaakgun/cc-arcade/blob/main/README.md) · Demo: No demo post verified by this guide

### Workflow, cost and privacy

#### fable-pin · karanb192

- **What it does:** Rewrite the selected model on non-fork subagent spawns.
- **Use case:** Keep non-fork subagents on a chosen model target.
- **Requirements / limits:** The bundled target is an upstream model alias: verify it exists for your account before use. Changes model selection and costs; upstream notes an error can leave a spawn unpinned.
- **Links:** [Source](https://github.com/karanb192/claude-code-mods/tree/main/plugins/fable-pin) · [Upstream docs / setup](https://github.com/karanb192/claude-code-mods/blob/main/plugins/fable-pin/README.md) · Demo: No demo post verified by this guide

#### cache-tax · karanb192

- **What it does:** Warn about a cold prompt cache and optionally send bounded keep-warm model calls.
- **Use case:** Inspect cache-related usage and experiment with keep-warm behavior.
- **Requirements / limits:** Advanced: model pings cost usage and have output-cost uncertainty. Cache lifetime must match the strategy. Do not assume savings or install alongside its classic-hook variant.
- **Links:** [Source](https://github.com/karanb192/cache-tax) · [Upstream docs / setup](https://github.com/karanb192/cache-tax/blob/main/README.md) · Demo: No demo post verified by this guide

#### secret-redactor · ray-amjad

- **What it does:** Heuristically substitute sensitive strings before model input, with reversible tool-input placeholders.
- **Use case:** Experiment with masking synthetic sensitive strings before model input.
- **Requirements / limits:** Not a complete leakage barrier. Detection has exceptions, its memory vault resets, and restoration into tool inputs is enabled by default. Use synthetic secrets when evaluating.
- **Links:** [Source](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/main/plugins/secret-redactor) · [Upstream docs / setup](https://github.com/ray-amjad/awesome-claude-code-function-hooks/blob/main/plugins/secret-redactor/README.md) · Demo: No demo post verified by this guide

## Built-in implementation references

These ship with Claude Code. Read them to learn patterns; **do not install duplicate copies by default**. The [repository license](https://github.com/anthropics/claude-code/blob/main/LICENSE.md) reserves rights under Anthropic terms. Public source does not imply MIT licensing.

### diff · anthropics

- **What it does:** The built-in changed-file and hunk review pane.
- **Use case:** Learn the built-in Git-backed review-pane implementation.
- **Requirements / limits:** Built-in reference, not a separate install recommendation. Uses repository files, session context and Git.
- **Links:** [Source](https://github.com/anthropics/claude-code/tree/main/mods/diff) · [Implementation docs](https://github.com/anthropics/claude-code/blob/main/mods/diff/README.md) · Demo: No demo post verified by this guide

### agents-md · anthropics

- **What it does:** Load AGENTS.md project instructions according to the instruction-file policy.
- **Use case:** Learn instruction-file loading and precedence.
- **Requirements / limits:** Instruction loading varies with policy and session mode; review the upstream behavior before adapting it.
- **Links:** [Source](https://github.com/anthropics/claude-code/tree/main/mods/agents-md) · [Implementation docs](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md) · Demo: No demo post verified by this guide

### sec-default · anthropics

- **What it does:** Preserve organization-managed policy across user-installed mod hooks.
- **Use case:** Study organization-managed mod policy boundaries.
- **Requirements / limits:** Administrative reference; normal user-tier loading is not equivalent to managed placement.
- **Links:** [Source](https://github.com/anthropics/claude-code/tree/main/mods/sec-default) · [Implementation docs](https://github.com/anthropics/claude-code/blob/main/mods/sec-default/README.md) · Demo: No demo post verified by this guide

### telemetry · anthropics

- **What it does:** Provide first-party analytics hooks for built-in features.
- **Use case:** Study first-party event contracts and batching.
- **Requirements / limits:** Not a general community analytics SDK or an installation suggestion; upstream restricts callers and honors analytics controls.
- **Links:** [Source](https://github.com/anthropics/claude-code/tree/main/mods/telemetry) · [Implementation docs](https://github.com/anthropics/claude-code/blob/main/mods/telemetry/README.md) · Demo: No demo post verified by this guide

## Watchlist: license clarification needed

Separate from community selections: these are **inspection links, not installation recommendations**. No upstream code is copied or redistributed here.

### token-ledger · Arunjay4213

- **What it does:** A lighter cost, token, and cache-ratio ledger with per-turn history.
- **Use case:** Research a lightweight alternative to a full usage dashboard.
- **Requirements / limits:** License clarification needed before reuse: plugin and README say MIT; root package says ISC; no license text found. Stores history locally.
- **Links:** [Source](https://github.com/Arunjay4213/claude-mods/tree/main/plugins/token-ledger) · [Upstream docs / setup](https://github.com/Arunjay4213/claude-mods/blob/main/plugins/token-ledger/README.md) · Demo: No demo post verified by this guide

### context-lens · Arunjay4213

- **What it does:** Inspect context usage, composition and recent growth.
- **Use case:** Research a more detailed view of context composition.
- **Requirements / limits:** Same MIT/ISC ambiguity; explicit refresh makes token-count API requests. Treat turns-until-compaction as an estimate.
- **Links:** [Source](https://github.com/Arunjay4213/claude-mods/tree/main/plugins/context-lens) · [Upstream docs / setup](https://github.com/Arunjay4213/claude-mods/blob/main/plugins/context-lens/README.md) · Demo: No demo post verified by this guide

### gh-ci-status · diegorv

- **What it does:** Show GitHub Actions and related PR links for the current repository.
- **Use case:** Research a compact current-repository CI indicator.
- **Requirements / limits:** No license declaration or text found. Requires authenticated gh and a GitHub remote; initial discovery failure can remain silent until reload.
- **Links:** [Source](https://github.com/diegorv/claude-functions-hook/tree/main/plugins/gh-ci-status) · [Upstream docs / setup](https://github.com/diegorv/claude-functions-hook/blob/main/README.md) · Demo: No demo post verified by this guide

## Version and license evidence

The [version and license matrix](docs/EVIDENCE.md) records upstream claims separately from our checks. [data/mods.json](data/mods.json) also stores reviewed file identities so a later review can detect source changes. A recent repository push does not prove that an individual mod is maintained or works on a new release.

## Build your own

- [Official overview](https://code.claude.com/docs/en/plugins/mods/overview): capabilities and trust
- [Create a mod](https://code.claude.com/docs/en/plugins/mods/create): the authoring loop
- [Test a mod](https://code.claude.com/docs/en/plugins/mods/test): the official test kit
- [Troubleshoot a mod](https://code.claude.com/docs/en/plugins/mods/troubleshoot): loading and failure diagnosis

A mod is a plugin containing executable function hooks. A skill is an instruction file, a settings hook is a configured lifecycle action, and an MCP server supplies external tools. A plugin can bundle several of these. This guide lists actual mod entry points; helper skills and broader directories stay in the next section.

## Related projects and credit

- [karanb192/awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods): a broader discovery catalog and capability-footprint scanner; useful for finding more candidates
- [karanb192/claude-code-mods](https://github.com/karanb192/claude-code-mods): a marketplace that includes a mod-builder **skill** as well as actual mods

These helped discovery. This guide independently checks selected upstream links and adds workflow selection, compatibility caveats, and evaluation recipes. It does not mirror their catalog or reproduce their scanner's grades as our own results.

## Contribute a useful result

- [Suggest a mod](https://github.com/Lucas-CX/awesome-claude-mods/issues/new?template=suggest-mod.yml): a source link and a concrete use case are enough to start; say what is still unknown.
- [Report a broken link, outdated claim, or compatibility result](https://github.com/Lucas-CX/awesome-claude-mods/issues/new?template=report-correction.yml): include the affected entry and evidence for the correction.
- Ready to edit? Follow [CONTRIBUTING.md](CONTRIBUTING.md) for a focused pull request.

You do not need to install a mod or translate both READMEs to open an issue. Distinguish upstream claims from checks you actually ran, and use only sanitized or synthetic examples.

## Attribution and licensing

Independent community guide; not affiliated with or endorsed by Anthropic. Project names belong to their owners. Upstream code and media retain their own licenses, and no upstream screenshots or implementation code are bundled here. Original descriptions were written for this guide.

No collection-wide license grant is added here. Linking a project does not change its copyright or license. See the [publishing checklist](docs/PUBLISHING.md) for responsible maintenance and discovery.
