# Publish a credible starter, then earn discovery

Publication checklist for the owner. A checklist item is not evidence that an action has been completed.

## Before publishing an update

- Target: `Lucas-CX/awesome-claude-mods`, public. Verify the pushed commit and rendered README before announcing an update
- No collection-wide license is granted without the owner choosing one. Upstream code/media keep their own terms
- Check that no draft-only claims or unverified live URLs remain
- Keep the three unresolved-license candidates in the watchlist, or omit them from the first public release
- Run the local catalog check and recheck high-priority upstream URLs on publication day
- Prefer a small honest release with zero runtime-tested claims over an invented test badge

## GitHub discovery setup

Suggested description:

> Practical Claude Code Mods: curated use cases, compatibility evidence, safety notes, and reproducible evaluation recipes. English / 中文.

Suggested relevant topics: `claude-code`, `claude-mods`, `claude-code-plugin`, `function-hooks`, `developer-tools`.

Keep the main README in English and the Chinese version one click away. Put a clear use-case summary in the first screen. Do not add unrelated keywords, fake stars, paid-star schemes, copied “awesome” badges, or unsolicited mass promotion.

## The first genuinely distinctive content

1. Run and publish one exact-version evaluation of Token Weather, Replay Theater, or cc-pr-tracker
2. Capture your own short GIF or screenshots from a synthetic project, label the version, and show one limitation as well as the success
3. Publish a concise comparison with a takeaway a reader can use immediately
4. Share it once in an appropriate community where self-promotion is allowed, identifying your involvement and crediting the original authors

## What we adapted from established resource lists

Reviewed on 2026-10-03. These are observable publishing patterns, not proof that a layout or post caused star growth.

- **Task-first navigation:** [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) offers a starting path and task categories; [awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods) groups mods by the job they do. Our bilingual task chooser now links directly to existing entries while keeping samples, community projects, references, and the watchlist distinct.
- **A short path to useful evidence:** [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) puts runnable examples and categories up front; [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills/blob/main/CONTRIBUTING.md) asks for concise, categorized contributions. Our first-use steps and separate suggestion/correction forms reduce navigation and submission friction without claiming that our listed mods were tested.
- **Teach one useful thing, then link the resource:** the closest catalog's author publishes a [Mods analysis](https://karanbansal.in/blog/claude-mods-scoreboard/) and a [mechanism tutorial](https://karanbansal.in/blog/claude-mods/). For a future announcement, use one concrete task, an attributed demo, one important limit, and a direct section link. Keep credit with the original author; never turn a demo into a claim of independent runtime verification.

## Site cross-link, after a site exists

Use `data/mods.json` as the source for a small searchable companion directory, with filters for use case, review status, and license. Keep important descriptions and source links in crawlable HTML. Link each site entry to the original project and to the GitHub evidence page; link the README back to the real site URL. Only add a site URL after it is live and checked.

The site should add browsing value, not duplicate a giant catalog. Search indexing and traffic are not guaranteed. Use actual GitHub traffic/referrer data and permitted site analytics to decide what is useful; do not treat star count as product validation.

## Ongoing editorial focus

Recheck when Claude releases break the API, a selected mod moves, its permissions expand, or a reader reports a failure. A monthly small selection of substantiated updates is preferable to mass-adding links without review. This is an editorial suggestion, not an enabled automation.
