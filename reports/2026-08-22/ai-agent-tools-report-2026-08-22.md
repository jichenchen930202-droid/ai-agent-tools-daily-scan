# 每日 AI Agent 工具扫描报告 - 2026-08-22

> 搜索截止日期：2026-08-22 ｜ 生成时间：2026-08-22 10:06:20 ｜ 发现工具数：11

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | Codex Harness（OpenAI / openai/codex） | OpenAI 于 2026-08-19 全面开源的 Agent 底层执行框架（harness 层），提供 codex exec（非交互调用）、Codex SDK（程序化编排）、Codex app-server（持久会话）三层接口，将 Agent 循环（对话状态/工具调用/沙箱/流式/人工审批）作为可嵌入产品的底层执行引擎。与 WorkBench 相似度：高——同为 Agent 执行与编排基础设施，前后端解耦、可嵌入业务系统，模型无关。适用：已成熟业务界面需原生嵌入 Agent 执行并掌控审批流程的团队。 | Apache-2.0，可完全免费自部署/二次分发（含商用）。作为库/CLI/SDK 嵌入自有产品免费；默认对接 OpenAI API，模型调用需自备 OpenAI API Key 并按其计费，替换其他模型需自适配调用层。 | [官网](https://developers.openai.com/blog/codex-as-a-platform) / [GitHub](https://github.com/openai/codex) / [文档](https://developers.openai.com/blog/codex-as-a-platform) | 2026-08-22 | GitHub |
| 2 | TeamAI（腾讯 / Tencent/teamai-cli） | 腾讯 2026-08-21 开源的「团队 harness for AI agents」，核心思路是把 Git 仓库变成 AI Agent 的共享大脑：统一管理 Claude Code / Cursor 等编程 Agent 的技能与规则，支持「经验自动沉淀」（摩擦点触发后将解决问题的经验推送到团队共享库）、MCP 服务配置统一分发、基于 codebase 的知识图谱检索。与 WorkBench 相似度：中——偏 Agent 协作治理/对齐层，而非完整构建平台；Git-native 方案避开中心化平台。适用：多 Agent 规模化落地的团队对齐。 | 开源（许可证为 NOASSERTION/Other，非标准协议，商用前需确认条款）；可自托管。将 Git 仓库作为 Agent 共享记忆与规则层，无需中心化平台。 | [GitHub](https://github.com/Tencent/teamai-cli) | 2026-08-20 | 开发者社区 |
| 3 | QwenPaw（AgentScope / agentscope-ai/QwenPaw） | AgentScope 团队推出的本地优先、可自托管的个人 AI 助手（原 CoPaw），可同时接入即时通讯、邮件、日程等多个渠道，在本地维护统一上下文与三层记忆，支持自定义技能扩展；安装简单（本机或云端皆可部署）。与 WorkBench 相似度：高——多渠道个人智能体平台，技能/记忆/自托管，与 OpenClaw 类产品定位一致。适用：想要个人助理但不愿把生活数据交托云端者。 | Apache-2.0，完全免费自托管（本机或云端），无信用卡要求；需自备 LLM API Key（OpenAI/通义等），按所选模型计费。 | [官网](http://qwenpaw.agentscope.io/) / [GitHub](https://github.com/agentscope-ai/QwenPaw) / [文档](http://qwenpaw.agentscope.io/) | 2026-08-21 | GitHub |
| 4 | Open-SWE（LangChain / langchain-ai/open-swe） | LangChain 开源的异步编码 Agent 框架（开源版「内部 Devin」），基于 LangGraph 与 Deep Agents 构建，提供云沙箱、Slack/Linear/GitHub 调用、子 Agent 编排与自动 PR 创建，面向工程组织。与 WorkBench 相似度：中——内部编码 Agent 框架，偏研发自动化而非通用构建平台。适用：需要内部编码 Agent 的软件团队。 | MIT，开源免费自托管；提供云沙箱（可能按用量计费）与本地执行两种路径，模型调用按所选 LLM 计费。 | [官网](https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents) / [GitHub](https://github.com/langchain-ai/open-swe) / [文档](https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents) | 2026-08-22 | GitHub |
| 5 | OpenAgents（openagents-org/openagents） | 面向开放协作的 AI Agent 网络（「AI Agent Networks for Open Collaboration」），提供统一工作空间管理、多 Agent 协调与网络集成，无供应商锁定。与 WorkBench 相似度：中——多 Agent 协作操作系统/网络，开放协作。适用：想以去中心化方式组织多个 Agent 协同的团队。 | Apache-2.0，开源免费自托管；需自备模型 API Key。 | [官网](https://openagents.org) / [GitHub](https://github.com/openagents-org/openagents) / [文档](https://openagents.org) | 2026-08-21 | GitHub |
| 6 | Atmosphere（Atmosphere/atmosphere） | JVM 上的可移植 AI Agent 运行时：一个 @Agent 类即可在 Spring AI、LangChain4j、Anthropic 等 9+ 后端之上运行（统一 SPI）；支持 Token 流式、工具调用、人工审批与治理，通过 WebSocket/SSE/gRPC/WebTransport 传输，原生支持 MCP、A2A、AG-UI。与 WorkBench 相似度：中——企业级 Agent 运行时（老牌 JVM 项目新增的 AI agent 能力，今日仍高频提交）。适用：Java/Spring 生态需将 Agent 嵌入现有后端服务的团队。 | Apache-2.0，开源免费；JVM 运行时，需自备模型 API Key（Spring AI/LangChain4j/Anthropic 等）。 | [官网](https://async-io.live) / [GitHub](https://github.com/Atmosphere/atmosphere) / [文档](https://async-io.live) | 2026-08-22 | GitHub |
| 7 | PraisonAI（MervinPraison/PraisonAI） | 无代码/低代码「AI 数字员工」全家桶：用一个 YAML 文件（角色/目标/指令三段式）或可视化 Claw 面板（13 个内置页面：聊天、Agent 管理、记忆、知识库、渠道、护栏、定时任务等）即可组建多 Agent 工作流；支持 Telegram/Discord/Slack/WhatsApp 等渠道接入，集成 Langflow 拖拽画布。与 WorkBench 相似度：高——最贴近 WorkBench 定位的开源多 Agent 构建平台（填表/拖拽即建 Agent）。适用：不想写代码也想批量创建 AI 员工的职场人与小团队。 | MIT，开源免费自托管（pip install praisonai / praisonai claw）；需自备 LLM API Key（OpenAI/DeepSeek 等），按 Token 计费。 | [官网](https://praison.ai/docs) / [GitHub](https://github.com/MervinPraison/PraisonAI) / [文档](https://praison.ai/docs) | 2026-08-21 | AI 工具导航站 |
| 8 | Skybridge（alpic-ai/skybridge） | 用于构建 MCP Apps 与 ChatGPT Apps 的全栈 TypeScript 框架：类型安全、React 驱动、平台无关，让开发者用统一 TS 接口编写可嵌入 ChatGPT/Claude 等客户端的 Agent 应用与 MCP 服务器。与 WorkBench 相似度：中——Agent 应用/扩展构建框架，偏应用开发侧。适用：想为 MCP/ChatGPT 生态快速产出类型安全 Agent 应用的开发者。 | MIT，开源免费；需自备模型 API Key。 | [官网](https://skybridge.tech) / [GitHub](https://github.com/alpic-ai/skybridge) / [文档](https://skybridge.tech) | 2026-08-21 | GitHub |
| 9 | NeuroLink（Juspay / juspay/neurolink） | 统一 24+ LLM 提供商的单一 TypeScript 接口（provider 热切换无需改码），MCP-native（可连任意 MCP 服务器），内置语音（TTS/STT/realtime）、RAG、记忆与文件处理；源自 Juspay 生产环境（驱动其 Tara/Yama/Clairvoyance 等 Agent）。与 WorkBench 相似度：中——Agent 开发 SDK/集成底座（统一 LLM 接口 + MCP + RAG + 记忆），偏基础设施。适用：需要在多模型间灵活切换并快速搭建 Agent 的 TS 开发者。 | MIT，开源免费；需自备所接提供商的 API Key。 | [官网](https://neurolink.ink) / [GitHub](https://github.com/juspay/neurolink) / [文档](https://neurolink.ink) | 2026-08-21 | GitHub |
| 10 | PwrAgent（pwrdrvr/PwrAgent） | 桌面编码 Agent，可运行在笔记本本地，并通过 Telegram、Discord、Slack、Mattermost、飞书/Lark、LINE 等消息平台远程驱动；Codex 兼容，让 Agent「住在手机里、跑在电脑上」。与 WorkBench 相似度：中——远程消息驱动的编码 Agent，偏编码助手。适用：希望在聊天软件里随时派活、本机执行的开发者。 | MIT，开源免费自托管；Codex 兼容，需自备模型（如 OpenAI Codex/本地模型），模型调用按所选方案计费。 | [官网](https://pwragent.ai) / [GitHub](https://github.com/pwrdrvr/PwrAgent) / [文档](https://pwragent.ai) | 2026-08-22 | GitHub |
| 11 | llmix（sno-ai/llmix） | 面向 AI Agent 与工具的生产级 LLM 调用层：在保留 OpenAI/Anthropic/AI SDK/LiteLLM 接口的同时，以 MDA 预设热切换模型，并叠加缓存、重试、熔断（circuit breaker）、密钥轮换、singleflight 等韧性机制，提供 Python/TypeScript/Rust 三语言一致实现。与 WorkBench 相似度：低——更偏 Agent 的 LLM 调用基础设施库，而非完整构建平台，但为 Agent 提供生产级底座。适用：需要稳健多模型调用的 Agent/工具开发者。 | Apache-2.0，开源免费；需自备所接模型的 API Key。 | [官网](https://github.com/sno-ai/llmix) / [GitHub](https://github.com/sno-ai/llmix) | 2026-08-16 | GitHub |

## 详细信息

### 1. Codex Harness（OpenAI / openai/codex）

- **功能描述**：OpenAI 于 2026-08-19 全面开源的 Agent 底层执行框架（harness 层），提供 codex exec（非交互调用）、Codex SDK（程序化编排）、Codex app-server（持久会话）三层接口，将 Agent 循环（对话状态/工具调用/沙箱/流式/人工审批）作为可嵌入产品的底层执行引擎。与 WorkBench 相似度：高——同为 Agent 执行与编排基础设施，前后端解耦、可嵌入业务系统，模型无关。适用：已成熟业务界面需原生嵌入 Agent 执行并掌控审批流程的团队。
- **免费使用方式**：Apache-2.0，可完全免费自部署/二次分发（含商用）。作为库/CLI/SDK 嵌入自有产品免费；默认对接 OpenAI API，模型调用需自备 OpenAI API Key 并按其计费，替换其他模型需自适配调用层。
- **官网**：https://developers.openai.com/blog/codex-as-a-platform
- **GitHub**：https://github.com/openai/codex
- **文档**：https://developers.openai.com/blog/codex-as-a-platform
- **最后更新日期**：2026-08-22
- **发现渠道**：GitHub

### 2. TeamAI（腾讯 / Tencent/teamai-cli）

- **功能描述**：腾讯 2026-08-21 开源的「团队 harness for AI agents」，核心思路是把 Git 仓库变成 AI Agent 的共享大脑：统一管理 Claude Code / Cursor 等编程 Agent 的技能与规则，支持「经验自动沉淀」（摩擦点触发后将解决问题的经验推送到团队共享库）、MCP 服务配置统一分发、基于 codebase 的知识图谱检索。与 WorkBench 相似度：中——偏 Agent 协作治理/对齐层，而非完整构建平台；Git-native 方案避开中心化平台。适用：多 Agent 规模化落地的团队对齐。
- **免费使用方式**：开源（许可证为 NOASSERTION/Other，非标准协议，商用前需确认条款）；可自托管。将 Git 仓库作为 Agent 共享记忆与规则层，无需中心化平台。
- **官网**：-
- **GitHub**：https://github.com/Tencent/teamai-cli
- **文档**：-
- **最后更新日期**：2026-08-20
- **发现渠道**：开发者社区

### 3. QwenPaw（AgentScope / agentscope-ai/QwenPaw）

- **功能描述**：AgentScope 团队推出的本地优先、可自托管的个人 AI 助手（原 CoPaw），可同时接入即时通讯、邮件、日程等多个渠道，在本地维护统一上下文与三层记忆，支持自定义技能扩展；安装简单（本机或云端皆可部署）。与 WorkBench 相似度：高——多渠道个人智能体平台，技能/记忆/自托管，与 OpenClaw 类产品定位一致。适用：想要个人助理但不愿把生活数据交托云端者。
- **免费使用方式**：Apache-2.0，完全免费自托管（本机或云端），无信用卡要求；需自备 LLM API Key（OpenAI/通义等），按所选模型计费。
- **官网**：http://qwenpaw.agentscope.io/
- **GitHub**：https://github.com/agentscope-ai/QwenPaw
- **文档**：http://qwenpaw.agentscope.io/
- **最后更新日期**：2026-08-21
- **发现渠道**：GitHub

### 4. Open-SWE（LangChain / langchain-ai/open-swe）

- **功能描述**：LangChain 开源的异步编码 Agent 框架（开源版「内部 Devin」），基于 LangGraph 与 Deep Agents 构建，提供云沙箱、Slack/Linear/GitHub 调用、子 Agent 编排与自动 PR 创建，面向工程组织。与 WorkBench 相似度：中——内部编码 Agent 框架，偏研发自动化而非通用构建平台。适用：需要内部编码 Agent 的软件团队。
- **免费使用方式**：MIT，开源免费自托管；提供云沙箱（可能按用量计费）与本地执行两种路径，模型调用按所选 LLM 计费。
- **官网**：https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents
- **GitHub**：https://github.com/langchain-ai/open-swe
- **文档**：https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents
- **最后更新日期**：2026-08-22
- **发现渠道**：GitHub

### 5. OpenAgents（openagents-org/openagents）

- **功能描述**：面向开放协作的 AI Agent 网络（「AI Agent Networks for Open Collaboration」），提供统一工作空间管理、多 Agent 协调与网络集成，无供应商锁定。与 WorkBench 相似度：中——多 Agent 协作操作系统/网络，开放协作。适用：想以去中心化方式组织多个 Agent 协同的团队。
- **免费使用方式**：Apache-2.0，开源免费自托管；需自备模型 API Key。
- **官网**：https://openagents.org
- **GitHub**：https://github.com/openagents-org/openagents
- **文档**：https://openagents.org
- **最后更新日期**：2026-08-21
- **发现渠道**：GitHub

### 6. Atmosphere（Atmosphere/atmosphere）

- **功能描述**：JVM 上的可移植 AI Agent 运行时：一个 @Agent 类即可在 Spring AI、LangChain4j、Anthropic 等 9+ 后端之上运行（统一 SPI）；支持 Token 流式、工具调用、人工审批与治理，通过 WebSocket/SSE/gRPC/WebTransport 传输，原生支持 MCP、A2A、AG-UI。与 WorkBench 相似度：中——企业级 Agent 运行时（老牌 JVM 项目新增的 AI agent 能力，今日仍高频提交）。适用：Java/Spring 生态需将 Agent 嵌入现有后端服务的团队。
- **免费使用方式**：Apache-2.0，开源免费；JVM 运行时，需自备模型 API Key（Spring AI/LangChain4j/Anthropic 等）。
- **官网**：https://async-io.live
- **GitHub**：https://github.com/Atmosphere/atmosphere
- **文档**：https://async-io.live
- **最后更新日期**：2026-08-22
- **发现渠道**：GitHub

### 7. PraisonAI（MervinPraison/PraisonAI）

- **功能描述**：无代码/低代码「AI 数字员工」全家桶：用一个 YAML 文件（角色/目标/指令三段式）或可视化 Claw 面板（13 个内置页面：聊天、Agent 管理、记忆、知识库、渠道、护栏、定时任务等）即可组建多 Agent 工作流；支持 Telegram/Discord/Slack/WhatsApp 等渠道接入，集成 Langflow 拖拽画布。与 WorkBench 相似度：高——最贴近 WorkBench 定位的开源多 Agent 构建平台（填表/拖拽即建 Agent）。适用：不想写代码也想批量创建 AI 员工的职场人与小团队。
- **免费使用方式**：MIT，开源免费自托管（pip install praisonai / praisonai claw）；需自备 LLM API Key（OpenAI/DeepSeek 等），按 Token 计费。
- **官网**：https://praison.ai/docs
- **GitHub**：https://github.com/MervinPraison/PraisonAI
- **文档**：https://praison.ai/docs
- **最后更新日期**：2026-08-21
- **发现渠道**：AI 工具导航站

### 8. Skybridge（alpic-ai/skybridge）

- **功能描述**：用于构建 MCP Apps 与 ChatGPT Apps 的全栈 TypeScript 框架：类型安全、React 驱动、平台无关，让开发者用统一 TS 接口编写可嵌入 ChatGPT/Claude 等客户端的 Agent 应用与 MCP 服务器。与 WorkBench 相似度：中——Agent 应用/扩展构建框架，偏应用开发侧。适用：想为 MCP/ChatGPT 生态快速产出类型安全 Agent 应用的开发者。
- **免费使用方式**：MIT，开源免费；需自备模型 API Key。
- **官网**：https://skybridge.tech
- **GitHub**：https://github.com/alpic-ai/skybridge
- **文档**：https://skybridge.tech
- **最后更新日期**：2026-08-21
- **发现渠道**：GitHub

### 9. NeuroLink（Juspay / juspay/neurolink）

- **功能描述**：统一 24+ LLM 提供商的单一 TypeScript 接口（provider 热切换无需改码），MCP-native（可连任意 MCP 服务器），内置语音（TTS/STT/realtime）、RAG、记忆与文件处理；源自 Juspay 生产环境（驱动其 Tara/Yama/Clairvoyance 等 Agent）。与 WorkBench 相似度：中——Agent 开发 SDK/集成底座（统一 LLM 接口 + MCP + RAG + 记忆），偏基础设施。适用：需要在多模型间灵活切换并快速搭建 Agent 的 TS 开发者。
- **免费使用方式**：MIT，开源免费；需自备所接提供商的 API Key。
- **官网**：https://neurolink.ink
- **GitHub**：https://github.com/juspay/neurolink
- **文档**：https://neurolink.ink
- **最后更新日期**：2026-08-21
- **发现渠道**：GitHub

### 10. PwrAgent（pwrdrvr/PwrAgent）

- **功能描述**：桌面编码 Agent，可运行在笔记本本地，并通过 Telegram、Discord、Slack、Mattermost、飞书/Lark、LINE 等消息平台远程驱动；Codex 兼容，让 Agent「住在手机里、跑在电脑上」。与 WorkBench 相似度：中——远程消息驱动的编码 Agent，偏编码助手。适用：希望在聊天软件里随时派活、本机执行的开发者。
- **免费使用方式**：MIT，开源免费自托管；Codex 兼容，需自备模型（如 OpenAI Codex/本地模型），模型调用按所选方案计费。
- **官网**：https://pwragent.ai
- **GitHub**：https://github.com/pwrdrvr/PwrAgent
- **文档**：https://pwragent.ai
- **最后更新日期**：2026-08-22
- **发现渠道**：GitHub

### 11. llmix（sno-ai/llmix）

- **功能描述**：面向 AI Agent 与工具的生产级 LLM 调用层：在保留 OpenAI/Anthropic/AI SDK/LiteLLM 接口的同时，以 MDA 预设热切换模型，并叠加缓存、重试、熔断（circuit breaker）、密钥轮换、singleflight 等韧性机制，提供 Python/TypeScript/Rust 三语言一致实现。与 WorkBench 相似度：低——更偏 Agent 的 LLM 调用基础设施库，而非完整构建平台，但为 Agent 提供生产级底座。适用：需要稳健多模型调用的 Agent/工具开发者。
- **免费使用方式**：Apache-2.0，开源免费；需自备所接模型的 API Key。
- **官网**：https://github.com/sno-ai/llmix
- **GitHub**：https://github.com/sno-ai/llmix
- **文档**：-
- **最后更新日期**：2026-08-16
- **发现渠道**：GitHub
