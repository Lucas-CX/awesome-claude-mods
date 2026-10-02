# Compatibility and safe evaluation

Snapshot: 2026-10-02. This guide has not run a Claude Code mod. There is no Claude executable in the preparation environment.

## Read version claims literally

- The [current authoring guide](https://code.claude.com/docs/en/plugins/mods/create) requires Claude Code 2.1.287 or later. Record your exact version before comparing results.
- A project's statement that it validated on 2.1.269 or 2.1.276 is historical evidence, not a promise about 2.1.287 or a later release.
- The old enable-function-hooks environment variable is ignored by the current baseline. Do not use it as an enable/disable switch.
- A compatible API does not guarantee that a particular UI appears on every surface. Check the project's UI requirements and the [official surface matrix](https://code.claude.com/docs/en/plugins/mods/overview#where-mods-run).
- Several mods may compete for the same prompt band or pane. Evaluate alone before trying combinations.

## Review before loading

1. Follow the original author's canonical repository; inspect its manifest, hooks declaration, entry module, release notes, dependencies, and license. Pin a release or commit for a reproducible evaluation.
2. Look for file access, process execution, network requests, transcript access, model calls, and event rewriting. Read-only file behavior is not the same as no model cost or no external transmission.
3. Use a disposable project without secrets or production credentials. Do not treat a mod as a sandbox or a substitute for your permission policy.
4. Inspect the capability listing before running the mod:

   ```sh
   claude --version
   claude plugin validate ./path-to-reviewed-mod
   ```

5. If the project ships official-kit tests, review them and follow its documented test command. The [official testing guide](https://code.claude.com/docs/en/plugins/mods/test) explains stubbed event tests and `claude plugin test`. Static validation, unit tests, and live behavior are different evidence levels.
6. Only after reviewing the code and permissions, follow the author's current installation instructions. A one-session local checkout can be loaded with `claude --plugin-dir ./path-to-reviewed-mod`; that command executes the mod.
7. Check the mod is listed as active, exercise the intended workflow and its failure path, and record the result using [the review template](REVIEW_TEMPLATE.md).
8. Disable/uninstall the specific plugin if needed. Restart without `--plugin-dir` for a local one-session trial. Consult [official troubleshooting](https://code.claude.com/docs/en/plugins/mods/troubleshoot) rather than weakening organization policies to force loading.

## What this guide does not guarantee

A capability footprint is evidence about declared behavior, not a security certification. Upstream test reports remain upstream claims until reproduced. A project described as a guard or redactor may have bypasses. A successful display does not prove a correct cost estimate, cache saving, or final filesystem state.
