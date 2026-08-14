---
name: ai-agent-tools-scanner
description: 'Discovers AI Agent building platforms and tools that are free to use as of a given date, comparable in capability to WorkBench. Searches HuggingFace, GitHub, ProductHunt, AI tool directories and developer communities, extracts structured fields (name, capability description, free-usage terms, links, last-updated), emits Markdown + JSON reports archived under reports/YYYY-MM-DD/, and optionally auto-commits results to a Git repository. Agent-agnostic: depends only on a caller-provided web-search / web-fetch / shell capability plus explicit input parameters, with a defined input/output contract for integration by any caller. Use when the user asks for free AI agent builder tools, daily AI agent tool scans, or scheduled AI tooling reports.'
metadata:
  argument-hint: '[--search_date YYYY-MM-DD] [--work_dir PATH] [--output_format markdown|json|both] [--repo_url URL] [--branch NAME] [--auth_method token|ssh] [--lang zh|en]'
agent_created: true
---

# AI Agent 工具每日扫描 Skill

## 概述

检索**指定日期**仍可免费使用的、与 **WorkBench** 功能相似的 AI Agent 智能体构建平台/工具，结构化采集后生成报告并按日期归档，可选自动推送到 Git 仓库。

**设计原则（agent 无关 / 解耦）：**
- 不依赖任何调用方的会话上下文、私有状态或特定 agent 的内置工具名。
- 仅依赖一组**显式声明的输入参数**和调用方提供的**通用能力**（联网检索 / 网页抓取 / Shell 执行）。
- 输入 / 输出均有明确契约，可被任意 agent 或纯 cron 脚本以程序化方式集成。
- 定时调度由**调用方**负责（cron / systemd timer / agent 平台的 automation），本 skill 只声明推荐调度参数，不绑定任何调度实现。

## 接口契约 (Interface Contract)

### 输入参数 (Input)

| 参数 | 类型 | 默认值 | 必填 | 说明 |
|---|---|---|---|---|
| `search_date` | string `YYYY-MM-DD` | 执行当日日期 | 否 | 搜索截止日期。所有"是否仍免费""最后更新"判断以此为准。 |
| `work_dir` | string path | 当前工作目录 | 否 | 报告与日志的输出根目录；启用推送时同时作为 Git 仓库本地克隆路径。 |
| `output_format` | enum `markdown` \| `json` \| `both` | `both` | 否 | 报告输出格式。 |
| `repo_url` | string URL | 空 | 否 | 目标 Git 仓库地址（https 或 ssh）。**为空则跳过推送，仅本地归档**，不视为失败。 |
| `branch` | string | `main` | 否 | 推送目标分支。 |
| `auth_method` | enum `token` \| `ssh` | `token` | 否 | 认证方式。`token` 从环境变量读取 PAT；`ssh` 使用本机 ssh key。 |
| `token_env` | string | `GITHUB_TOKEN` | 否 | `auth_method=token` 时读取 PAT 的环境变量名。**PAT 绝不写入配置文件或日志**。 |
| `schedule_time` | string `HH:MM` | `09:00` | 否 | 推荐触发时间（声明性，供调用方配置调度器）。 |
| `schedule_frequency` | enum `daily` \| `weekly` \| `custom_cron` | `daily` | 否 | 推荐执行频率（声明性）。 |
| `custom_cron` | string | 空 | 否 | `schedule_frequency=custom_cron` 时的 cron 表达式。 |
| `lang` | enum `zh` \| `en` | `zh` | 否 | 检索词与报告输出语言。 |
| `dingtalk_webhook` | string URL | 空 | 否 | 钉钉机器人 webhook URL。**为空则跳过钉钉推送**，不视为失败。 |
| `dingtalk_keywords` | string | `免费` | 否 | 钉钉机器人安全关键词（逗号分隔多个），消息内容须至少包含其一。 |

> 参数可通过三种等价方式传入，优先级从高到低：**命令行参数 > 配置文件（`--config` 指向的 JSON）> 默认值**。本 skill 不读取任何隐含上下文。`config.example.json` 为配置文件模板。

### 依赖能力 (Required Capabilities)

调用方需提供以下能力（**工具名由调用方绑定，本 skill 不假定具体实现**）：

- `web_search(query: str, keyword_groups?: list[str], max_results?: int) -> list[{title, url, snippet}]`
- `web_fetch(url: str, prompt?: str) -> str`
- `shell(command: str) -> {stdout, stderr, exit_code}` — 用于执行 `scripts/` 下的 Python 脚本
- `file_write(path: str, content: str) -> void` — 亦可由 `shell` 代替

