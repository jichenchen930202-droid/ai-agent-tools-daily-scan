# 每日 AI Agent 工具扫描报告 - 2026-08-13

> 搜索截止日期：2026-08-13 ｜ 生成时间：2026-08-13 10:06:37 ｜ 发现工具数：5

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | Sim Studio | 可视化 AI 智能体/工作流构建与监控平台（sim.ai），画布拖拽编排 Agent 节点、工具、模块并即时运行，内置 Copilot 以自然语言生成节点/修复错误，支持向量数据库 RAG 与多模型（OpenAI/Claude/Gemini/Ollama 本地）。与 WorkBench 相似度：高 —— 同为可视化低代码 Agent 工作流编排 + 自托管 + 本地模型隐私优先，是 WorkBench 类「AI 员工/工作流指挥中心」的直接竞品。适用场景：创作者/运营/团队在不写代码的情况下快速搭建多 AI 协同的自动化工作流，或私有化部署保障数据安全。 | Apache-2.0 开源；可完全自托管（npx simstudio 一键拉起 Docker，或 docker compose 部署，支持 Ollama / vLLM 本地模型），也可使用 sim.ai 云版。自托管免费，仅模型 API 费用（对接 Ollama 本地模型可零成本）；云版含免费档与付费档。无信用卡要求（自备模型）。 | [官网](https://sim.ai) / [GitHub](https://github.com/simstudioai/sim) / [文档](https://docs.simstudio.ai/introduction) | 2026-08-12 | GitHub/导航站 |
| 2 | OpenJiuwen（openJiuwen AgentStudio） | 华为云 Stack 开源的通用 AI Agent 平台，提供零码/低码可视化开发、工作流编排、模型/知识库/插件统一资源管理；原生支持多智能体协同（Coordination Engineering 协同工程）与智能体自演进，含 agent-studio / agent-core / JiuwenSwarm / DeepSearch / SkillHub 等一整套 Apache-2.0 组件。与 WorkBench 相似度：高 —— 一站式可视化 Agent 开发+编排+部署+运营，定位与 WorkBench 高度重合，且强调多智能体协同与商用级稳定性。适用场景：企业/个人快速搭建生产级、可私有化部署的多智能体系统。 | Apache-2.0 开源（agent-studio、agent-core、jiuwenswarm 等核心仓库均为 Apache-2.0）；可完全自托管（Docker 部署，提供 deploy/ 统一脚本）；免费，仅自备模型与算力成本，无信用卡要求；支持零码/低码/SDK 多种开发方式。 | [官网](https://www.openjiuwen.com) / [GitHub](https://github.com/openJiuwen-ai/agent-studio) / [文档](https://github.com/openJiuwen-ai/community) | 2026-08-12 | GitHub/社区 |
| 3 | QM（yc-software/qm） | Y Combinator 于 2026-07-31 开源的「多人（multiplayer）智能体 harness for work」，为每个员工提供完全隔离的 AI 工作空间（独立记忆/文件/密钥/权限/定时任务/沙盒），员工可在同一 Slack 频道内协作而上下文互不泄漏；支持自定义 harness 与模型（Pi / OpenCode / Codex / Claude Code 驱动同一核心）、共享技能与后台 cron 任务。与 WorkBench 相似度：中高 —— 面向「企业级多员工 Agent 管理/隔离协作」的组织级 Agent 运行时，与 WorkBench 的私有化、多智能体协作定位互补。适用场景：小团队/初创公司免费自托管公司级 Agent 系统，解决共享 API Key 的安全灾难与按人头 SaaS 的成本灾难。 | MIT 开源；可自托管（qm init 部署到自有 Fly / AWS 云账号，或私有 fork 定制）；免费，仅模型 API 成本；无信用卡要求。 | [官网](https://github.com/yc-software/qm) / [GitHub](https://github.com/yc-software/qm) | 2026-08-12 | GitHub |
| 4 | Kiro Crew（kirodotdev/KiroCrew） | AWS 于 2026-08-04 开源的持久化 Agent 工作空间/编排器，把 AI 编码 Agent 从「单次会话助手」升级为可 7×24 无人值守运行的工程队友：多 Agent 与子 Agent 编排、跨会话持久记忆、定时任务与心跳监控，可通过桌面应用 / Web 仪表盘 / Slack / Telegram / Discord / 企业微信远程操控；内部以 MeshClaw 孵化，半年内被 3.9 万+ Amazon 开发者采用。与 WorkBench 相似度：中 —— 偏「持久化、可编排、跨会话的工程 Agent 工作空间」，与 WorkBench 的自托管/本地优先定位相符。适用场景：已在用 Kiro 的团队做低摩擦增量（读现有 .kiro 配置），或作为可自托管的 Agent 编排试验田。 | 编排层 Apache-2.0 开源、可自托管（Gateway / Agent 运行时 / 状态均跑在用户自有机器，无需 AWS 账号）；但驱动引擎为 AWS 专有 kiro-cli，按 credits 计费（免费层 50 credits/月，Pro $20/月起）。即仅编排层免费开源，智能体实际执行依赖 Kiro 账户/CLI 额度——自托管不托管「智能」。 | [官网](https://kiro.dev/) / [GitHub](https://github.com/kirodotdev/KiroCrew) / [文档](https://kiro.dev/docs/crew/) | 2026-08-04 | GitHub |
| 5 | OpenClaw（openclaw/openclaw） | 成熟的本地优先开源个人 AI 智能体框架（前身 Clawdbot / Moltbot，2026 年初定名 OpenClaw），以消息平台（WhatsApp / Telegram / Slack / Discord / 微信等 100+ 渠道）为主要交互界面，具备自主任务执行、持久记忆、Skills 插件生态（ClawHub）、多智能体路由与本地网关架构。与 WorkBench 相似度：中 —— 偏「个人/团队自托管 Agent 运行时 + 消息驱动」，与 WorkBench 的本地优先/自托管定位相符，但形态为终端用户 Agent 而非低代码构建平台。适用场景：在自有硬件 7×24 运行可接管日常任务的个人 AI 助手，数据不出本机。注：此为已 established 的标志性免费自托管 Agent 项目（非本月新发布），因尚未被本扫描收录且免费价值突出，本次一并补录。 | MIT 开源；完全自托管（本地 Mac/VPS/树莓派，官方 Docker 镜像，Windows 经 WSL2）；免费，仅模型 API 或本地模型成本，无信用卡要求；核心机器人无订阅费，可选托管服务（Capable.ai 等）才收费。社区规模极大且每日活跃开发，但各聚合站点 star 数差异较大（18 万~38 万不等），未能权威核实精确数值，故标 unknown。 | [官网](https://openclaw.ai) / [GitHub](https://github.com/openclaw/openclaw) / [文档](https://docs.openclaw.ai) | unknown | GitHub/社区 |

## 详细信息

### 1. Sim Studio

- **功能描述**：可视化 AI 智能体/工作流构建与监控平台（sim.ai），画布拖拽编排 Agent 节点、工具、模块并即时运行，内置 Copilot 以自然语言生成节点/修复错误，支持向量数据库 RAG 与多模型（OpenAI/Claude/Gemini/Ollama 本地）。与 WorkBench 相似度：高 —— 同为可视化低代码 Agent 工作流编排 + 自托管 + 本地模型隐私优先，是 WorkBench 类「AI 员工/工作流指挥中心」的直接竞品。适用场景：创作者/运营/团队在不写代码的情况下快速搭建多 AI 协同的自动化工作流，或私有化部署保障数据安全。
- **免费使用方式**：Apache-2.0 开源；可完全自托管（npx simstudio 一键拉起 Docker，或 docker compose 部署，支持 Ollama / vLLM 本地模型），也可使用 sim.ai 云版。自托管免费，仅模型 API 费用（对接 Ollama 本地模型可零成本）；云版含免费档与付费档。无信用卡要求（自备模型）。
- **官网**：https://sim.ai
- **GitHub**：https://github.com/simstudioai/sim
- **文档**：https://docs.simstudio.ai/introduction
- **最后更新日期**：2026-08-12
- **发现渠道**：GitHub/导航站

### 2. OpenJiuwen（openJiuwen AgentStudio）

- **功能描述**：华为云 Stack 开源的通用 AI Agent 平台，提供零码/低码可视化开发、工作流编排、模型/知识库/插件统一资源管理；原生支持多智能体协同（Coordination Engineering 协同工程）与智能体自演进，含 agent-studio / agent-core / JiuwenSwarm / DeepSearch / SkillHub 等一整套 Apache-2.0 组件。与 WorkBench 相似度：高 —— 一站式可视化 Agent 开发+编排+部署+运营，定位与 WorkBench 高度重合，且强调多智能体协同与商用级稳定性。适用场景：企业/个人快速搭建生产级、可私有化部署的多智能体系统。
- **免费使用方式**：Apache-2.0 开源（agent-studio、agent-core、jiuwenswarm 等核心仓库均为 Apache-2.0）；可完全自托管（Docker 部署，提供 deploy/ 统一脚本）；免费，仅自备模型与算力成本，无信用卡要求；支持零码/低码/SDK 多种开发方式。
- **官网**：https://www.openjiuwen.com
- **GitHub**：https://github.com/openJiuwen-ai/agent-studio
- **文档**：https://github.com/openJiuwen-ai/community
- **最后更新日期**：2026-08-12
- **发现渠道**：GitHub/社区

### 3. QM（yc-software/qm）

- **功能描述**：Y Combinator 于 2026-07-31 开源的「多人（multiplayer）智能体 harness for work」，为每个员工提供完全隔离的 AI 工作空间（独立记忆/文件/密钥/权限/定时任务/沙盒），员工可在同一 Slack 频道内协作而上下文互不泄漏；支持自定义 harness 与模型（Pi / OpenCode / Codex / Claude Code 驱动同一核心）、共享技能与后台 cron 任务。与 WorkBench 相似度：中高 —— 面向「企业级多员工 Agent 管理/隔离协作」的组织级 Agent 运行时，与 WorkBench 的私有化、多智能体协作定位互补。适用场景：小团队/初创公司免费自托管公司级 Agent 系统，解决共享 API Key 的安全灾难与按人头 SaaS 的成本灾难。
- **免费使用方式**：MIT 开源；可自托管（qm init 部署到自有 Fly / AWS 云账号，或私有 fork 定制）；免费，仅模型 API 成本；无信用卡要求。
- **官网**：https://github.com/yc-software/qm
- **GitHub**：https://github.com/yc-software/qm
- **文档**：-
- **最后更新日期**：2026-08-12
- **发现渠道**：GitHub

### 4. Kiro Crew（kirodotdev/KiroCrew）

- **功能描述**：AWS 于 2026-08-04 开源的持久化 Agent 工作空间/编排器，把 AI 编码 Agent 从「单次会话助手」升级为可 7×24 无人值守运行的工程队友：多 Agent 与子 Agent 编排、跨会话持久记忆、定时任务与心跳监控，可通过桌面应用 / Web 仪表盘 / Slack / Telegram / Discord / 企业微信远程操控；内部以 MeshClaw 孵化，半年内被 3.9 万+ Amazon 开发者采用。与 WorkBench 相似度：中 —— 偏「持久化、可编排、跨会话的工程 Agent 工作空间」，与 WorkBench 的自托管/本地优先定位相符。适用场景：已在用 Kiro 的团队做低摩擦增量（读现有 .kiro 配置），或作为可自托管的 Agent 编排试验田。
- **免费使用方式**：编排层 Apache-2.0 开源、可自托管（Gateway / Agent 运行时 / 状态均跑在用户自有机器，无需 AWS 账号）；但驱动引擎为 AWS 专有 kiro-cli，按 credits 计费（免费层 50 credits/月，Pro $20/月起）。即仅编排层免费开源，智能体实际执行依赖 Kiro 账户/CLI 额度——自托管不托管「智能」。
- **官网**：https://kiro.dev/
- **GitHub**：https://github.com/kirodotdev/KiroCrew
- **文档**：https://kiro.dev/docs/crew/
- **最后更新日期**：2026-08-04
- **发现渠道**：GitHub

### 5. OpenClaw（openclaw/openclaw）

- **功能描述**：成熟的本地优先开源个人 AI 智能体框架（前身 Clawdbot / Moltbot，2026 年初定名 OpenClaw），以消息平台（WhatsApp / Telegram / Slack / Discord / 微信等 100+ 渠道）为主要交互界面，具备自主任务执行、持久记忆、Skills 插件生态（ClawHub）、多智能体路由与本地网关架构。与 WorkBench 相似度：中 —— 偏「个人/团队自托管 Agent 运行时 + 消息驱动」，与 WorkBench 的本地优先/自托管定位相符，但形态为终端用户 Agent 而非低代码构建平台。适用场景：在自有硬件 7×24 运行可接管日常任务的个人 AI 助手，数据不出本机。注：此为已 established 的标志性免费自托管 Agent 项目（非本月新发布），因尚未被本扫描收录且免费价值突出，本次一并补录。
- **免费使用方式**：MIT 开源；完全自托管（本地 Mac/VPS/树莓派，官方 Docker 镜像，Windows 经 WSL2）；免费，仅模型 API 或本地模型成本，无信用卡要求；核心机器人无订阅费，可选托管服务（Capable.ai 等）才收费。社区规模极大且每日活跃开发，但各聚合站点 star 数差异较大（18 万~38 万不等），未能权威核实精确数值，故标 unknown。
- **官网**：https://openclaw.ai
- **GitHub**：https://github.com/openclaw/openclaw
- **文档**：https://docs.openclaw.ai
- **最后更新日期**：unknown
- **发现渠道**：GitHub/社区
