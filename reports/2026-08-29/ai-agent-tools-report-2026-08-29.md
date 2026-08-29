# 每日 AI Agent 工具扫描报告 - 2026-08-29

> 搜索截止日期：2026-08-29 ｜ 生成时间：2026-08-29 12:58:51 ｜ 发现工具数：6

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | AgentZ (AccuKnox) | 零信任 AI Agent 平台，统一构建 / 运行 / 治理 AI 代理。采用「组织-工作区-代理-工作流-沙箱」模型：每个代理在独立沙箱内执行（可配置 vCPU/内存/文件系统/域名白名单/网络访问），运行时注入凭据、工具级权限、可视化工作流图与执行轨迹/审计日志；模型无关，支持 OpenAI、Claude、Grok 及自带大模型（BYOLLM），支持 SaaS、本地部署与隔离（air-gapped）部署。相似度：高——与 WorkBench 同为「Agent 构建 + 编排 + 治理」一体化平台，且支持自带模型与自托管，定位企业级生产落地。 | 托管 SaaS 提供免费计划（agentzharness.ai，可用 GitHub / Google 登录，免费构建并运行代理、工作流与技能、沙箱执行）；企业 / 自管与隔离部署需联系销售定价；开源仓库 Apache-2.0，可自行克隆自托管（无平台软件费，仅付模型与算力）。 | [官网](https://agentzharness.ai) / [GitHub](https://github.com/accuknox/agentZ) / [文档](https://github.com/accuknox/agentZ) | 2026-08-28 | GitHub |
| 2 | Oasis | 多人 AI 工作空间，让人类与 AI 代理作为「平等队友」在同一 Room 内协作。支持通过模板（销售研究、客服、代码审查、招聘等）快速创建代理团队，共享记忆随使用复利增长；路由 Claude / GPT / Gemini 及开源模型，可连接 Devin、Manus、Claude Code 等外部代理，Mac 原生应用将本地代理无配置桥接进 Room；代理具备名称、角色、系统提示、模型与可选工具（Gmail、Linear 等）。相似度：中——偏「多代理协作 / 编排工作空间」，团队级人类+Agent 协同，并非完全低代码构建器，但具备协调 Agent 团队、策略与审批能力，与 WorkBench 工作流编排场景相关。 | Freemium。Free 档 $0/月：最多 3 席位、10 个集成、10 个定时 Room/月、可使用开源模型；Starter $19/月（10 席位、25 集成、20 定时 Room、全模型按量）；Pro $199/月（50 席位、SSO、审计、导出）；付费计划支持自带 API Key 按量计费；免费档无需信用卡即可试用。 | [官网](https://joinoasis.com) / [文档](https://joinoasis.com) | unknown | ProductHunt |
| 3 | Heym | 源代码可见（source-available）的多智能体工作流平台，可在自有基础设施上构建并运行 agentic 系统。可视化构建多代理工作流、连接自有数据与工具、接入 Codex / OpenCode 等编码代理、在关键节点加入人工审批；内置 traces、成本、延迟与 evals 可观测性；可将工作流暴露为 Portal、API 或 MCP 工具。相似度：高——与 WorkBench 同为「可视化多代理工作流编排 + 自托管」平台，强调自带模型与凭据、数据驻留可控。 | 自托管免费（source-available，自带模型与凭据，无平台软件费；具体许可证未公开确认，非完全开源）；ProductHunt 标注「free and available today」。注：许可证性质以官方仓库为准，本报告中记为 unknown。 | [官网](https://www.producthunt.com/products/heym) / [文档](https://www.producthunt.com/products/heym) | unknown | ProductHunt |
| 4 | Headlong | Laude Institute（MIT 关联）开源的 agent microharness，核心不到 10k 行 Bash 实现「持久智能体（persistent agency）」——agent 在无人交互时也持续自主思考/行动，外部消息以 observation 形式注入统一的连续思想流。提供 shellm（递归 LLM 核心）、traj（轨迹 DAG）、context（分层压缩）、mem/skills 等可组合小工具，支持 Slack/Telegram/Web 多端协作、Docker 沙箱与子代理。相似度：高——同属可自托管、可编排多步任务/多智能体、带工具调用与记忆系统的 agent 运行时；区别在于 Headlong 以 Bash 为唯一工具、强调常驻自治而非按需响应。 | 完全开源（Apache-2.0），可自托管、免费使用；仅需自备 LLM API Key（Anthropic/OpenAI/Gemini/OpenRouter，BYOK），无固定费用。后台思考循环按 token 计费约 $1–2/小时，官方建议用限额 API Key 防失控。alpha 研究软件，建议沙箱内运行。 | [官网](https://headlong.ai) / [GitHub](https://github.com/laude-institute/headlong) / [文档](https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents) | 2026-08-29 | GitHub |
| 5 | openhuman | tinyhumansai 开源的个人 AI 超级智能（Personal AI super intelligence）：本地优先（local-first）的「记忆树（Memory Tree）」沉淀你的数字生活，作为 agent 集群与工作流的高效编排器（orchestrator of agent fleets and workflows），并具备深度研究能力。相似度：高——同属可自托管、带持久记忆与多智能体编排的 agent 平台/运行时，面向个人自动化与知识中枢；区别在于 openhuman 强调本地优先的个人记忆大脑，而非团队工作流编排。 | 完全开源（GPL-3.0），可自托管、免费使用；本地优先架构，数据留在本地，仅需自备大模型 API 或本地模型。beta 阶段已快速积累约 3.9 万星，无信用卡要求。 | [官网](https://tinyhumans.ai/openhuman) / [GitHub](https://github.com/tinyhumansai/openhuman) | 2026-08-27 | GitHub |
| 6 | OpenBot | CopilotKit 开源的「AI 同事（AI coworkers）」框架：每个 agent 拥有独立的电脑（浏览器 + 文件 + 工具），且每个动作在发生时先经治理闸门审批、执行后被记录（action approved before it happens, recorded after）。可接入任意 AG-UI agent，内置容器化与治理（agent governance）。相似度：高——同属可自托管、多智能体并行、带工具调用/浏览器自动化/治理审计的 agent 构建与编排平台，且 CopilotKit 生态成熟（MCP / AG-UI / Generative UI）。 | 完全开源（MIT），可自托管、免费使用；接入自有模型或 AG-UI agent（BYOK），无固定费用，无信用卡要求。CopilotKit 另有商业托管层，但 OpenBot 本体开源免费。 | [官网](https://www.copilotkit.ai/openbot) / [GitHub](https://github.com/CopilotKit/OpenBot) | 2026-08-28 | GitHub |

## 详细信息

### 1. AgentZ (AccuKnox)

- **功能描述**：零信任 AI Agent 平台，统一构建 / 运行 / 治理 AI 代理。采用「组织-工作区-代理-工作流-沙箱」模型：每个代理在独立沙箱内执行（可配置 vCPU/内存/文件系统/域名白名单/网络访问），运行时注入凭据、工具级权限、可视化工作流图与执行轨迹/审计日志；模型无关，支持 OpenAI、Claude、Grok 及自带大模型（BYOLLM），支持 SaaS、本地部署与隔离（air-gapped）部署。相似度：高——与 WorkBench 同为「Agent 构建 + 编排 + 治理」一体化平台，且支持自带模型与自托管，定位企业级生产落地。
- **免费使用方式**：托管 SaaS 提供免费计划（agentzharness.ai，可用 GitHub / Google 登录，免费构建并运行代理、工作流与技能、沙箱执行）；企业 / 自管与隔离部署需联系销售定价；开源仓库 Apache-2.0，可自行克隆自托管（无平台软件费，仅付模型与算力）。
- **官网**：https://agentzharness.ai
- **GitHub**：https://github.com/accuknox/agentZ
- **文档**：https://github.com/accuknox/agentZ
- **最后更新日期**：2026-08-28
- **发现渠道**：GitHub

### 2. Oasis

- **功能描述**：多人 AI 工作空间，让人类与 AI 代理作为「平等队友」在同一 Room 内协作。支持通过模板（销售研究、客服、代码审查、招聘等）快速创建代理团队，共享记忆随使用复利增长；路由 Claude / GPT / Gemini 及开源模型，可连接 Devin、Manus、Claude Code 等外部代理，Mac 原生应用将本地代理无配置桥接进 Room；代理具备名称、角色、系统提示、模型与可选工具（Gmail、Linear 等）。相似度：中——偏「多代理协作 / 编排工作空间」，团队级人类+Agent 协同，并非完全低代码构建器，但具备协调 Agent 团队、策略与审批能力，与 WorkBench 工作流编排场景相关。
- **免费使用方式**：Freemium。Free 档 $0/月：最多 3 席位、10 个集成、10 个定时 Room/月、可使用开源模型；Starter $19/月（10 席位、25 集成、20 定时 Room、全模型按量）；Pro $199/月（50 席位、SSO、审计、导出）；付费计划支持自带 API Key 按量计费；免费档无需信用卡即可试用。
- **官网**：https://joinoasis.com
- **GitHub**：-
- **文档**：https://joinoasis.com
- **最后更新日期**：unknown
- **发现渠道**：ProductHunt

### 3. Heym

- **功能描述**：源代码可见（source-available）的多智能体工作流平台，可在自有基础设施上构建并运行 agentic 系统。可视化构建多代理工作流、连接自有数据与工具、接入 Codex / OpenCode 等编码代理、在关键节点加入人工审批；内置 traces、成本、延迟与 evals 可观测性；可将工作流暴露为 Portal、API 或 MCP 工具。相似度：高——与 WorkBench 同为「可视化多代理工作流编排 + 自托管」平台，强调自带模型与凭据、数据驻留可控。
- **免费使用方式**：自托管免费（source-available，自带模型与凭据，无平台软件费；具体许可证未公开确认，非完全开源）；ProductHunt 标注「free and available today」。注：许可证性质以官方仓库为准，本报告中记为 unknown。
- **官网**：https://www.producthunt.com/products/heym
- **GitHub**：-
- **文档**：https://www.producthunt.com/products/heym
- **最后更新日期**：unknown
- **发现渠道**：ProductHunt

### 4. Headlong

- **功能描述**：Laude Institute（MIT 关联）开源的 agent microharness，核心不到 10k 行 Bash 实现「持久智能体（persistent agency）」——agent 在无人交互时也持续自主思考/行动，外部消息以 observation 形式注入统一的连续思想流。提供 shellm（递归 LLM 核心）、traj（轨迹 DAG）、context（分层压缩）、mem/skills 等可组合小工具，支持 Slack/Telegram/Web 多端协作、Docker 沙箱与子代理。相似度：高——同属可自托管、可编排多步任务/多智能体、带工具调用与记忆系统的 agent 运行时；区别在于 Headlong 以 Bash 为唯一工具、强调常驻自治而非按需响应。
- **免费使用方式**：完全开源（Apache-2.0），可自托管、免费使用；仅需自备 LLM API Key（Anthropic/OpenAI/Gemini/OpenRouter，BYOK），无固定费用。后台思考循环按 token 计费约 $1–2/小时，官方建议用限额 API Key 防失控。alpha 研究软件，建议沙箱内运行。
- **官网**：https://headlong.ai
- **GitHub**：https://github.com/laude-institute/headlong
- **文档**：https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents
- **最后更新日期**：2026-08-29
- **发现渠道**：GitHub

### 5. openhuman

- **功能描述**：tinyhumansai 开源的个人 AI 超级智能（Personal AI super intelligence）：本地优先（local-first）的「记忆树（Memory Tree）」沉淀你的数字生活，作为 agent 集群与工作流的高效编排器（orchestrator of agent fleets and workflows），并具备深度研究能力。相似度：高——同属可自托管、带持久记忆与多智能体编排的 agent 平台/运行时，面向个人自动化与知识中枢；区别在于 openhuman 强调本地优先的个人记忆大脑，而非团队工作流编排。
- **免费使用方式**：完全开源（GPL-3.0），可自托管、免费使用；本地优先架构，数据留在本地，仅需自备大模型 API 或本地模型。beta 阶段已快速积累约 3.9 万星，无信用卡要求。
- **官网**：https://tinyhumans.ai/openhuman
- **GitHub**：https://github.com/tinyhumansai/openhuman
- **文档**：-
- **最后更新日期**：2026-08-27
- **发现渠道**：GitHub

### 6. OpenBot

- **功能描述**：CopilotKit 开源的「AI 同事（AI coworkers）」框架：每个 agent 拥有独立的电脑（浏览器 + 文件 + 工具），且每个动作在发生时先经治理闸门审批、执行后被记录（action approved before it happens, recorded after）。可接入任意 AG-UI agent，内置容器化与治理（agent governance）。相似度：高——同属可自托管、多智能体并行、带工具调用/浏览器自动化/治理审计的 agent 构建与编排平台，且 CopilotKit 生态成熟（MCP / AG-UI / Generative UI）。
- **免费使用方式**：完全开源（MIT），可自托管、免费使用；接入自有模型或 AG-UI agent（BYOK），无固定费用，无信用卡要求。CopilotKit 另有商业托管层，但 OpenBot 本体开源免费。
- **官网**：https://www.copilotkit.ai/openbot
- **GitHub**：https://github.com/CopilotKit/OpenBot
- **文档**：-
- **最后更新日期**：2026-08-28
- **发现渠道**：GitHub
