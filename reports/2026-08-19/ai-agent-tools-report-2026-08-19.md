# 每日 AI Agent 工具扫描报告 - 2026-08-19

> 搜索截止日期：2026-08-19 ｜ 生成时间：2026-08-19 15:50:27 ｜ 发现工具数：11

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | Superpowers（obra） | agentic skills 框架与软件开发方法论：把 agent 能力定义为可版本化、可组合的 shell 脚本 + markdown 技能文件，跨 agent（Claude/Codex/Gemini）可移植、可审计。相似度 中高（偏 agent 技能/能力构建，非可视化编排），适合 DevOps 与可审计的生产级 agent 工作流。 | 完全免费开源（MIT），自托管，无使用费用，仅自管基础设施成本；脚本/包安装即可（install.sh）。 | [官网](https://github.com/obra/superpowers) / [GitHub](https://github.com/obra/superpowers) | 2026-08-13 | GitHub |
| 2 | oh-my-claudecode（Yeachan-Heo） | 面向团队的多 agent 编排层（运行于 Claude Code 之上）：并行编排多个 Claude Code 实例，处理工作分发、冲突解决与上下文共享，提供团队级共享记忆与任务队列。相似度 高（多 agent 协作编排），适合已采用 Claude Code 的工程团队规模化使用。 | 完全免费开源（MIT），自托管；需自备 Claude API Key（BYOK），无平台费。 | [官网](https://oh-my-claudecode.dev) / [GitHub](https://github.com/Yeachan-Heo/oh-my-claudecode) | 2026-08-18 | GitHub |
| 3 | Deep Agents（LangChain） | batteries-included agent harness：开箱即用的高层 agent，支持子 agent、文件系统、上下文管理、shell 执行、持久记忆、human-in-the-loop、skills 与任意 MCP；构建于 LangGraph（持久化/checkpoint/streaming + 一等公民 tracing/eval）。相似度 高（生产级 agent 构建/编排），适合不想从 LangGraph 底层搭起、又要求可扩展的团队。 | 完全免费开源（MIT），自托管或用 LangSmith Cloud（可选）；模型无关，支持任意支持 tool calling 的 LLM（前沿/开源/本地）。 | [官网](https://docs.langchain.com/deepagents) / [GitHub](https://github.com/langchain-ai/deepagents) / [文档](https://docs.langchain.com/deepagents) | 2026-08-19 | GitHub |
| 4 | Mission Control（Builderz Labs） | 自托管 AI agent 控制平面：在一个本地仪表盘统一调度任务、运行多 agent 工作流、审查运行、追踪花费并治理 OpenClaw / Claude Code / Codex 等运行时。相似度 高（agent 编排与运维治理），适合需要统一管控多个运行时 agent 的团队。 | 完全免费开源（MIT），自托管（SQLite + Docker），无平台费；运行时本身 BYOK。 | [官网](https://mc.builderz.dev) / [GitHub](https://github.com/builderz-labs/mission-control) | 2026-08-18 | GitHub |
| 5 | Dograh | 开源语音 AI agent 平台，Vapi / Retell 的自托管替代：可视化流程构建器、Speech-to-Speech（70+ 语言）、电话落地 + 人工暖转接、通话录音与自动 QA、免费 REST API，MCP 原生。相似度 中高（垂直领域 agent 构建 —— 语音 agent 平台）。 | 完全免费开源（BSD-2-Clause），一条命令自托管，无门控、无按分钟计费；BYOK 或本地模型离线运行；数据不出本地服务器。 | [官网](https://app.dograh.com) / [GitHub](https://github.com/dograh-hq/dograh) | 2026-08-18 | ProductHunt |
| 6 | MetaBot（xvirobotics） | 受监督、自我进化的 Agent 组织基础设施：飞书 / Telegram 手机端运行 Claude Code 或 Kimi Code（双引擎，原生订阅直连），提供共享记忆、Agent 工厂、定时任务与通信总线。相似度 中高（多 agent 组织 / 协作 + 定时自动化）。 | 完全免费开源（MIT），自托管；需自备 Claude / Kimi 订阅（原生订阅直连）；仓库未声明的部分以 LICENSE 为准。 | [官网](https://xvirobotics.com/metabot/) / [GitHub](https://github.com/xvirobotics/metabot) | 2026-08-08 | GitHub |
| 7 | Captain Claw（kstevica） | 自托管框架，编排专家型 agent 编队：6 种编排模式、48 个内置工具 / agent、6 层共享记忆、31 个即用专家、完整 agentic 编码流水线（plan → review → ship），模型无关、本地友好（Ollama / OpenAI / Claude / Gemini / DeepSeek）。相似度 高（多 agent 编排 + 编码流水线）。 | 完全免费开源（MIT），自托管；支持本地模型（Ollama）100% 离线运行；无使用费用。 | [官网](https://captain-claw.com) / [GitHub](https://github.com/kstevica/captain-claw) | 2026-08-01 | GitHub |
| 8 | AgentLoom（linora-u） | 面向多 agent AI 应用的轻量工作流编排框架：YAML 声明式配置，内置运行时安全、可观测性与断点续传（resume）能力。相似度 高（多 agent 工作流编排）。 | 免费开源（许可证 unknown —— 仓库未声明 LICENSE 文件，以仓库为准），自托管；需自备 LLM API 或本地模型。 | [官网](https://github.com/linora-u/AgentLoom) / [GitHub](https://github.com/linora-u/AgentLoom) | 2026-08-13 | 开发者社区 |
| 9 | Keystroke（YC 背书） | 一体化内部 agent 与工作流构建平台：用自然语言或 TypeScript 描述，内置 agent 构建器即生成真实 TS 代码、连接工具、测试并部署到共享工作区；支持记忆、工作流、触发器、人工审批、1000+ 集成、任意 API / MCP；亦可用 Cursor / Claude Code / Codex 直接构建。相似度 高（agent + 工作流可视化/代码双模构建平台）。 | 开源（ELv2 许可证），YC 背书；开放 alpha 阶段，注册即赠 $20 免费额度，可免费试用；托管版含免费档（用量计费）。 | [官网](https://keystroke.ai) / [GitHub](https://github.com/keystrokehq/keystroke) / [文档](https://keystroke.ai/docs) | unknown | ProductHunt |
| 10 | Assembly Studio | 面向专业服务公司的 AI 应用构建器：用自然语言描述即可生成 onboarding agents、分析看板、社区中心等生产级应用，20+ 模板可混编，连接任意第三方工具。相似度 中（AI 应用 / agent 构建器，偏无代码应用生成）。 | 永久免费档（Free forever plan）；无需信用卡即可试用，按席位克隆替代高价 SaaS；高级 / 托管功能可能另行收费。 | [官网](https://studio.assembly.com) | unknown | ProductHunt |
| 11 | Airlock（airlockrun） | 自升级「赛博格」agent 平台：将 agent 编译为容器化的自治 Go 二进制，能用确定代码做的用代码、需判断的才调模型；支持 chat / web / cron / webhook 交互，通过 API 自升级生成新工具 / 修复错误，并管理 OAuth、存储、沙箱，桥接 Telegram / Discord。相似度 高（agent 运行时 / 自进化构建平台）。 | 开源（Apache-2.0），自托管（Docker），alpha 阶段免费；需自备模型 API（如 OpenAI / Claude）。 | [官网](https://github.com/airlockrun) / [GitHub](https://github.com/airlockrun/agentsdk) | 2026-08-19 | 开发者社区（Hacker News Show HN） |

## 详细信息

### 1. Superpowers（obra）

- **功能描述**：agentic skills 框架与软件开发方法论：把 agent 能力定义为可版本化、可组合的 shell 脚本 + markdown 技能文件，跨 agent（Claude/Codex/Gemini）可移植、可审计。相似度 中高（偏 agent 技能/能力构建，非可视化编排），适合 DevOps 与可审计的生产级 agent 工作流。
- **免费使用方式**：完全免费开源（MIT），自托管，无使用费用，仅自管基础设施成本；脚本/包安装即可（install.sh）。
- **官网**：https://github.com/obra/superpowers
- **GitHub**：https://github.com/obra/superpowers
- **文档**：-
- **最后更新日期**：2026-08-13
- **发现渠道**：GitHub

### 2. oh-my-claudecode（Yeachan-Heo）

- **功能描述**：面向团队的多 agent 编排层（运行于 Claude Code 之上）：并行编排多个 Claude Code 实例，处理工作分发、冲突解决与上下文共享，提供团队级共享记忆与任务队列。相似度 高（多 agent 协作编排），适合已采用 Claude Code 的工程团队规模化使用。
- **免费使用方式**：完全免费开源（MIT），自托管；需自备 Claude API Key（BYOK），无平台费。
- **官网**：https://oh-my-claudecode.dev
- **GitHub**：https://github.com/Yeachan-Heo/oh-my-claudecode
- **文档**：-
- **最后更新日期**：2026-08-18
- **发现渠道**：GitHub

### 3. Deep Agents（LangChain）

- **功能描述**：batteries-included agent harness：开箱即用的高层 agent，支持子 agent、文件系统、上下文管理、shell 执行、持久记忆、human-in-the-loop、skills 与任意 MCP；构建于 LangGraph（持久化/checkpoint/streaming + 一等公民 tracing/eval）。相似度 高（生产级 agent 构建/编排），适合不想从 LangGraph 底层搭起、又要求可扩展的团队。
- **免费使用方式**：完全免费开源（MIT），自托管或用 LangSmith Cloud（可选）；模型无关，支持任意支持 tool calling 的 LLM（前沿/开源/本地）。
- **官网**：https://docs.langchain.com/deepagents
- **GitHub**：https://github.com/langchain-ai/deepagents
- **文档**：https://docs.langchain.com/deepagents
- **最后更新日期**：2026-08-19
- **发现渠道**：GitHub

### 4. Mission Control（Builderz Labs）

- **功能描述**：自托管 AI agent 控制平面：在一个本地仪表盘统一调度任务、运行多 agent 工作流、审查运行、追踪花费并治理 OpenClaw / Claude Code / Codex 等运行时。相似度 高（agent 编排与运维治理），适合需要统一管控多个运行时 agent 的团队。
- **免费使用方式**：完全免费开源（MIT），自托管（SQLite + Docker），无平台费；运行时本身 BYOK。
- **官网**：https://mc.builderz.dev
- **GitHub**：https://github.com/builderz-labs/mission-control
- **文档**：-
- **最后更新日期**：2026-08-18
- **发现渠道**：GitHub

### 5. Dograh

- **功能描述**：开源语音 AI agent 平台，Vapi / Retell 的自托管替代：可视化流程构建器、Speech-to-Speech（70+ 语言）、电话落地 + 人工暖转接、通话录音与自动 QA、免费 REST API，MCP 原生。相似度 中高（垂直领域 agent 构建 —— 语音 agent 平台）。
- **免费使用方式**：完全免费开源（BSD-2-Clause），一条命令自托管，无门控、无按分钟计费；BYOK 或本地模型离线运行；数据不出本地服务器。
- **官网**：https://app.dograh.com
- **GitHub**：https://github.com/dograh-hq/dograh
- **文档**：-
- **最后更新日期**：2026-08-18
- **发现渠道**：ProductHunt

### 6. MetaBot（xvirobotics）

- **功能描述**：受监督、自我进化的 Agent 组织基础设施：飞书 / Telegram 手机端运行 Claude Code 或 Kimi Code（双引擎，原生订阅直连），提供共享记忆、Agent 工厂、定时任务与通信总线。相似度 中高（多 agent 组织 / 协作 + 定时自动化）。
- **免费使用方式**：完全免费开源（MIT），自托管；需自备 Claude / Kimi 订阅（原生订阅直连）；仓库未声明的部分以 LICENSE 为准。
- **官网**：https://xvirobotics.com/metabot/
- **GitHub**：https://github.com/xvirobotics/metabot
- **文档**：-
- **最后更新日期**：2026-08-08
- **发现渠道**：GitHub

### 7. Captain Claw（kstevica）

- **功能描述**：自托管框架，编排专家型 agent 编队：6 种编排模式、48 个内置工具 / agent、6 层共享记忆、31 个即用专家、完整 agentic 编码流水线（plan → review → ship），模型无关、本地友好（Ollama / OpenAI / Claude / Gemini / DeepSeek）。相似度 高（多 agent 编排 + 编码流水线）。
- **免费使用方式**：完全免费开源（MIT），自托管；支持本地模型（Ollama）100% 离线运行；无使用费用。
- **官网**：https://captain-claw.com
- **GitHub**：https://github.com/kstevica/captain-claw
- **文档**：-
- **最后更新日期**：2026-08-01
- **发现渠道**：GitHub

### 8. AgentLoom（linora-u）

- **功能描述**：面向多 agent AI 应用的轻量工作流编排框架：YAML 声明式配置，内置运行时安全、可观测性与断点续传（resume）能力。相似度 高（多 agent 工作流编排）。
- **免费使用方式**：免费开源（许可证 unknown —— 仓库未声明 LICENSE 文件，以仓库为准），自托管；需自备 LLM API 或本地模型。
- **官网**：https://github.com/linora-u/AgentLoom
- **GitHub**：https://github.com/linora-u/AgentLoom
- **文档**：-
- **最后更新日期**：2026-08-13
- **发现渠道**：开发者社区

### 9. Keystroke（YC 背书）

- **功能描述**：一体化内部 agent 与工作流构建平台：用自然语言或 TypeScript 描述，内置 agent 构建器即生成真实 TS 代码、连接工具、测试并部署到共享工作区；支持记忆、工作流、触发器、人工审批、1000+ 集成、任意 API / MCP；亦可用 Cursor / Claude Code / Codex 直接构建。相似度 高（agent + 工作流可视化/代码双模构建平台）。
- **免费使用方式**：开源（ELv2 许可证），YC 背书；开放 alpha 阶段，注册即赠 $20 免费额度，可免费试用；托管版含免费档（用量计费）。
- **官网**：https://keystroke.ai
- **GitHub**：https://github.com/keystrokehq/keystroke
- **文档**：https://keystroke.ai/docs
- **最后更新日期**：unknown
- **发现渠道**：ProductHunt

### 10. Assembly Studio

- **功能描述**：面向专业服务公司的 AI 应用构建器：用自然语言描述即可生成 onboarding agents、分析看板、社区中心等生产级应用，20+ 模板可混编，连接任意第三方工具。相似度 中（AI 应用 / agent 构建器，偏无代码应用生成）。
- **免费使用方式**：永久免费档（Free forever plan）；无需信用卡即可试用，按席位克隆替代高价 SaaS；高级 / 托管功能可能另行收费。
- **官网**：https://studio.assembly.com
- **GitHub**：-
- **文档**：-
- **最后更新日期**：unknown
- **发现渠道**：ProductHunt

### 11. Airlock（airlockrun）

- **功能描述**：自升级「赛博格」agent 平台：将 agent 编译为容器化的自治 Go 二进制，能用确定代码做的用代码、需判断的才调模型；支持 chat / web / cron / webhook 交互，通过 API 自升级生成新工具 / 修复错误，并管理 OAuth、存储、沙箱，桥接 Telegram / Discord。相似度 高（agent 运行时 / 自进化构建平台）。
- **免费使用方式**：开源（Apache-2.0），自托管（Docker），alpha 阶段免费；需自备模型 API（如 OpenAI / Claude）。
- **官网**：https://github.com/airlockrun
- **GitHub**：https://github.com/airlockrun/agentsdk
- **文档**：-
- **最后更新日期**：2026-08-19
- **发现渠道**：开发者社区（Hacker News Show HN）
