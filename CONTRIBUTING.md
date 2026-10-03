# Contributing

Help readers choose and verify a useful mod. A short, evidenced entry is better than a large list of unreviewed links.

## Inclusion criteria

- A canonical, publicly readable original-author source
- An actual plugin mod: `hooks/hooks.json` identifies an executable module, and the named file exists
- A specific use case and a meaningful reason to choose it
- Documented version assumptions and installation path
- A license declaration or an explicit unresolved-license label
- Clear access/cost caveats and honest test status

Standalone skills, MCP servers, terminal themes, settings hooks, forks that only repackage somebody else's work, and general catalogs do not become mod entries. Relevant authoring tools may be linked separately.

## Suggest or correct without a pull request

- [Suggest a mod](https://github.com/Lucas-CX/awesome-claude-mods/issues/new?template=suggest-mod.yml): give its original source, one concrete use case, and whatever evidence you already have. Unknown version or license details are welcome when clearly marked; a suggestion still needs review before inclusion.
- [Report a correction or compatibility result](https://github.com/Lucas-CX/awesome-claude-mods/issues/new?template=report-correction.yml): identify the affected entry, what changed, and a dated source or reproducible result.

English and Chinese submissions are both welcome. You do not need to install a mod or translate both READMEs to open an issue. A documentation check is useful; label it honestly.

## Submit a pull request

1. Add a concise entry to `data/mods.json` and both READMEs. Use the existing fields; preserve original attribution.
2. Update `docs/EVIDENCE.md` with a dated primary-source link and upstream version claim. Do not silently convert an old tested version into a current minimum.
3. If you ran anything, include exact mod commit/release, Claude version, OS/surface, steps, result, known failures, and a sanitized log or screenshot. Use `docs/REVIEW_TEMPLATE.md`.
4. Run `python3 scripts/validate_catalog.py`.
5. Open a focused pull request. Disclose if you wrote, maintain, or receive payment from the project.

Do not upload real secrets, private repositories, private transcripts, customer data, or unlicensed screenshots. Use synthetic examples. Do not describe a project as safe, maintained, tested, official, or cost-saving unless the statement has dated evidence and a precise scope.

## Review labels

- `documentation-and-entry-checked`: primary documentation and module entry existence checked; not full implementation audit
- `static-validated`: the exact commit passed the named Claude validator version, with log
- `runtime-tested`: a named workflow was exercised on the exact environment, with result
- `blocked`: a relevant dependency, license, compatibility, or access issue remains

A failure is worth contributing. Describe what broke and on which version. Never remove a failure simply to make a badge green.

## Maintenance policy

When reviewing an entry again, preserve the old date and outcome in a case report, record the new source identity, and update its current status. Do not change review dates automatically without rechecking. Mark archived, moved, or broken projects visibly; prefer canonical destinations over mirrors. No automated review schedule is promised.

No collection-wide license is granted by this repository. Submit only original text or material you are authorized to contribute; attribution and upstream licenses remain separate.
