# 每日 AI Agent 工具扫描报告 - 2026-08-09

> 搜索截止日期：2026-08-09 ｜ 生成时间：2026-08-09 10:10:52 ｜ 发现工具数：8

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | LongHorizon-Harness | 阿里高德 AMAP-ML 团队开源的长周期（long-horizon）计算机使用 Agent 编排框架。核心是 Manage–Execute–Audit（MEA）三角色循环：manager 依据已验证事实动态派生下一子任务，executor 每轮从干净上下文执行单个子任务后丢弃原始轨迹，只读 auditor 检查真实环境并且是唯一能更新任务状态记录的角色，从而抑制复合错误、上下文腐化与任务状态丢失。后端无关，通过轻量 AgentAdapter 把 Claude Code / Codex CLI / OpenClaw / Gemini CLI / Hermes / mini-SWE-agent 作为可互换运行时，三个角色还可各配不同模型。与 WorkBench 相似度：高——同属跨会话长任务的 Agent 编排 + 工具调用 + 状态记忆底座。适用场景：桌面应用与 CLI 混合的长流程自动化、OSWorld/Terminal-Bench 类计算机使用任务、需要可审计执行轨迹的企业流程。 | 完全开源可自部署，MIT 许可证，无任何付费层。安装 `uv tool install lh-harness` 即可，需 Python 3.10+ 与至少一个 agent 运行时（claude / codex / openclaw）在 PATH 中。模型调用成本由用户自带 API Key 承担，框架本身不收费，无需信用卡。 | [官网](https://lh-harness.pages.dev) / [GitHub](https://github.com/AMAP-ML/LongHorizon-Harness) / [文档](https://lh-harness.pages.dev) | 2026-08-07 | GitHub |
| 2 | BossConsole | risa-labs 开源的多平台 AI Agent 操作台（operator's console），基于 JVM 原生多线程实现而非 Electron，主打低资源占用与企业可控。在一个界面里同时驱动 Claude Code、Codex、Gemini、OpenCode 等多个编码 Agent，内置真实浏览器、终端、编辑器、密钥管理与 100+ MCP 工具接入。与 WorkBench 相似度：高——多 Agent 并行编排、工具/MCP 生态、本地文件与系统访问、浏览器自动化四项能力齐备。适用场景：企业内部 Agent 工作台、科研与实验流程自动化、需要统一密钥治理的多 Agent 协同开发。 | 开源可自部署，Apache-2.0 许可证，仓库代码完整开放，无付费墙。模型侧需自带各 Agent CLI 的账号或 API Key。官网 bossconsole.ai 未公开商业版定价（unknown），开源版本身免费、无需信用卡。 | [官网](https://bossconsole.ai) / [GitHub](https://github.com/risa-labs-inc/BossConsole) | 2026-08-09 | GitHub |
| 3 | goal-flow (Graph-Orchestrated Agent Loop) | 2026-08-06 新建的开源 Agent 编排框架，构建在 LangGraph 之上，把「工作流图」与「Agent 自主循环」两种范式合并：既能用确定性图节点约束流程，又允许节点内 Agent 自由 loop。特色能力是可把 Dify DSL 直接转译（transpile）为可运行代码，并支持切换 wire protocol（Dify / OpenAI 兼容），便于从 Dify 低代码画布平滑迁移到代码托管的生产工程。与 WorkBench 相似度：中高——覆盖工作流编排、agent loop、工具调用，但无内置 UI 与定时任务面板。适用场景：已有 Dify 编排资产需要代码化、要求生产级可测试性的团队。 | 开源可自部署，MIT 许可证，全部功能免费，无付费层、无需信用卡。依赖 LangGraph（同为开源），模型调用费用自理。项目较新（71 star），建议评估后再用于生产。 | [官网](https://github.com/wanmol/goal-flow) / [GitHub](https://github.com/wanmol/goal-flow) | 2026-08-06 | GitHub |
| 4 | Approving | 开源、可自托管的 Agent 交付流水线平台，把编码 Agent 的执行过程变成「可视化、可评审、可恢复」的工作流。每个 Agent 在真实 Docker 沙箱中运行，节点之间以结构化 artifact 交换产物，并在关键节点自动暂停等待人工 Approve 后再继续。与 WorkBench 相似度：中高——具备多 Agent 编排、沙箱化工具执行、人机协同审批与断点恢复；偏交付治理而非通用 Agent 构建。适用场景：需要合规审批留痕的团队级 AI 编码交付、把不可控的 Agent 长跑变成分段可回滚的流程。 | 开源可自部署，MIT 许可证，代码与自托管部署完全免费，无需信用卡。需要本机或服务器可运行 Docker。官网 approving-ai.com 未公开托管版定价（unknown）。 | [官网](https://www.approving-ai.com) / [GitHub](https://github.com/cocofhu/approving) | 2026-08-08 | GitHub |
| 5 | Coldtea | 2026-08-07 在 Product Hunt 发布（当日 469 赞）的 agentic IDE，主张「让软件交付自动驾驶」。把三类 Agent 收进同一个本地工作区：终端里的编码 Agent 可以成组启动、互相 review 与协作；视觉 QA Agent 把自然语言描述的 Web/移动端用户旅程转成自愈测试，在每个 PR 预览环境上跑全量套件并对部署做门禁；监控 Agent 盯着 Sentry / Datadog / Grafana / New Relic / PostHog / Vercel 的错误日志、用户会话与客户反馈，自行调查后直接开 PR 提修复。另有 Tasks 面板同步研发看板、把任务派给云端后台 Agent 并行跑。兼容 Claude Code、Codex、OpenCode 等现有 CLI Agent，代码默认留在本机，云端执行为可选项。与 WorkBench 相似度：高——多 Agent 编排、工具调用、后台/定时任务、本地文件与浏览器自动化俱全。适用场景：已用编码 Agent 但卡在回归测试与线上问题响应的工程团队。 | Freemium。官方 FAQ 明确：终端（多 Agent 编码工作区）永久免费（free forever）；agentic testing 提供「generous free tier」；生产监控可免费试用（free to try）。付费档价格官网未公开（unknown）。目前仅 macOS 客户端，Windows/Linux 在等待列表。注册未见强制信用卡要求。 | [官网](https://www.coldtea.ai/) / [文档](https://www.coldtea.ai/) | 2026-08-07 | ProductHunt |
| 6 | Rindler | 2026-08-07 Product Hunt 发布（247 赞）的网页任务自动化 Agent。与「每次让浏览器 Agent 现场看页面猜操作」的做法不同，Rindler 预先把网站测绘成一张「地图」——记录站点有哪些界面、每个界面能做什么动作、动作返回什么字段，已测绘 1000+ 站点；运行时 Agent 直接调用地图，因此每次返回的字段名与结构完全一致，速度与成本也不随次数线性增长。单次运行内按步骤动态选择传输方式（真实浏览器点击 或 直接调站点自有接口）。每张地图每天对真实站点做一次校验，页面改版由官方修复；运行中单步失败则由模型现场重解该步。支持自然语言下单、自动登录、按计划定时重复执行，并提供 HTTP MCP Server（mcp.rindler.ai）供自有后端调用。与 WorkBench 相似度：中高——浏览器自动化 + 定时任务 + MCP 工具调用，但不做通用 Agent 构建。适用场景：无 API 的后台系统批量取数、重复性网页操作外包给 Agent。 | 有免费可用途径但非永久免费层：Starter 档 $100/月含 100 次 session，附带 7 天免费试用并免费为你测绘一个指定站点；Teams 档 $1000/月含 1000 次 session 与定时自动化。所有档位单次 session 均为 $1，失败的运行不计费。另提供无需注册的公开 playground（chat.rindler.ai），预置若干站点可直接试用。试用是否需要信用卡官网未说明（unknown）。 | [官网](https://rindler.ai) / [文档](https://chat.rindler.ai/) | 2026-08-07 | ProductHunt |
| 7 | CopilotKit Channels SDK | CopilotKit（AG-UI 协议作者，GitHub 36.6k star）于 2026-08-06 发布的新模块，解决「Agent 建好了但用户不在你的 Web App 里」的最后一公里。用一套共享的 Channels JSX 写一次交互，自动在 Slack 渲染原生 Block Kit、在 Microsoft Teams 渲染 Adaptive Cards，Discord、WhatsApp、Telegram 在路上。已部署的 Agent 会为每个频道会话单独初始化，支持流式回复、工具结果回传、以及用原生卡片做人工审批（human-in-the-loop）而不必跳转到另一个后台。可接入 LangGraph、CrewAI、Microsoft Agent Framework 或任何自定义 AG-UI Agent。与 WorkBench 相似度：中高——不是从零构建 Agent，而是给已有 Agent 补齐多渠道交付、审批与状态持久化这层编排能力。适用场景：把内部 Agent 铺到团队日常协作工具里。 | CopilotKit 主仓库 MIT 开源可自托管（36,640 star，2026-08-09 仍有提交），Channels SDK 随开源栈发布，官方提供完整可克隆的示例仓库 CopilotKit/OpenTag。托管侧的 CopilotKit Intelligence（负责 Slack/Teams 的 provider 连接、投递重试、持久化频道状态）为官方运营服务，其定价与免费额度官网未公开（unknown）；纯自托管路径无需付费、无需信用卡。 | [官网](https://copilotkit.ai/channels) / [GitHub](https://github.com/CopilotKit/CopilotKit) / [文档](https://docs.copilotkit.ai/channels) | 2026-08-09 | 社区 |
| 8 | Open Minis | 跨 iOS / Android 的开源端侧 AI Agent 应用，2026-08-03 登上 Product Hunt（90 赞）后在国内外 AI 工具导航站快速铺开。它给模型配了一台「真正的电脑」：手机内跑一个沙箱化 Alpine Linux shell（iOS 用 iSH、Android 用 PRoot），Agent 可以装软件包、跑 Python、改真实文件、驱动浏览器；外围 30+ 原生桥接打通 HealthKit、HomeKit、日历、提醒事项、通讯录、蓝牙、剪贴板、媒体与闹钟。带 SKILL.md 技能系统与持久记忆，为 Claude / Codex / OpenClaw 写的 Skills 基本可直接复用；多 Workspace 隔离各自上下文。自带模型（Claude、GPT、Gemini、Kimi、Grok 或任意 OpenAI 兼容端点），API Key 与数据不离开手机。与 WorkBench 相似度：高——agent loop、工具调用、技能生态、本地文件系统访问、浏览器自动化、记忆系统全覆盖，差异在于运行载体是手机而非桌面。适用场景：移动端个人自动化、智能家居与健康数据联动、随身可用的 Agent 工作区。 | 完全免费且开源，GPL-3.0 许可证（主仓库 3,403 star，技能库 MinisSkills 为 MIT，用例库 AwesomeMinis 为 CC0）。App 本身不收费、无内购层、无需信用卡；唯一成本是自带的模型 API Key 消耗。所有数据与密钥仅存本机。 | [官网](https://openminis.app) / [GitHub](https://github.com/OpenMinis/OpenMinis) / [文档](https://github.com/OpenMinis/MinisSkills) | 2026-08-01 | 导航站 |

## 详细信息

### 1. LongHorizon-Harness

- **功能描述**：阿里高德 AMAP-ML 团队开源的长周期（long-horizon）计算机使用 Agent 编排框架。核心是 Manage–Execute–Audit（MEA）三角色循环：manager 依据已验证事实动态派生下一子任务，executor 每轮从干净上下文执行单个子任务后丢弃原始轨迹，只读 auditor 检查真实环境并且是唯一能更新任务状态记录的角色，从而抑制复合错误、上下文腐化与任务状态丢失。后端无关，通过轻量 AgentAdapter 把 Claude Code / Codex CLI / OpenClaw / Gemini CLI / Hermes / mini-SWE-agent 作为可互换运行时，三个角色还可各配不同模型。与 WorkBench 相似度：高——同属跨会话长任务的 Agent 编排 + 工具调用 + 状态记忆底座。适用场景：桌面应用与 CLI 混合的长流程自动化、OSWorld/Terminal-Bench 类计算机使用任务、需要可审计执行轨迹的企业流程。
- **免费使用方式**：完全开源可自部署，MIT 许可证，无任何付费层。安装 `uv tool install lh-harness` 即可，需 Python 3.10+ 与至少一个 agent 运行时（claude / codex / openclaw）在 PATH 中。模型调用成本由用户自带 API Key 承担，框架本身不收费，无需信用卡。
- **官网**：https://lh-harness.pages.dev
- **GitHub**：https://github.com/AMAP-ML/LongHorizon-Harness
- **文档**：https://lh-harness.pages.dev
- **最后更新日期**：2026-08-07
- **发现渠道**：GitHub

### 2. BossConsole

- **功能描述**：risa-labs 开源的多平台 AI Agent 操作台（operator's console），基于 JVM 原生多线程实现而非 Electron，主打低资源占用与企业可控。在一个界面里同时驱动 Claude Code、Codex、Gemini、OpenCode 等多个编码 Agent，内置真实浏览器、终端、编辑器、密钥管理与 100+ MCP 工具接入。与 WorkBench 相似度：高——多 Agent 并行编排、工具/MCP 生态、本地文件与系统访问、浏览器自动化四项能力齐备。适用场景：企业内部 Agent 工作台、科研与实验流程自动化、需要统一密钥治理的多 Agent 协同开发。
- **免费使用方式**：开源可自部署，Apache-2.0 许可证，仓库代码完整开放，无付费墙。模型侧需自带各 Agent CLI 的账号或 API Key。官网 bossconsole.ai 未公开商业版定价（unknown），开源版本身免费、无需信用卡。
- **官网**：https://bossconsole.ai
- **GitHub**：https://github.com/risa-labs-inc/BossConsole
- **文档**：-
- **最后更新日期**：2026-08-09
- **发现渠道**：GitHub

### 3. goal-flow (Graph-Orchestrated Agent Loop)

- **功能描述**：2026-08-06 新建的开源 Agent 编排框架，构建在 LangGraph 之上，把「工作流图」与「Agent 自主循环」两种范式合并：既能用确定性图节点约束流程，又允许节点内 Agent 自由 loop。特色能力是可把 Dify DSL 直接转译（transpile）为可运行代码，并支持切换 wire protocol（Dify / OpenAI 兼容），便于从 Dify 低代码画布平滑迁移到代码托管的生产工程。与 WorkBench 相似度：中高——覆盖工作流编排、agent loop、工具调用，但无内置 UI 与定时任务面板。适用场景：已有 Dify 编排资产需要代码化、要求生产级可测试性的团队。
- **免费使用方式**：开源可自部署，MIT 许可证，全部功能免费，无付费层、无需信用卡。依赖 LangGraph（同为开源），模型调用费用自理。项目较新（71 star），建议评估后再用于生产。
- **官网**：https://github.com/wanmol/goal-flow
- **GitHub**：https://github.com/wanmol/goal-flow
- **文档**：-
- **最后更新日期**：2026-08-06
- **发现渠道**：GitHub

### 4. Approving

- **功能描述**：开源、可自托管的 Agent 交付流水线平台，把编码 Agent 的执行过程变成「可视化、可评审、可恢复」的工作流。每个 Agent 在真实 Docker 沙箱中运行，节点之间以结构化 artifact 交换产物，并在关键节点自动暂停等待人工 Approve 后再继续。与 WorkBench 相似度：中高——具备多 Agent 编排、沙箱化工具执行、人机协同审批与断点恢复；偏交付治理而非通用 Agent 构建。适用场景：需要合规审批留痕的团队级 AI 编码交付、把不可控的 Agent 长跑变成分段可回滚的流程。
- **免费使用方式**：开源可自部署，MIT 许可证，代码与自托管部署完全免费，无需信用卡。需要本机或服务器可运行 Docker。官网 approving-ai.com 未公开托管版定价（unknown）。
- **官网**：https://www.approving-ai.com
- **GitHub**：https://github.com/cocofhu/approving
- **文档**：-
- **最后更新日期**：2026-08-08
- **发现渠道**：GitHub

### 5. Coldtea

- **功能描述**：2026-08-07 在 Product Hunt 发布（当日 469 赞）的 agentic IDE，主张「让软件交付自动驾驶」。把三类 Agent 收进同一个本地工作区：终端里的编码 Agent 可以成组启动、互相 review 与协作；视觉 QA Agent 把自然语言描述的 Web/移动端用户旅程转成自愈测试，在每个 PR 预览环境上跑全量套件并对部署做门禁；监控 Agent 盯着 Sentry / Datadog / Grafana / New Relic / PostHog / Vercel 的错误日志、用户会话与客户反馈，自行调查后直接开 PR 提修复。另有 Tasks 面板同步研发看板、把任务派给云端后台 Agent 并行跑。兼容 Claude Code、Codex、OpenCode 等现有 CLI Agent，代码默认留在本机，云端执行为可选项。与 WorkBench 相似度：高——多 Agent 编排、工具调用、后台/定时任务、本地文件与浏览器自动化俱全。适用场景：已用编码 Agent 但卡在回归测试与线上问题响应的工程团队。
- **免费使用方式**：Freemium。官方 FAQ 明确：终端（多 Agent 编码工作区）永久免费（free forever）；agentic testing 提供「generous free tier」；生产监控可免费试用（free to try）。付费档价格官网未公开（unknown）。目前仅 macOS 客户端，Windows/Linux 在等待列表。注册未见强制信用卡要求。
- **官网**：https://www.coldtea.ai/
- **GitHub**：-
- **文档**：https://www.coldtea.ai/
- **最后更新日期**：2026-08-07
- **发现渠道**：ProductHunt

### 6. Rindler

- **功能描述**：2026-08-07 Product Hunt 发布（247 赞）的网页任务自动化 Agent。与「每次让浏览器 Agent 现场看页面猜操作」的做法不同，Rindler 预先把网站测绘成一张「地图」——记录站点有哪些界面、每个界面能做什么动作、动作返回什么字段，已测绘 1000+ 站点；运行时 Agent 直接调用地图，因此每次返回的字段名与结构完全一致，速度与成本也不随次数线性增长。单次运行内按步骤动态选择传输方式（真实浏览器点击 或 直接调站点自有接口）。每张地图每天对真实站点做一次校验，页面改版由官方修复；运行中单步失败则由模型现场重解该步。支持自然语言下单、自动登录、按计划定时重复执行，并提供 HTTP MCP Server（mcp.rindler.ai）供自有后端调用。与 WorkBench 相似度：中高——浏览器自动化 + 定时任务 + MCP 工具调用，但不做通用 Agent 构建。适用场景：无 API 的后台系统批量取数、重复性网页操作外包给 Agent。
- **免费使用方式**：有免费可用途径但非永久免费层：Starter 档 $100/月含 100 次 session，附带 7 天免费试用并免费为你测绘一个指定站点；Teams 档 $1000/月含 1000 次 session 与定时自动化。所有档位单次 session 均为 $1，失败的运行不计费。另提供无需注册的公开 playground（chat.rindler.ai），预置若干站点可直接试用。试用是否需要信用卡官网未说明（unknown）。
- **官网**：https://rindler.ai
- **GitHub**：-
- **文档**：https://chat.rindler.ai/
- **最后更新日期**：2026-08-07
- **发现渠道**：ProductHunt

### 7. CopilotKit Channels SDK

- **功能描述**：CopilotKit（AG-UI 协议作者，GitHub 36.6k star）于 2026-08-06 发布的新模块，解决「Agent 建好了但用户不在你的 Web App 里」的最后一公里。用一套共享的 Channels JSX 写一次交互，自动在 Slack 渲染原生 Block Kit、在 Microsoft Teams 渲染 Adaptive Cards，Discord、WhatsApp、Telegram 在路上。已部署的 Agent 会为每个频道会话单独初始化，支持流式回复、工具结果回传、以及用原生卡片做人工审批（human-in-the-loop）而不必跳转到另一个后台。可接入 LangGraph、CrewAI、Microsoft Agent Framework 或任何自定义 AG-UI Agent。与 WorkBench 相似度：中高——不是从零构建 Agent，而是给已有 Agent 补齐多渠道交付、审批与状态持久化这层编排能力。适用场景：把内部 Agent 铺到团队日常协作工具里。
- **免费使用方式**：CopilotKit 主仓库 MIT 开源可自托管（36,640 star，2026-08-09 仍有提交），Channels SDK 随开源栈发布，官方提供完整可克隆的示例仓库 CopilotKit/OpenTag。托管侧的 CopilotKit Intelligence（负责 Slack/Teams 的 provider 连接、投递重试、持久化频道状态）为官方运营服务，其定价与免费额度官网未公开（unknown）；纯自托管路径无需付费、无需信用卡。
- **官网**：https://copilotkit.ai/channels
- **GitHub**：https://github.com/CopilotKit/CopilotKit
- **文档**：https://docs.copilotkit.ai/channels
- **最后更新日期**：2026-08-09
- **发现渠道**：社区

### 8. Open Minis

- **功能描述**：跨 iOS / Android 的开源端侧 AI Agent 应用，2026-08-03 登上 Product Hunt（90 赞）后在国内外 AI 工具导航站快速铺开。它给模型配了一台「真正的电脑」：手机内跑一个沙箱化 Alpine Linux shell（iOS 用 iSH、Android 用 PRoot），Agent 可以装软件包、跑 Python、改真实文件、驱动浏览器；外围 30+ 原生桥接打通 HealthKit、HomeKit、日历、提醒事项、通讯录、蓝牙、剪贴板、媒体与闹钟。带 SKILL.md 技能系统与持久记忆，为 Claude / Codex / OpenClaw 写的 Skills 基本可直接复用；多 Workspace 隔离各自上下文。自带模型（Claude、GPT、Gemini、Kimi、Grok 或任意 OpenAI 兼容端点），API Key 与数据不离开手机。与 WorkBench 相似度：高——agent loop、工具调用、技能生态、本地文件系统访问、浏览器自动化、记忆系统全覆盖，差异在于运行载体是手机而非桌面。适用场景：移动端个人自动化、智能家居与健康数据联动、随身可用的 Agent 工作区。
- **免费使用方式**：完全免费且开源，GPL-3.0 许可证（主仓库 3,403 star，技能库 MinisSkills 为 MIT，用例库 AwesomeMinis 为 CC0）。App 本身不收费、无内购层、无需信用卡；唯一成本是自带的模型 API Key 消耗。所有数据与密钥仅存本机。
- **官网**：https://openminis.app
- **GitHub**：https://github.com/OpenMinis/OpenMinis
- **文档**：https://github.com/OpenMinis/MinisSkills
- **最后更新日期**：2026-08-01
- **发现渠道**：导航站