运行时依赖：**Python ≥ 3.8**（标准库即可，无第三方依赖）；启用推送时额外需要 **git**。

调用方在集成时填写 `tool_binding`（模板，非运行时依赖）：

```
## tool_binding（由调用方填写）
web_search: <调用方实际提供的联网检索工具>
web_fetch:  <调用方实际提供的网页抓取工具>
shell:      <调用方实际提供的命令执行工具>
python:     <目标环境的 Python 解释器命令，如 python3 / python>
```

执行步骤中以 `{{web_search}}` / `{{web_fetch}}` / `{{shell}}` / `{{python}}` 指代上述能力。
具体绑定样例见 `references/integration_examples.md`。

### 输出契约 (Output Contract)

产物统一位于 `{work_dir}` 下：

| 路径 | 内容 |
|---|---|
| `reports/{search_date}/ai-agent-tools-report-{search_date}.md` | Markdown 主报告（汇总表 + 详情） |
| `reports/{search_date}/ai-agent-tools-report-{search_date}.json` | 机器可读报告 |
| `logs/run-{search_date}.log` | 完整运行日志 |
| `logs/error-{search_date}.log` | 错误日志（仅出错时产生内容） |

JSON 报告结构：

```json
{
  "report_date": "YYYY-MM-DD",
  "generated_at": "YYYY-MM-DD HH:MM:SS",
  "tool_count": 0,
  "no_new_tools": true,
  "note": "当日未发现新工具",
  "tools": [
    {
      "name": "工具名称",
      "description": "核心能力 + 与 WorkBench 的相似度（高/中/低 + 理由）+ 适用场景",
      "free_usage": "免费额度 / 试用期限 / 限制条件 / 是否需要信用卡",
      "links": {"website": "https://...", "github": "https://... | null", "docs": "https://... | null"},
      "last_updated": "YYYY-MM-DD | unknown",
      "source_channel": "HuggingFace | GitHub | ProductHunt | 导航站 | 社区"
    }
  ]
}
```

约束：
- 仅输出通过筛选条件（与 WorkBench 相似 **且** 截止 `search_date` 可免费使用）的工具。
- 不编造工具、链接或免费政策；无法核实的字段填 `unknown`，`website` 必填。
- **无结果不是错误**：生成标注「当日未发现新工具」的空报告，流程正常结束（退出码 0）。

## 触发条件

当用户询问「有哪些免费的 AI Agent 构建平台」「每日扫描 AI 智能体工具」「找类似 WorkBench 的免费工具」「AI agent builder free list」，或调度器触发每日扫描任务时。

## 执行步骤

### Step 1: 解析参数

确定 `search_date`（未传入则取运行环境当前日期，如 `{{shell}}: date +%F`）与 `work_dir`（未传入则用当前目录），确保 `work_dir` 存在。

### Step 2: 多渠道检索

参照 `references/search_sources.md` 的渠道清单与查询词模板，用 `{{web_search}}` 执行多轮检索，覆盖全部五类渠道，确保不遗漏新兴或小众工具：

1. **HuggingFace** — Spaces / 官方博客中的 agent 构建工具
2. **GitHub** — 开源 AI Agent 框架与低代码 Agent 平台（关注近期活跃项目）
3. **ProductHunt** — 近期发布的 AI Agent builder 产品
4. **AI 工具导航站** — 国内外（Toolify、AI工具集、Futurepedia、There's An AI For That 等）
5. **开发者社区** — Reddit r/AI_Agents、Hacker News、V2EX、掘金、知乎等

检索词中 `{year}` / `{date}` 分别取 `search_date` 的年份与完整日期；`lang` 决定中英文检索词权重。

### Step 3: 筛选与核实

收录条件（须同时满足）：
1. **功能相似**：具备 AI Agent 构建 / 编排 / 自动化工作流能力（详见 `references/search_sources.md` 的相似度判定）。
2. **免费可用**：截止 `search_date` 有永久免费层、可用免费额度、有效试用期，或开源可自部署。
3. **非重复**：不在 `references/search_sources.md` 的已知基线清单内；基线内工具仅在**免费政策重大变化或大版本更新**时收录并注明。

对每个候选用 `{{web_fetch}}` 打开官网或 GitHub 页面核实：仍可访问、免费政策描述准确、最后更新日期（GitHub 看最近 commit/release，产品站看 changelog）。无法核实的字段填 `unknown`，**不得编造**。

### Step 4: 结构化采集

将结果按「输出契约」中 `tools[]` 的字段结构组装为 JSON 数组，写入 `{work_dir}/collected-{search_date}.json`（UTF-8）。**无结果时写入 `[]`**。

