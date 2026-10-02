# Three evaluation recipes

These are original proposed workflows for this guide. **They have not been executed.** Run only after reviewing a mod, in a disposable project. Capture exact versions and sanitized evidence with the [review template](../docs/REVIEW_TEMPLATE.md).

## 1. Choose a context display

Candidates: [Token Weather](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather) and [cctop](https://github.com/tomstagl/cctop/tree/main/plugin).

**Question:** Is a one-line context indicator enough, or do you need a full dashboard?

1. Use a small synthetic repository, one mod at a time, with the same Claude model and a comparable starting state.
2. Ask Claude to inspect a small file, then several larger files. Record displayed usage after each completed turn.
3. Compare with Claude's own usage display, keeping full-window percentage distinct from the compaction threshold.
4. Restart and narrow the terminal. Check what resets, what remains visible, and whether errors are understandable.

**Useful result:** a short comparison of clarity, update timing, space used, setup overhead, and discrepancies. Do not claim token savings from a display alone.

## 2. Review editing intent versus final state

Candidates: [Replay Theater](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater) and [built-in diff](https://github.com/anthropics/claude-code/tree/main/mods/diff).

**Question:** Does a sequence of edit attempts help you understand changes faster than a final diff?

1. Start with a clean disposable Git repository containing a tiny, local example.
2. Ask for one rename across a few files. Open `/replay`, then compare with `/diff` and the actual file contents.
3. Include an intentionally declined edit and verify whether replay labels or displays it. The upstream says denied/failed attempts can appear.
4. Check a no-edit turn, the next editing turn, and session restart. Record which history remains.

**Useful result:** where replay explains chronology and where final-state checks are still necessary. Do not present attempted edits as successful changes.

## 3. Watch a PR without leaving the session

Candidate: [cc-pr-tracker](https://github.com/sezaakgun/cc-pr-tracker).

**Question:** Can the status line reliably tell you when this specific PR needs attention?

1. Use a PR you can already read in a low-risk test repository and an appropriately authorized `gh` login. Confirm access before loading the mod.
2. Watch the PR and compare its review/required-check state with GitHub's own page.
3. Observe an ordinary CI state change when one occurs. Do not merge, push, or change protection merely to produce a demo.
4. Check how missing access or a failed refresh is represented; distinguish stale data from a genuinely clean PR.
5. Restart and verify whether watched PRs persist, then stop watching.

**Useful result:** state accuracy, alert delay, failure clarity, and what the reader must set up. Record API/CLI dependencies and avoid exposing private PR titles or repository names.
