# Evidence matrix

Checked on 2026-10-02 through read-only source retrieval. All entries: runtime tests not run by this guide.

| Mod | Upstream version evidence | License/provenance |
| --- | --- | --- |
| [Token Weather](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather) | Requires 2.1.287+; upstream reports live testing on 2.1.280 and validation on 2.1.285. Not retested here. | [Apache-2.0 (repository license)](https://github.com/anthropics/claude-code-playground/blob/main/LICENSE) |
| [Replay Theater](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater) | Requires 2.1.287+; upstream reports live testing on 2.1.280 and validation on 2.1.285. Not retested here. | [Apache-2.0 (repository license)](https://github.com/anthropics/claude-code-playground/blob/main/LICENSE) |
| [Blast Radius](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius) | Requires 2.1.287+; upstream reports live testing on 2.1.280 and validation on 2.1.285. Not retested here. | [Apache-2.0 (repository license)](https://github.com/anthropics/claude-code-playground/blob/main/LICENSE) |
| [cctop](https://github.com/tomstagl/cctop/tree/main/plugin) | Plugin 0.10.0 documents a 2.1.284 contract; this is upstream evidence, not a current-version guarantee. | [MIT; brand fonts have separate notices](https://github.com/tomstagl/cctop/blob/main/LICENSE) |
| [cc-pr-tracker](https://github.com/sezaakgun/cc-pr-tracker) | Upstream reports testing on 2.1.269; setup still mentions the obsolete enable flag. | [MIT](https://github.com/sezaakgun/cc-pr-tracker/blob/main/LICENSE) |
| [aside](https://github.com/JayDoubleu/aside) | Upstream reports validation and tests on 2.1.270; setup still mentions the obsolete enable flag. | [MIT](https://github.com/JayDoubleu/aside/blob/main/LICENSE) |
| [claude-mermaid](https://github.com/galElmalah/claude-mods/tree/main/claude-mermaid) | Upstream requires 2.1.270+ with old flag instructions; current compatibility untested. | [MIT](https://github.com/galElmalah/claude-mods/blob/main/LICENSE) |
| [Mindful Claude](https://github.com/halluton/Mindful-Claude) | Upstream requires 2.1.269+ with old flag instructions; current compatibility untested. | [MIT](https://github.com/halluton/Mindful-Claude/blob/main/LICENSE) |
| [cc-arcade](https://github.com/sezaakgun/cc-arcade) | Upstream requires 2.1.269+ with old flag instructions; its surface claims predate current docs. | [MIT](https://github.com/sezaakgun/cc-arcade/blob/main/LICENSE) |
| [fable-pin](https://github.com/karanb192/claude-code-mods/tree/main/plugins/fable-pin) | Upstream reports validation on 2.1.272; setup still mentions the obsolete enable flag. | [MIT (repository license)](https://github.com/karanb192/claude-code-mods/blob/main/license) |
| [cache-tax](https://github.com/karanb192/cache-tax) | Upstream reports validation on 2.1.276; setup still mentions the obsolete enable flag. | MIT (repository metadata) |
| [secret-redactor](https://github.com/ray-amjad/awesome-claude-code-function-hooks/tree/main/plugins/secret-redactor) | No numeric Claude minimum found; README retains old flag-gated setup. | [MIT](https://github.com/ray-amjad/awesome-claude-code-function-hooks/blob/main/LICENSE) |
| [diff](https://github.com/anthropics/claude-code/tree/main/mods/diff) | Built into Claude Code; inspect the copy shipped with your installed release. No current runtime test here. | [Anthropic proprietary terms; public source is not an MIT grant](https://github.com/anthropics/claude-code/blob/main/LICENSE.md) |
| [agents-md](https://github.com/anthropics/claude-code/tree/main/mods/agents-md) | Built into Claude Code; inspect the copy shipped with your installed release. No current runtime test here. | [Anthropic proprietary terms; public source is not an MIT grant](https://github.com/anthropics/claude-code/blob/main/LICENSE.md) |
| [sec-default](https://github.com/anthropics/claude-code/tree/main/mods/sec-default) | Built into Claude Code; inspect the copy shipped with your installed release. No current runtime test here. | [Anthropic proprietary terms; public source is not an MIT grant](https://github.com/anthropics/claude-code/blob/main/LICENSE.md) |
| [telemetry](https://github.com/anthropics/claude-code/tree/main/mods/telemetry) | Built into Claude Code; inspect the copy shipped with your installed release. No current runtime test here. | [Anthropic proprietary terms; public source is not an MIT grant](https://github.com/anthropics/claude-code/blob/main/LICENSE.md) |
| [token-ledger](https://github.com/Arunjay4213/claude-mods/tree/main/plugins/token-ledger) | Upstream claims 2.1.269+ with old flag instructions; current compatibility untested. | Ambiguous: MIT/ISC declarations; no license text found |
| [context-lens](https://github.com/Arunjay4213/claude-mods/tree/main/plugins/context-lens) | Root claims 2.1.269+; plugin says breakdown needs 2.1.272; old flag instructions. | Ambiguous: MIT/ISC declarations; no license text found |
| [gh-ci-status](https://github.com/diegorv/claude-functions-hook/tree/main/plugins/gh-ci-status) | Root discusses folder loading from 2.1.265, not proven current mod compatibility; old flag instructions. | No license declaration/text found |

## What was actually checked

- Canonical project or mod-directory link and README
- hooks/hooks.json with a modules entry, plus the named entry module
- License declarations or available license text; ambiguities remain explicit
- Public repository metadata where available, as a dated snapshot

Reviewed README, hooks and module blob identities are stored in data/mods.json. File identities identify reviewed content; they do not mean the full implementation was audited. No stars, download totals, uptime claims, or supported-version badges are inferred.

## Known redirects and classification corrections

- The former galElmalah/claude-mermaid repository redirects to galElmalah/claude-mods; the mod lives in its claude-mermaid directory
- mod-builder is a skill that helps create mods, not itself an executable mod entry in this collection
- cctop is a hybrid: its plugin contains a real hooks module alongside skills, and its companion binary has separate installation considerations
- Anthropic playground examples are Apache-2.0; the main Claude Code repository has different terms
- token-ledger and context-lens have conflicting license declarations; gh-ci-status lacks a found declaration. Keep these on the watchlist until clarified
