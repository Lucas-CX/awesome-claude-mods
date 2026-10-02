# Awesome Claude Mods

Practical Claude Code Mods, organized by the job they help you do, with version evidence, safety caveats, and original-author links.

[简体中文](README.zh-CN.md) · [Compatibility](docs/COMPATIBILITY.md) · [Evaluation recipes](cases/README.md) · [X demos](docs/X_SHOWCASE.md) · [Contribute](CONTRIBUTING.md)

**Review snapshot: 2026-10-02.** 19 linked examples: 3 Anthropic playground samples, 9 community selections, 4 built-in references, and 3 license-clarification candidates. We checked documentation and module entry files. **We have not installed or run these mods.** “Listed” is not a security audit or a compatibility guarantee.

## Start with a real job

- **Understand context growth:** start by reading [Token Weather](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather); compare its lightweight display with cctop below
- **Review a long editing turn:** compare Replay Theater's sequence of attempted edits with the final working-tree view in built-in diff
- **Stop switching tabs to watch a PR:** evaluate cc-pr-tracker with a low-risk test repository
- **Make architecture explanations readable:** try the supported diagram types in claude-mermaid

The three [evaluation recipes](cases/README.md) turn those ideas into repeatable checks. They are proposed experiments, not published test results.

## Watch the original X demos

Five author or official-publisher posts, grouped by the problem they illustrate. We checked post provenance and actual mod entry points; we did not reproduce the videos or test runtime behavior. Full bilingual notes: [X showcase](docs/X_SHOWCASE.md).

