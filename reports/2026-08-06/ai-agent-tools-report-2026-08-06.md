# 每日 AI Agent 工具扫描报告 - 2026-08-06

> 搜索截止日期：2026-08-06 ｜ 生成时间：2026-08-06 10:05:07 ｜ 发现工具数：6

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | DeerFlow (ByteDance) | 开源长周期 SuperAgent 编排框架，集沙箱、记忆、工具、技能、子智能体与消息网关于一体，能自主完成研究、编码、创作等耗时数分钟至数小时的任务。与 WorkBench 相似度高：提供多智能体编排与可视化工作流能力（基于 LangChain/LangGraph），可本地自部署。 | 开源（MIT 许可证），可免费自部署；需自备 LLM API Key 与运行环境（Docker）。无云端付费墙。 | [官网](https://deerflow.tech) / [GitHub](https://github.com/bytedance/deer-flow) | 2026-08-05 | GitHub |
| 2 | Ruflo | 开源 agent meta-harness（智能体元框架），用于部署多智能体 swarm（蜂群）、协调自主工作流、构建对话式 AI 系统；内置自适应记忆、自学习、RAG 集成，原生集成 Claude Code / Codex / Hermes 等。与 WorkBench 相似度高：多智能体编排与自动化工作流框架，可自部署。 | 开源（MIT），可免费自部署；需自备 API Key 与运行环境。 | [官网](https://Cognitum.One) / [GitHub](https://github.com/ruvnet/ruflo) | 2026-08-05 | GitHub |
| 3 | Page Agent (Alibaba) | 开源 JavaScript 网页内 GUI 智能体框架，用自然语言控制网页界面（点击、填写、操作 DOM）。与 WorkBench 相似度中：偏「GUI/浏览器自动化智能体」框架而非可视化构建器，但提供了用自然语言驱动网页操作的 agent 能力，可自部署，适合构建网页操作类 agent。 | 开源（MIT），可免费自部署；以 npm 包形式集成，需自备模型 API。 | [官网](https://alibaba.github.io/page-agent/) / [GitHub](https://github.com/alibaba/page-agent) / [文档](https://alibaba.github.io/page-agent/) | 2026-08-05 | GitHub |
| 4 | OpenClaw | 开源「个人 AI 助手」平台，可在任意操作系统/平台自托管，连接 Telegram、WhatsApp、Slack、Discord 等，强调 own-your-data。与 WorkBench 相似度中：属可自部署的 AI 智能体运行平台（端侧个人助手），而非低代码构建器；适合想把智能体跑在自己基础设施上的用户。 | 开源可自部署（仓库许可证为 NOASSERTION，非标准 SPDX 协议，使用前需查看仓库 LICENSE 确认条款）；无强制付费。 | [官网](https://openclaw.ai) / [GitHub](https://github.com/openclaw/openclaw) | 2026-08-06 | GitHub |
| 5 | Arahi Agent Builder | 无代码 AI 智能体构建平台：一句话描述即可生成可运行的智能体，呈现为可编辑的可视化图，支持替换工具、调整语气、添加审批节点；内置 1500+ 原生集成与 Agent 市场模板。与 WorkBench 相似度高：自然语言驱动的 agent 构建 + 可视化编排 + 多工具集成 + 定时/触发器工作流，定位同类。 | 有免费层（free plan，无需信用卡，可在免费额度内构建并运行工作流）；付费版按席位+用量扩展。免费额度具体上限未在官网明确，以官网 pricing 为准。免费层截至 2026-08-06 仍可注册使用。 | [官网](https://arahi.ai) / [文档](https://arahi.ai/autonomous-virtual-agents) | unknown | 导航站 |
| 6 | Lamoom | 面向 Claude 的「本地优先」智能体应用市场与 loop 构建器：用户可在自己的 Claude 环境中安装/运行 agent apps（loops，带自评 judge 循环），也可发布自己的 loop 并按时/按月收费。与 WorkBench 相似度中：提供 agent 工作流（loop）的封装、分发与运行，强调数据不出本地（运行在用户自己的 Claude）。 | 注册赠送 $20 免费额度可用于试用付费 agent apps（非永久免费层）；后续按 per-run 或月度订阅付费。创作者发布 loop 自行定价。 | [官网](https://lamoom.com) | unknown | ProductHunt |

## 详细信息

### 1. DeerFlow (ByteDance)

- **功能描述**：开源长周期 SuperAgent 编排框架，集沙箱、记忆、工具、技能、子智能体与消息网关于一体，能自主完成研究、编码、创作等耗时数分钟至数小时的任务。与 WorkBench 相似度高：提供多智能体编排与可视化工作流能力（基于 LangChain/LangGraph），可本地自部署。
- **免费使用方式**：开源（MIT 许可证），可免费自部署；需自备 LLM API Key 与运行环境（Docker）。无云端付费墙。
- **官网**：https://deerflow.tech
- **GitHub**：https://github.com/bytedance/deer-flow
- **文档**：-
- **最后更新日期**：2026-08-05
- **发现渠道**：GitHub

### 2. Ruflo

- **功能描述**：开源 agent meta-harness（智能体元框架），用于部署多智能体 swarm（蜂群）、协调自主工作流、构建对话式 AI 系统；内置自适应记忆、自学习、RAG 集成，原生集成 Claude Code / Codex / Hermes 等。与 WorkBench 相似度高：多智能体编排与自动化工作流框架，可自部署。
- **免费使用方式**：开源（MIT），可免费自部署；需自备 API Key 与运行环境。
- **官网**：https://Cognitum.One
- **GitHub**：https://github.com/ruvnet/ruflo
- **文档**：-
- **最后更新日期**：2026-08-05
- **发现渠道**：GitHub

### 3. Page Agent (Alibaba)

- **功能描述**：开源 JavaScript 网页内 GUI 智能体框架，用自然语言控制网页界面（点击、填写、操作 DOM）。与 WorkBench 相似度中：偏「GUI/浏览器自动化智能体」框架而非可视化构建器，但提供了用自然语言驱动网页操作的 agent 能力，可自部署，适合构建网页操作类 agent。
- **免费使用方式**：开源（MIT），可免费自部署；以 npm 包形式集成，需自备模型 API。
- **官网**：https://alibaba.github.io/page-agent/
- **GitHub**：https://github.com/alibaba/page-agent
- **文档**：https://alibaba.github.io/page-agent/
- **最后更新日期**：2026-08-05
- **发现渠道**：GitHub

### 4. OpenClaw

- **功能描述**：开源「个人 AI 助手」平台，可在任意操作系统/平台自托管，连接 Telegram、WhatsApp、Slack、Discord 等，强调 own-your-data。与 WorkBench 相似度中：属可自部署的 AI 智能体运行平台（端侧个人助手），而非低代码构建器；适合想把智能体跑在自己基础设施上的用户。
- **免费使用方式**：开源可自部署（仓库许可证为 NOASSERTION，非标准 SPDX 协议，使用前需查看仓库 LICENSE 确认条款）；无强制付费。
- **官网**：https://openclaw.ai
- **GitHub**：https://github.com/openclaw/openclaw
- **文档**：-
- **最后更新日期**：2026-08-06
- **发现渠道**：GitHub

### 5. Arahi Agent Builder

- **功能描述**：无代码 AI 智能体构建平台：一句话描述即可生成可运行的智能体，呈现为可编辑的可视化图，支持替换工具、调整语气、添加审批节点；内置 1500+ 原生集成与 Agent 市场模板。与 WorkBench 相似度高：自然语言驱动的 agent 构建 + 可视化编排 + 多工具集成 + 定时/触发器工作流，定位同类。
- **免费使用方式**：有免费层（free plan，无需信用卡，可在免费额度内构建并运行工作流）；付费版按席位+用量扩展。免费额度具体上限未在官网明确，以官网 pricing 为准。免费层截至 2026-08-06 仍可注册使用。
- **官网**：https://arahi.ai
- **GitHub**：-
- **文档**：https://arahi.ai/autonomous-virtual-agents
- **最后更新日期**：unknown
- **发现渠道**：导航站

### 6. Lamoom

- **功能描述**：面向 Claude 的「本地优先」智能体应用市场与 loop 构建器：用户可在自己的 Claude 环境中安装/运行 agent apps（loops，带自评 judge 循环），也可发布自己的 loop 并按时/按月收费。与 WorkBench 相似度中：提供 agent 工作流（loop）的封装、分发与运行，强调数据不出本地（运行在用户自己的 Claude）。
- **免费使用方式**：注册赠送 $20 免费额度可用于试用付费 agent apps（非永久免费层）；后续按 per-run 或月度订阅付费。创作者发布 loop 自行定价。
- **官网**：https://lamoom.com
- **GitHub**：-
- **文档**：-
- **最后更新日期**：unknown
- **发现渠道**：ProductHunt
