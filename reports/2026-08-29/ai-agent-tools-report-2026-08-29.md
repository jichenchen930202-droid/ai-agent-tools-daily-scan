# 每日 AI Agent 工具扫描报告 - 2026-08-29

> 搜索截止日期：2026-08-29 ｜ 生成时间：2026-08-29 12:18:54 ｜ 发现工具数：3

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | Headlong | Laude Institute（MIT 关联）开源的 agent microharness，核心不到 10k 行 Bash 实现「持久智能体（persistent agency）」——agent 在无人交互时也持续自主思考/行动，外部消息以 observation 形式注入统一的连续思想流。提供 shellm（递归 LLM 核心）、traj（轨迹 DAG）、context（分层压缩）、mem/skills 等可组合小工具，支持 Slack/Telegram/Web 多端协作、Docker 沙箱与子代理。相似度：高——同属可自托管、可编排多步任务/多智能体、带工具调用与记忆系统的 agent 运行时；区别在于 Headlong 以 Bash 为唯一工具、强调常驻自治而非按需响应。 | 完全开源（Apache-2.0），可自托管、免费使用；仅需自备 LLM API Key（Anthropic/OpenAI/Gemini/OpenRouter，BYOK），无固定费用。后台思考循环按 token 计费约 $1–2/小时，官方建议用限额 API Key 防失控。alpha 研究软件，建议沙箱内运行。 | [官网](https://headlong.ai) / [GitHub](https://github.com/laude-institute/headlong) / [文档](https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents) | 2026-08-29 | GitHub |
| 2 | openhuman | tinyhumansai 开源的个人 AI 超级智能（Personal AI super intelligence）：本地优先（local-first）的「记忆树（Memory Tree）」沉淀你的数字生活，作为 agent 集群与工作流的高效编排器（orchestrator of agent fleets and workflows），并具备深度研究能力。相似度：高——同属可自托管、带持久记忆与多智能体编排的 agent 平台/运行时，面向个人自动化与知识中枢；区别在于 openhuman 强调本地优先的个人记忆大脑，而非团队工作流编排。 | 完全开源（GPL-3.0），可自托管、免费使用；本地优先架构，数据留在本地，仅需自备大模型 API 或本地模型。beta 阶段已快速积累约 3.9 万星，无信用卡要求。 | [官网](https://tinyhumans.ai/openhuman) / [GitHub](https://github.com/tinyhumansai/openhuman) | 2026-08-27 | GitHub |
| 3 | OpenBot | CopilotKit 开源的「AI 同事（AI coworkers）」框架：每个 agent 拥有独立的电脑（浏览器 + 文件 + 工具），且每个动作在发生时先经治理闸门审批、执行后被记录（action approved before it happens, recorded after）。可接入任意 AG-UI agent，内置容器化与治理（agent governance）。相似度：高——同属可自托管、多智能体并行、带工具调用/浏览器自动化/治理审计的 agent 构建与编排平台，且 CopilotKit 生态成熟（MCP / AG-UI / Generative UI）。 | 完全开源（MIT），可自托管、免费使用；接入自有模型或 AG-UI agent（BYOK），无固定费用，无信用卡要求。CopilotKit 另有商业托管层，但 OpenBot 本体开源免费。 | [官网](https://www.copilotkit.ai/openbot) / [GitHub](https://github.com/CopilotKit/OpenBot) | 2026-08-28 | GitHub |

## 详细信息

### 1. Headlong

- **功能描述**：Laude Institute（MIT 关联）开源的 agent microharness，核心不到 10k 行 Bash 实现「持久智能体（persistent agency）」——agent 在无人交互时也持续自主思考/行动，外部消息以 observation 形式注入统一的连续思想流。提供 shellm（递归 LLM 核心）、traj（轨迹 DAG）、context（分层压缩）、mem/skills 等可组合小工具，支持 Slack/Telegram/Web 多端协作、Docker 沙箱与子代理。相似度：高——同属可自托管、可编排多步任务/多智能体、带工具调用与记忆系统的 agent 运行时；区别在于 Headlong 以 Bash 为唯一工具、强调常驻自治而非按需响应。
- **免费使用方式**：完全开源（Apache-2.0），可自托管、免费使用；仅需自备 LLM API Key（Anthropic/OpenAI/Gemini/OpenRouter，BYOK），无固定费用。后台思考循环按 token 计费约 $1–2/小时，官方建议用限额 API Key 防失控。alpha 研究软件，建议沙箱内运行。
- **官网**：https://headlong.ai
- **GitHub**：https://github.com/laude-institute/headlong
- **文档**：https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents
- **最后更新日期**：2026-08-29
- **发现渠道**：GitHub

### 2. openhuman

- **功能描述**：tinyhumansai 开源的个人 AI 超级智能（Personal AI super intelligence）：本地优先（local-first）的「记忆树（Memory Tree）」沉淀你的数字生活，作为 agent 集群与工作流的高效编排器（orchestrator of agent fleets and workflows），并具备深度研究能力。相似度：高——同属可自托管、带持久记忆与多智能体编排的 agent 平台/运行时，面向个人自动化与知识中枢；区别在于 openhuman 强调本地优先的个人记忆大脑，而非团队工作流编排。
- **免费使用方式**：完全开源（GPL-3.0），可自托管、免费使用；本地优先架构，数据留在本地，仅需自备大模型 API 或本地模型。beta 阶段已快速积累约 3.9 万星，无信用卡要求。
- **官网**：https://tinyhumans.ai/openhuman
- **GitHub**：https://github.com/tinyhumansai/openhuman
- **文档**：-
- **最后更新日期**：2026-08-27
- **发现渠道**：GitHub

### 3. OpenBot

- **功能描述**：CopilotKit 开源的「AI 同事（AI coworkers）」框架：每个 agent 拥有独立的电脑（浏览器 + 文件 + 工具），且每个动作在发生时先经治理闸门审批、执行后被记录（action approved before it happens, recorded after）。可接入任意 AG-UI agent，内置容器化与治理（agent governance）。相似度：高——同属可自托管、多智能体并行、带工具调用/浏览器自动化/治理审计的 agent 构建与编排平台，且 CopilotKit 生态成熟（MCP / AG-UI / Generative UI）。
- **免费使用方式**：完全开源（MIT），可自托管、免费使用；接入自有模型或 AG-UI agent（BYOK），无固定费用，无信用卡要求。CopilotKit 另有商业托管层，但 OpenBot 本体开源免费。
- **官网**：https://www.copilotkit.ai/openbot
- **GitHub**：https://github.com/CopilotKit/OpenBot
- **文档**：-
- **最后更新日期**：2026-08-28
- **发现渠道**：GitHub