| Demo post | Use case | Publisher / date | Code |
| --- | --- | --- | --- |
| [Token Weather](https://x.com/ClaudeDevs/status/2105721436270993609) | Context visibility | @ClaudeDevs · 2026-10-01 | [Original source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather) |
| [Replay Theater](https://x.com/ClaudeDevs/status/2105721439206994232) | Edit review | @ClaudeDevs · 2026-10-01 | [Original source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater) |
| [Blast Radius](https://x.com/ClaudeDevs/status/2105721437701259338) | Command impact preview | @ClaudeDevs · 2026-10-01 | [Original source](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius) |
| [Mindful Claude](https://x.com/halluton/status/2099640486130835845) | Interface and waiting time | @halluton · 2026-09-14 | [Original source](https://github.com/halluton/Mindful-Claude) |
| [terminal-browser](https://x.com/RobKnight__/status/2100622380439683541) | Embedded browser and preview | @RobKnight__ · 2026-09-17 | [Original source](https://github.com/zenbu-labs/terminal-browser/tree/main/claude-code-plugin) |

The showcase adds terminal-browser as an experimental browser-in-a-pane example. It requires a separate binary and suitable terminal graphics support; see the caveats before installing. The three Anthropic samples are not supported products.

## Before installing

Current official docs set the baseline at **Claude Code 2.1.287+**, with mods enabled by default. `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` is ignored on that baseline, including when set to `0`. Older community READMEs still contain early-access instructions. Follow [current official guidance](https://code.claude.com/docs/en/plugins/mods/overview) and the project's release notes, then verify your exact version.

A mod can act with your account's permissions and consume model usage. Start in a disposable project, review capabilities, and add one mod at a time. See the [review and installation checklist](docs/COMPATIBILITY.md).

## Anthropic playground samples

These are examples published by Anthropic, **not supported Anthropic products**. Their upstream READMEs contain screenshots and build notes. License: [Apache-2.0](https://github.com/anthropics/claude-code-playground/blob/main/LICENSE).

| Mod / author | Useful for | Check before use |
| --- | --- | --- |
| [Token Weather](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather) · anthropics | A compact, per-turn context-usage display with a recent-history chart. | Full-window percentage differs from the auto-compaction threshold; updates after turns. Competes with other AbovePrompt bands. |
| [Replay Theater](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater) · anthropics | Step through edit attempts from the last editing turn. | Records attempted edits, including denied or failed ones; not proof of the final filesystem state. Diff views are truncated and session-local. |
| [Blast Radius](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius) · anthropics | Preview the impact of selected risky Bash commands and choose whether to continue. | Not a security boundary: misses wrappers and shell constructs. Migration previews load project code. Upstream says later fixes have not been re-run live; only test in disposable projects. |

## Community selections

These selections favor a clear workflow and inspectable documentation, not star counts. Each entry retains its original author. Current-runtime compatibility is untested for every entry.

### Context and session visibility

| Mod / author | Useful for | Check before use |
| --- | --- | --- |
| [cctop](https://github.com/tomstagl/cctop/tree/main/plugin) · tomstagl | A detailed dashboard for context, usage, tool activity, agents, and session state. | Hybrid mod, skills and optional native companion. Review binary installation separately; some metrics are estimates. Follow root installation docs and plugin compatibility notes. |
| [aside](https://github.com/JayDoubleu/aside) · JayDoubleu | Ask a side question about the transcript without adding it to the main conversation. | Uses model calls and the session transcript, so it can consume usage. During a running turn, a fork may reflect the previous completed turn. Read-only does not mean cost-free. |

### Review and CI

| Mod / author | Useful for | Check before use |
| --- | --- | --- |
| [cc-pr-tracker](https://github.com/sezaakgun/cc-pr-tracker) · sezaakgun | Keep selected GitHub pull requests, reviews, and required checks visible in the session. | Requires authenticated gh with repository access; polls GitHub through a process. A failed refresh can leave old values visible. |

### Interface and waiting time

| Mod / author | Useful for | Check before use |
| --- | --- | --- |
| [claude-mermaid](https://github.com/galElmalah/claude-mods/tree/main/claude-mermaid) · galElmalah | Render supported Mermaid diagrams as terminal text art inside replies. | Not all Mermaid diagram types are supported; wide art can be clipped. Original repository URL redirected to this canonical subdirectory. |
| [Mindful Claude](https://github.com/halluton/Mindful-Claude) · halluton | Show a breathing animation while a turn is running. | A UI/focus experiment; no medical-benefit claims are made here. Review conflicts with other prompt bands. |
| [cc-arcade](https://github.com/sezaakgun/cc-arcade) · sezaakgun | Play small terminal games while Claude works, with a turn-aware pause. | Needs suitable terminal input/font support. Its pet observes tool calls; presentation-only does not imply it sees no session data. |

### Workflow, cost and privacy

| Mod / author | Useful for | Check before use |
| --- | --- | --- |
| [fable-pin](https://github.com/karanb192/claude-code-mods/tree/main/plugins/fable-pin) · karanb192 | Rewrite the selected model on non-fork subagent spawns. | The bundled target is an upstream model alias: verify it exists for your account before use. Changes model selection and costs; upstream notes an error can leave a spawn unpinned. |
| [cache-tax](https://github.com/karanb192/cache-tax) · karanb192 | Warn about a cold prompt cache and optionally send bounded keep-warm model calls. | Advanced: model pings cost usage and have output-cost uncertainty. Cache lifetime must match the strategy. Do not assume savings or install alongside its classic-hook variant. |
| [secret-redactor](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/main/plugins/secret-redactor) · ray-amjad | Heuristically substitute sensitive strings before model input, with reversible tool-input placeholders. | Not a complete leakage barrier. Detection has exceptions, its memory vault resets, and restoration into tool inputs is enabled by default. Use synthetic secrets when evaluating. |

## Built-in implementation references

These ship with Claude Code. Read them to learn patterns; do not install duplicate copies by default. The [repository license](https://github.com/anthropics/claude-code/blob/main/LICENSE.md) reserves rights under Anthropic terms. Public source does not imply MIT licensing.

| Mod / author | Useful for | Check before use |
| --- | --- | --- |
| [diff](https://github.com/anthropics/claude-code/tree/main/mods/diff) · anthropics | The built-in changed-file and hunk review pane. | Built-in reference, not a separate install recommendation. Uses repository files, session context and Git. |
| [agents-md](https://github.com/anthropics/claude-code/tree/main/mods/agents-md) · anthropics | Load AGENTS.md project instructions according to the instruction-file policy. | Instruction loading varies with policy and session mode; review the upstream behavior before adapting it. |
| [sec-default](https://github.com/anthropics/claude-code/tree/main/mods/sec-default) · anthropics | Preserve organization-managed policy across user-installed mod hooks. | Administrative reference; normal user-tier loading is not equivalent to managed placement. |
| [telemetry](https://github.com/anthropics/claude-code/tree/main/mods/telemetry) · anthropics | Provide first-party analytics hooks for built-in features. | Not a general community analytics SDK or an installation suggestion; upstream restricts callers and honors analytics controls. |

## Watchlist: license clarification needed

Useful ideas, with a provenance blocker made visible. These links are for inspection; no code is copied or redistributed here.

| Mod / author | Useful for | Check before use |
| --- | --- | --- |
| [token-ledger](https://github.com/Arunjay4213/claude-mods/tree/main/plugins/token-ledger) · Arunjay4213 | A lighter cost, token, and cache-ratio ledger with per-turn history. | License clarification needed before reuse: plugin and README say MIT; root package says ISC; no license text found. Stores history locally. |
| [context-lens](https://github.com/Arunjay4213/claude-mods/tree/main/plugins/context-lens) · Arunjay4213 | Inspect context usage, composition and recent growth. | Same MIT/ISC ambiguity; explicit refresh makes token-count API requests. Treat turns-until-compaction as an estimate. |
| [gh-ci-status](https://github.com/diegorv/claude-functions-hook/tree/main/plugins/gh-ci-status) · diegorv | Show GitHub Actions and related PR links for the current repository. | No license declaration or text found. Requires authenticated gh and a GitHub remote; initial discovery failure can remain silent until reload. |

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

A reproducible example beats another promotional link. Send the original repository, the specific mod directory, the problem it solves, version evidence, license, and an honest test status. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Attribution and licensing

Independent community guide; not affiliated with or endorsed by Anthropic. Project names belong to their owners. Upstream code and media retain their own licenses, and no upstream screenshots or implementation code are bundled here. Original descriptions were written for this guide.

No collection-wide license grant is added here. Linking a project does not change its copyright or license. See the [publishing checklist](docs/PUBLISHING.md) for responsible maintenance and discovery.