### Step 5: 生成报告

```
{{shell}}: {{python}} <skill_dir>/scripts/generate_report.py \
  --input   {work_dir}/collected-{search_date}.json \
  --work-dir {work_dir} \
  --date    {search_date} \
  --output-format {output_format}
```

脚本自动处理空结果（生成「当日未发现新工具」报告而非中断）并写运行日志。
亦可用 `--config <path>` 从配置文件读取默认值；显式命令行参数优先。

### Step 6: 推送钉钉群（可选）

```
{{shell}}: {{python}} <skill_dir>/scripts/dingtalk_push.py \
  --work-dir {work_dir} \
  --date    {search_date} \
  --webhook {dingtalk_webhook} \
  --keywords {dingtalk_keywords}
```

脚本内置行为：
- 读取 `{work_dir}/reports/{search_date}/ai-agent-tools-report-{search_date}.md` 作为消息内容。
- 消息标题固定为「【免费AI Agent工具 每日扫描】」，确保包含钉钉机器人安全关键词。
- 消息内容过长时自动截断（钉钉 text 消息上限约 20000 字节），尾部提示完整报告见仓库。
- 使用 Python `urllib` 发送（**严禁 bash curl 内联中文**，会导致 UTF-8 乱码触发关键词校验失败）。
- webhook URL 为空 → 记录「跳过推送」，退出码 0。
- 报告文件不存在 → 发送错误通知到钉钉（含关键词），退出码 1。
- webhook 中的 access_token 在日志中自动脱敏。
- 推送失败（errcode ≠ 0）→ 记录错误日志，退出码 4，但**不影响后续 Git 推送**。

### Step 7: 推送 Git 仓库（可选）

```
{{shell}}: {{python}} <skill_dir>/scripts/git_push.py \
  --work-dir {work_dir} \
  --date     {search_date} \
  --repo-url {repo_url} \
  --branch   {branch} \
  --auth-method {auth_method} \
  --token-env   {token_env}
```

脚本内置行为：
- 首次运行自动 clone；clone 失败（空仓库/分支不存在）则回退 `git init` + `remote add`。
- 从 `assets/repo_template/` 补齐仓库骨架文件（LICENSE / README.md / .gitignore），**已存在则不覆盖**。
- 同步 skill 自身代码到仓库 `skill/<skill-name>/`。
- commit 信息固定格式：`[Auto] 每日AI Agent工具扫描报告 - YYYY-MM-DD`
- 推送失败自动重试 **3 次，间隔 30 秒**（可用 `--retries` / `--retry-interval` 调整）。
- `repo_url` 为空 → 记录「跳过推送」，退出码 0。
- PAT 在所有日志与命令回显中自动脱敏为 `***TOKEN***`。

### Step 8: 汇报

检查三个脚本退出码，非 0 时读取 `{work_dir}/logs/error-{search_date}.log` 摘要原因。向调用方汇报：**发现工具数量、报告文件路径、钉钉推送结果、Git 推送结果**（成功 / 跳过 / 失败原因）。

## 退出码约定

| 码 | 含义 |
|---|---|
| 0 | 成功（含「无结果空报告」与「未配置 webhook/仓库跳过推送」） |
| 1 | 脚本内部异常（详见 error 日志） |
| 2 | 认证配置缺失（`auth_method=token` 但 token 环境变量为空） |
| 3 | Git 推送重试耗尽仍失败（本地报告已保留） |
| 4 | 钉钉 API 返回 errcode != 0（不影响后续步骤） |

## 调度集成（由调用方实现）

本 skill 不绑定调度器。推荐参数 `schedule_time` / `schedule_frequency` / `custom_cron` 仅为声明，调用方需自行映射：

| 频率 | cron | RRULE |
|---|---|---|
| `daily` @ 09:00 | `0 9 * * *` | `FREQ=DAILY;BYHOUR=9;BYMINUTE=0` |
| `weekly` @ 周一 09:00 | `0 9 * * 1` | `FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0` |
| `custom_cron` | 用户自定义 | 换算为等价 RRULE |

各类调用方（agent 平台 automation / crontab / systemd timer / GitHub Actions）的具体接法见 `references/integration_examples.md`。

## 注意事项

- 免费政策变动频繁，报告中的额度与限制以官方最新说明为准。
- 搜索无结果、报告生成失败、推送失败均**不应中断整体流程**：错误落盘到 `logs/`，已产出内容保留。
- 凭据只经由环境变量传递；`config.json` 中不得出现明文 PAT。
- 本 skill 不依赖任何调用方上下文；所有行为由上述输入参数与依赖能力决定，可被任意 agent 解耦集成。
