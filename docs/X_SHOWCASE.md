# X showcase: original Claude Mods demos and announcements

Source review: **2026-10-02**. Five cases, organized by use case.

Each case has an original-author or official-publisher post and a canonical function-hook implementation. This verifies provenance and project type, **not** safety, current-version compatibility, or measured productivity. No mods were installed or run. “Author-authored” does not claim to identify the earliest historical post.

The three Anthropic Playground entries are **published examples, not supported Anthropic products**. Read the current official installation guidance because older community READMEs still describe early-access flags.

## English

### Token Weather · Context visibility

- **Use case:** A weather-style context gauge with a recent-turn sparkline makes context growth visible without opening a separate dashboard.
- **X source:** [@ClaudeDevs · 2026-10-01](https://x.com/ClaudeDevs/status/2105721436270993609) · official publisher demo
- **Source:** [anthropics/claude-code-playground](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather) · [Apache-2.0 (repository license)](https://github.com/anthropics/claude-code-playground/blob/main/LICENSE)
- **Caveat:** The percentage uses the full model window, not the auto-compaction threshold. It updates after turns; it is a teaching sample, not a supported product.
- **Evidence:** original public X post read directly; canonical repository documentation and function-hook entry checked. [Function-hook entry](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/token-weather/hooks/hooks.json); [README](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/token-weather/README.md).

### Replay Theater · Edit review

- **Use case:** Step through the last editing turn one attempted Edit or Write at a time. Useful for learning how a change unfolded before checking the final Git diff.
- **X source:** [@ClaudeDevs · 2026-10-01](https://x.com/ClaudeDevs/status/2105721439206994232) · official publisher demo
- **Source:** [anthropics/claude-code-playground](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater) · [Apache-2.0 (repository license)](https://github.com/anthropics/claude-code-playground/blob/main/LICENSE)
- **Caveat:** It can record denied or failed attempts and truncates displayed diffs; it is not proof of final disk contents. Session-local teaching sample, not a supported product.
- **Evidence:** original public X post read directly; canonical repository documentation and function-hook entry checked. [Function-hook entry](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/replay-theater/hooks/hooks.json); [README](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/replay-theater/README.md).

### Blast Radius · Command impact preview

- **Use case:** Hold selected risky Bash commands and inspect a side-pane impact preview before choosing whether to proceed. An instructive example of a human decision inside a tool-call hook.
- **X source:** [@ClaudeDevs · 2026-10-01](https://x.com/ClaudeDevs/status/2105721437701259338) · official publisher demo
- **Source:** [anthropics/claude-code-playground](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius) · [Apache-2.0 (repository license)](https://github.com/anthropics/claude-code-playground/blob/main/LICENSE)
- **Caveat:** Heuristic command matching is not a security boundary and misses wrappers or shell constructs. Migration previews may load project code. Test only in a disposable project; upstream notes some later fixes were not re-run live.
- **Evidence:** original public X post read directly; canonical repository documentation and function-hook entry checked. [Function-hook entry](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/blast-radius/hooks/hooks.json); [README](https://github.com/anthropics/claude-code-playground/blob/main/claude-code/mods/blast-radius/README.md).

### Mindful Claude · Interface and waiting time

- **Use case:** A breathing animation appears while Claude is working and disappears when the turn ends. A compact example of turn-aware UI that does not need model-generated content.
- **X source:** [@halluton · 2026-09-14](https://x.com/halluton/status/2099640486130835845) · author authored demo
- **Source:** [halluton/Mindful-Claude](https://github.com/halluton/Mindful-Claude) · [MIT](https://github.com/halluton/Mindful-Claude/blob/main/LICENSE)
- **Caveat:** Treat it as a UI/focus experiment; no medical benefit is claimed here. Its README retains early-access flag instructions, and current-runtime compatibility was not tested.
- **Evidence:** original public X post read directly; canonical repository documentation and function-hook entry checked. [Function-hook entry](https://github.com/halluton/Mindful-Claude/blob/main/hooks/hooks.json); [README](https://github.com/halluton/Mindful-Claude/blob/main/README.md).

### terminal-browser · Embedded browser and preview

- **Use case:** Open a real browser inside a Claude Code pane to preview a local website or HTML output beside the conversation. The plugin also exposes a browser API for other mods.
- **X source:** [@RobKnight__ · 2026-09-17](https://x.com/RobKnight__/status/2100622380439683541) · author authored announcement
- **Source:** [zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser/tree/main/claude-code-plugin) · [MIT](https://github.com/zenbu-labs/terminal-browser/blob/main/LICENSE)
- **Caveat:** Requires the separate terminal-browser binary and kitty graphics protocol with Unicode placeholders. The author marks it experimental; tmux integration, mouse alignment and layout have documented limits. Installing or browsing may involve local-network permissions and normal website traffic.
- **Evidence:** author announcement plus explicit author-to-repository link; README, hook entry and exported register checked. [Function-hook entry](https://github.com/zenbu-labs/terminal-browser/blob/main/claude-code-plugin/hooks/hooks.json); [README](https://github.com/zenbu-labs/terminal-browser/blob/main/claude-code-plugin/README.md).
- **Attribution bridge:** the same author [links this exact plugin directory](https://x.com/RobKnight__/status/2100622964395774443).


## 简体中文

核对日期：**2026-10-02**。以下五个案例均可追溯到作者本人或官方发布者的 X 帖子，并核对到真实的 function-hook Mod 源码入口。核对范围为来源与项目类型，**不等于安全审计、当前版本兼容性测试或生产力效果验证**。没有安装或运行这些 Mod，也不以点赞量衡量质量。

Anthropic Playground 中的三个项目是公开教学示例，**不是受支持的 Anthropic 产品**。部分社区 README 仍使用旧版早期访问说明，安装前应核对当前官方文档。

### Token Weather · 上下文可视化

- **用途：**用天气状态与近期轮次的小图持续显示上下文增长，无需切换到单独的面板。
- **X 原帖：**[@ClaudeDevs · 2026-10-01](https://x.com/ClaudeDevs/status/2105721436270993609)
- **源码：**[anthropics/claude-code-playground](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/token-weather)
- **注意：**百分比以完整上下文窗口为基准，不等于自动压缩阈值；轮次结束后更新。这是教学示例，不是受支持的产品。
- **证据：**直接读取原始 X 帖子，并核对仓库说明、function-hook 入口及作者归属；未做运行验证。

### Replay Theater · 修改审阅

- **用途：**按顺序回看上一轮的 Edit／Write 修改尝试，先理解修改过程，再核对最终 Git diff。
- **X 原帖：**[@ClaudeDevs · 2026-10-01](https://x.com/ClaudeDevs/status/2105721439206994232)
- **源码：**[anthropics/claude-code-playground](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/replay-theater)
- **注意：**可能包含被拒绝或失败的修改尝试，差异视图也会截断；不能据此证明文件最终状态。会话内教学示例，不是受支持的产品。
- **证据：**直接读取原始 X 帖子，并核对仓库说明、function-hook 入口及作者归属；未做运行验证。

### Blast Radius · 命令影响预览

- **用途：**暂停部分高风险 Bash 命令，在侧栏查看影响后决定是否执行，是把人工决策接入工具调用钩子的教学案例。
- **X 原帖：**[@ClaudeDevs · 2026-10-01](https://x.com/ClaudeDevs/status/2105721437701259338)
- **源码：**[anthropics/claude-code-playground](https://github.com/anthropics/claude-code-playground/tree/main/claude-code/mods/blast-radius)
- **注意：**启发式命令匹配不是安全边界，会漏掉包装脚本及部分 shell 语法；迁移预览可能加载项目代码。仅在可丢弃项目中评估，上游说明部分后续修复尚未重新实测。
- **证据：**直接读取原始 X 帖子，并核对仓库说明、function-hook 入口及作者归属；未做运行验证。

### Mindful Claude · 界面与等待体验

- **用途：**Claude 工作时显示呼吸节奏动画，轮次结束后消失，是无需模型生成内容的轻量、轮次感知界面示例。
- **X 原帖：**[@halluton · 2026-09-14](https://x.com/halluton/status/2099640486130835845)
- **源码：**[halluton/Mindful-Claude](https://github.com/halluton/Mindful-Claude)
- **注意：**仅作为界面和专注体验实验收录，不宣称医疗收益。README 仍保留早期访问开关说明，未在当前版本运行验证。
- **证据：**直接读取原始 X 帖子，并核对仓库说明、function-hook 入口及作者归属；未做运行验证。

### terminal-browser · 内嵌浏览器与预览

- **用途：**在 Claude Code 侧栏打开真实浏览器，并排预览本地网站或 HTML 产物；还可通过插件 API 供其他 Mod 使用。
- **X 原帖：**[@RobKnight__ · 2026-09-17](https://x.com/RobKnight__/status/2100622380439683541)
- **源码：**[zenbu-labs/terminal-browser](https://github.com/zenbu-labs/terminal-browser/tree/main/claude-code-plugin)
- **注意：**依赖单独的 terminal-browser 程序，以及支持 kitty 图形协议和 Unicode 占位符的终端。作者标为实验性，tmux 集成、鼠标位置和布局存在限制；安装与浏览可能涉及本地网络权限及正常网站流量。
- **证据：**直接读取原始 X 帖子，并核对仓库说明、function-hook 入口及作者归属；未做运行验证。


## Attribution and collection boundaries

- Official announcement: https://x.com/ClaudeDevs/status/2105721434807083061
- Official sample / guide follow-on: https://x.com/ClaudeDevs/status/2105721441622884802
- cc-pr-tracker, cctop, claude-mermaid, aside, secret-redactor and cc-arcade remain useful repository-backed candidates, but this review did not establish an original author X permalink for them. Do not label them “sourced from X” without further evidence.
- Secondary catalogs and public post indexes helped discovery; the five included posts were then read directly on X. No repost is substituted for an author post.
- No code, screenshots, or videos were copied for redistribution. Link to upstream demos rather than assuming permission to reuse media.
