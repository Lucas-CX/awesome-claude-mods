# Mod review: harness-scope

- Review date: **2026-10-12** (Asia/Shanghai)
- Original author: **shimo4228**; self-submitted in [Issue #2](https://github.com/Lucas-CX/awesome-claude-mods/issues/2), with authorship and AI assistance disclosed.
- Original repository / mod path: [shimo4228/harness-scope](https://github.com/shimo4228/harness-scope), `plugin/`.
- Mod release / exact commit: manifest **0.1.5**, `efae82bc43c273e096130a7e0e549abf7aa1ed1a`; upstream main resolved to this commit when retrieved.
- Claude Code version: **not installed or run in this review**. Upstream minimum **2.1.287+**, reported checks on 2.1.287 and 2.1.294.
- OS / surface: source retrieval and offline catalog checks in a Linux workspace; no Claude terminal/app workflow exercised.
- Reviewer / relationship: repository owner's assistant, reviewing the author's suggestion; no authorship, maintenance or sponsorship relationship with harness-scope established.
- Review level: **`documentation-and-entry-checked`**.
- Independent mod tests: **none**. No `claude plugin validate`, installation, runtime workflow, performance benchmark or security audit.
- Decision: **include as a community workflow mod, with explicit limits and untested compatibility**.

**中文结论：符合文档与入口核验级别的收录标准，值得收录。独立运行及安全审计均未完成，不能升级为 static-validated 或 runtime-tested，也不能据作者自述宣称“安全”。**

## Job to be done and duplication check

A user with many global skills, installed plugins, agents and coding rules wants a writing or research repository to expose a smaller relevant set. The repository selects a named shared profile with `.claude/harness-scope.json`; the profile can contain allowlists or denylists for skills, agents, user instruction-file paths and tool names.

Compared all **19 baseline catalog entries** and the separate **terminal-browser** X showcase:

| Existing entry / group | Existing job | Why this is a distinct entry |
| --- | --- | --- |
| Token Weather, cctop, token-ledger, context-lens | Show context, usage or cost | harness-scope filters available capability listings rather than displaying their size. |
| aside | Side questions about a session | No shared per-repository profile selection. |
| fable-pin, cache-tax | Model pinning or cache behavior | No profile-based capability filtering. |
| secret-redactor, Blast Radius, sec-default | String redaction, command impact or managed policy | Different mechanisms; harness-scope is not a secret filter or security boundary. |
| agents-md | Load project AGENTS.md instructions | harness-scope selectively removes user instruction files; it does not replace project instruction loading. |
| Replay Theater, cc-pr-tracker, diff, gh-ci-status | Edit / PR / CI review | No overlapping configuration-scoping workflow. |
| claude-mermaid, Mindful Claude, cc-arcade, terminal-browser, telemetry | Rendering, waiting experience, browser or analytics | No overlapping workflow. |

Neither the canonical repository nor the mod directory is already listed. Upstream compares native settings such as `skillOverrides`, `enabledPlugins`, `claudeMdExcludes` and `permissions.deny`; those comparisons remain **author reports**, not independently verified product claims. The reason to choose this mod is a shared named profile with allow/deny rules across repositories.

## Inclusion criteria and primary evidence

All links below pin the reviewed commit rather than following future main-branch changes.

| Criterion | Independently checked by source inspection | Primary source |
| --- | --- | --- |
| Canonical original-author source | Public repository owned by the issue author; submission explicitly discloses authorship. | [Issue #2](https://github.com/Lucas-CX/awesome-claude-mods/issues/2), [README](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/README.md) |
| Actual mod entry | `plugin/hooks/hooks.json` declares `modules: ["./register.ts"]`; that relative file exists and exports `register(on, options)`. This is a module entry, not only a classic settings hook. | [hooks.json](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/hooks/hooks.json), [register.ts](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/hooks/register.ts) |
| Meaningful implementation | Selector/profile parsing, instruction/listing filters, agent offers, tool descriptions and tool-call refusal code are present. All four relative imports from register.ts exist. No runtime result inferred. | [profile.ts](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/hooks/profile.ts), [listing.ts](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/hooks/listing.ts), [instructions.ts](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/hooks/instructions.ts), [bundled.ts](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/hooks/bundled.ts) |
| Version assumptions | Manifest declares 0.1.5. Root README requires Claude Code 2.1.287+; historical checks are attributed below. | [plugin manifest](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/.claude-plugin/plugin.json), [README](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/README.md) |
| Installation path | Marketplace manifest maps the plugin name to `./plugin`; README documents marketplace and checkout installation. No install attempted. | [marketplace.json](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/.claude-plugin/marketplace.json), [plugin reference](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/README.md) |
| License | Manifest declares MIT; root and plugin contain matching full MIT text, copyright 2026 Tatsuya Shimomoto. | [plugin LICENSE](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/LICENSE), [root LICENSE](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/LICENSE) |
| Access / cost and test status | Local selector, user profiles and session metadata are read; no extra service account/API key documented. Normal Claude Code account/access and usage still apply. No savings claimed. | [register.ts](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/hooks/register.ts), [plugin reference](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/plugin/README.md) |

Reviewed file identities (Git blob SHA, not runtime-test hashes):

| File | Git blob SHA |
| --- | --- |
| `README.md` | `b8f9884c6d9b34bfe356ac7e4b71fbdeddfc4d21` |
| `.claude-plugin/marketplace.json` | `a2d21fbab6da9d9e79f140ecc7ee4335492fecaf` |
| `plugin/.claude-plugin/plugin.json` | `211d19dfadc65b8b84aeb7c0c5fc88303b23092c` |
| `plugin/LICENSE` | `0a21c4307bdc9edfcc490a517b6fd21ea75d301f` |
| `LICENSE` | `0a21c4307bdc9edfcc490a517b6fd21ea75d301f` |
| `plugin/hooks/hooks.json` | `21708dd26c882b7923de336b15eae3b7eef14d22` |
| `plugin/hooks/register.ts` | `279f2a964f32e67ee5122b5ca348665db3505adb` |
| `plugin/hooks/profile.ts` | `40f5b6ac00d6fb8e65c20feb27c607022e9d9b52` |
| `plugin/hooks/listing.ts` | `3ff3a240b811e8eb437885cc337a328b26122767` |
| `plugin/hooks/instructions.ts` | `f18a9ee3be9bb325e36d923248d70dfbfe264fe8` |
| `plugin/hooks/bundled.ts` | `4da697f22dd13258861f954220ccec49cb57a710` |

## What the hooks actually implement

| Source path / hook | Observed implementation | Limits |
| --- | --- | --- |
| `load`, `parseSelector`, `parseProfile` | Look for the selector at session root, then Git root; selector contains only a valid profile name. Read the user's matching profile before bundled profiles. Missing selector means off; parse/read errors yield pass-through. | A cloned repo can still select one of the user's existing profiles, including a profile that hides rules. This is not trust isolation. |
| `prompt.context` | Filter `kind: user` instruction files, including imported children; leave non-user files. | Later attachments are not filtered. If upstream rewrites instruction files into another representation, this hook passes them through. |
| `prompt.attachment` | Filter engine-origin skill listings using names/order from session usage; filter deferred tool names. Preserve project skills. | Unknown or ambiguous skill-list formats pass through; depends on Claude's listing format and metadata. Other plugin/hook text is not filtered. |
| `agent.offer` | Withhold matching agent types; preserve projectSettings agents. | Author documents a same-name project/built-in agent collision. Not independently reproduced. |
| `tool.describe`, `tool.call` | Defer filtered tools and refuse their matching calls; refuse Skill calls whose names were removed from the listing. | ToolSearch can rediscover names; direct reads of SKILL.md remain possible. |
| `classic.SessionStart`, `command.run` | Reset on clear/resume; show profile receipt and offered names via `/harness-scope` / `/harness-scope names`. | Changes require a new conversation or `/clear`. A mod that never loads cannot emit a diagnostic. |

The distributed hooks inspected here use `$.fs.exists/read`, session root/repo/usage/surfaces, command registration, UI logs/status and hook response transformations. No direct file-write, network, child-process or model-call path was observed in those five hook source files. This is **bounded source inspection**, consistent with upstream's statement, **not an independent safety audit** of Claude, the SDK, dependencies, future releases or an installed environment. Development/evaluation tools in the repository are outside this statement.

## Installation requirements and rollback

Upstream's documented command (not run here):

```bash
claude plugin install harness-scope --marketplace shimo4228/harness-scope
```

Alternatively, add `shimo4228/harness-scope` as a marketplace and install `harness-scope@harness-scope`. The marketplace source points at `./plugin`.

A repository's `.claude/harness-scope.json`:

```json
{"profile":"writing"}
```

The bundled `writing` profile keeps project skills, allows Explore/general-purpose global agents, and denies LSP, NotebookEdit, EnterWorktree and ExitWorktree. It **does not define an instructions rule**, so it does not by itself remove global coding instruction files. To filter those, the user must create a custom profile with an `instructions` rule.

Custom profiles live at `~/.claude/harness-scope/profiles/<name>.json`. The mod infers the configuration directory from an installed plugin path; a checkout loaded with `claude --plugin-dir <clone>/plugin` can use bundled profiles immediately, but needs the `configDir` setting for user profiles.

Start a new conversation or run `/clear` after choosing/editing a profile. Send one prompt, then inspect `/harness-scope` and `/harness-scope names`. Missing status in a repo that selects a profile is a signal to investigate loading, not proof that filtering is active. Remove the selector and `/clear` to disable it in that repo; upstream's global uninstall command is `claude plugin uninstall harness-scope@harness-scope`.

No extra service account or API key is documented for the mod. This does not remove Claude Code's ordinary access or model-usage requirements, and reduced listing length is not independently demonstrated cost savings.

## Author-reported results and known failures

- Root README reports checks on Claude **2.1.287** and **2.1.294**, including **1 of 9 runs not loading** on 2.1.287, with no confirmed cause.
- The [2026-10-08 readme-check record](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/docs/measurements/2026-10-08-readme-checks.md) reports **20 of 20 loads** on 2.1.294 using **plugin 0.1.2**, and discusses unchanged hooks for 0.1.3. Its 2026-10-09 appendix records a later checkout run. Neither is a 20-run independent test of reviewed 0.1.5.
- The [2026-10-08 product evaluation](https://github.com/shimo4228/harness-scope/blob/efae82bc43c273e096130a7e0e549abf7aa1ed1a/docs/measurements/2026-10-08-product-eval.md) reports improvement rounds on an older development branch. Its final pass-through dimension is **34/35**, with the author attributing a connector-tool discrepancy to connection timing. That attribution was not independently verified; do not flatten the report to “all checks passed.”
- The same evaluation says marketplace installation timing was not measured and that, at that time, the verification script's plugin test step could run zero tests because tests lived outside the plugin. The author describes separate manual test execution. This is historical author evidence, not proof that our review ran any suite.
- Direct skill-file reads, later path-scoped/subdirectory instruction attachments, ToolSearch discovery, profile reload requirements, agent name collisions and listing-format drift remain explicit limitations.

## Checks and actual results

| Check | Steps / scope | Actual result |
| --- | --- | --- |
| Source identity and entry | Retrieve pinned README, manifests, license and all five hook source files; resolve declared module and imports. | Checked; documentation-and-entry-checked only. |
| Duplicate / bilingual coverage | Compare baseline catalog/showcase; add one workflow entry and matching English/Chinese descriptions. | Distinct job; attribution preserved. |
| Offline catalog validation | `python3 scripts/validate_catalog.py` on the changed catalog; JSON parsing, duplicate IDs/URLs, source identities, bilingual coverage and relative links. | PASS: 20 unique entries. This validates the catalog, not the mod. |
| Loading / marketplace installation | Needs a named Claude Code version and synthetic repo. | **Not run**. |
| Main workflow / denied calls | Needs exact mod commit, Claude version, environment and sanitized output. | **Not run**. |
| Invalid profile / unknown listing | Source inspected; needs runtime fixtures to reproduce. | **Not run**. |
| Restart / reload / rollback | Source and upstream instructions inspected. | **Not run**. |
| Multiple mods / terminal UI / Windows | No Claude surface exercised. | **Not run**. |
| Claude validator / security audit | No `claude plugin validate` or independent security audit. | **Not run**. |

## Decision and next evidence

Include the mod at **documentation-and-entry-checked**: canonical source, executable module, concrete use case, version assumptions, install path, full license, caveats and honest test status meet CONTRIBUTING.md. No missing mandatory evidence blocks this level of inclusion.

To upgrade the status later, obtain an exact-0.1.5 (or later identified commit) Claude validator log and reproducible runtime report: Claude version, OS/surface, synthetic repo and profiles, installation route, loading status, filtered listings/refused calls, invalid-selector pass-through, clear/resume/rollback, and sanitized logs. A repeat-loading result should identify the actual plugin build and investigate the 2.1.287 non-load report. Recheck after upstream entry/version, Claude listing/API, permissions or loading behavior changes.
