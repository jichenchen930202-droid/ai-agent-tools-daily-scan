# 每日 AI Agent 工具扫描报告 - 2026-08-12

> 搜索截止日期：2026-08-12 ｜ 生成时间：2026-08-12 10:05:48 ｜ 发现工具数：6

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | TheYgent | 本地优先的无代码 AI 智能体构建与运行工作室，可视化拖拽编排智能体工作流；推理可完全在本地（llama.cpp / MLX / vLLM）运行，或对接任意 OpenAI 兼容 API。与 WorkBench 相似度：高 —— 具备可视化的多工具/多模型 Agent 编排、自托管、数据不出本机，是 WorkBench 类「本地优先 Agent 构建平台」的轻量替代。适用场景：个人/团队在隐私敏感环境下快速搭建生产级 AI Agent，无需编写代码。 | 采用 Fair-code（Sustainable Use License）许可，可免费用于自用、修改、自托管及内部业务/个人目的；禁止将 TheYgent 本身作为托管服务商业化。无信用卡要求，本地部署免费，仅需自备模型（本地或 API）费用。 | [官网](https://github.com/al2m4n/TheYgent) / [GitHub](https://github.com/al2m4n/TheYgent) / [文档](https://github.com/al2m4n/TheYgent) | 2026-08-04 | GitHub |
| 2 | LiveContext CE | 自托管的 AI 自动化平台：用自然语言对话即可生成可读工作流、限定范围的 scoped AI Agent 和团队小应用，Chat / Workflow / Agent / App 统一于单一画布，定位为 n8n / Zapier / Make 的开源自托管替代。与 WorkBench 相似度：高 —— 对话驱动的工作流 + Agent 编排 + 自托管，能力形态与 WorkBench 高度重合。适用场景：业务/运营团队无需编码即可将重复流程自动化，数据保留在自有基础设施。 | AGPL-3.0 开源；Community Edition 可免费自托管并用于组织内部生产环境，允许自由使用、自托管、修改与再分发（含商业用途，但作为网络服务修改后需依 AGPL 提供源码）。无信用卡要求，仅模型 API 费用自理。 | [官网](https://github.com/livecontext-ai/livecontext-ce) / [GitHub](https://github.com/livecontext-ai/livecontext-ce) / [文档](https://github.com/livecontext-ai/livecontext-ce) | 2026-08-04 | GitHub |
| 3 | ForestHub Edge Agents | 约 30MB 的开源边缘 AI 智能体运行时，可在 Linux 边缘设备（网关 / NUC / Jetson / 树莓派）上完全离线运行 AI 代理；以「图即程序」方式编排 LLM 节点、规则逻辑与本地小模型。与 WorkBench 相似度：中 —— 更偏边缘/离线 Agent 运行时与编排，而非通用低代码构建平台，但同属可自托管的 Agent 编排工具。适用场景：在资源受限或离线的边缘设备上运行确定性、可控的 AI 工作流。 | 双许可：contract/ 与 workflow-core 为 Apache-2.0；go 引擎、workflow-builder、workflow-cli、py/onnx 为 AGPL-3.0-only 或商业许可。AGPL 组件可按 AGPL 条款免费自托管使用，商业不兼容场景需购买商业许可。免费起步、无需信用卡；离线运行无 API 费用。 | [官网](https://www.foresthub.ai/en/platform) / [GitHub](https://github.com/ForestHubAI/edge-agents) / [文档](https://www.foresthub.ai/en/platform) | 2026-07-29 | GitHub |
| 4 | Cindy | 心动公司（TapTap）开源、开箱即用的 AI Agent 客户端，统一接入大语言/图像/视频/音频等多模型与工具，首批兼容 Claude Code 与 Codex 两套 Harness，支持本地模式、多引擎混合编排、以及通过 MCP / AI Gateway / VPC 接入内部系统。与 WorkBench 相似度：中高 —— 以「桌面/移动端 Agent 工作环境」形态出现的开源 Agent 客户端，强调开箱即用与本地运行，偏终端用户而非低代码平台。适用场景：个人/团队用自然语言驱动 Agent 在本地完成文件操作、应用管理与自动化（内置 TapTap 制造，可用于 AI 游戏创作）。 | Apache-2.0 开源。软件本身免费：接入自己的 API Key、本地模型或已有 Claude Code / Codex 订阅时无需额外付费（FREE 档）；官方模型服务按量充值（最低 50 元）或订阅 PLUS（单月 100 元，连续订阅 80 元/月）；企业版含额度管理与团队 Skill 治理。无信用卡要求（自备模型）。 | [官网](https://cindy.cn) / [GitHub](https://github.com/makecindy/cindy) / [文档](https://cindy.cn/download) | 2026-08-12 | 导航站/社区 |
| 5 | Odysseus | 开源的自托管一体化 AI 工作台（类本地版 ChatGPT），在自有设备 / NAS / 服务器通过 Docker 运行；内置 Agent 模块（赋予工具后自主执行任务，支持 MCP、网页、文件、Shell、技能与记忆）、深度研究、Cookbook 模型库、IMAP 邮箱与日历等。与 WorkBench 相似度：中 —— 偏「自托管 AI 工作空间 + Agent」，含 Agent 编排与记忆系统，与 WorkBench 的本地优先/自托管定位相符。适用场景：希望完全掌控数据、摆脱订阅制的个人/团队，在本地运行带 Agent 的生产力工作台。 | AGPL-3.0-or-later 开源，可免费自托管使用，数据默认本地处理、不上报；仅需自备模型（Ollama / OpenAI API 等）费用。无信用卡要求。 | [官网](https://github.com/odysseus-dev/odysseus) / [GitHub](https://github.com/odysseus-dev/odysseus) / [文档](https://github.com/odysseus-dev/odysseus) | 2026-08-12 | 导航站 |
| 6 | LiteLLM Agent Platform | BerriAI（LiteLLM Gateway 团队）开源的自托管 Agent 基础设施层，用于在 Kubernetes 上运行生产级智能体：提供 Next.js 仪表盘、基于 kubernetes-sigs/agent-sandbox CRD 的每会话隔离沙箱、Postgres 持久化会话，并对接 100+ LLM 提供商。与 WorkBench 相似度：中 —— 是面向平台的「Agent 运行/编排基础设施」而非终端用户低代码构建器，但同属可自托管、多提供商的 Agent 运行底座。适用场景：需要数据驻留/合规、在自有 K8s 集群隔离运行多个生产智能体的平台/工程团队（当前为 alpha 阶段，建议先试点评估）。 | MIT 许可，开源免费、可完全自托管（数据不出环境）；当前为 alpha public preview（2026-05-08 发布），处于快速迭代中。需自备 K8s 集群与 LLM 网关，仅产生云资源与模型 API 成本，无软件授权费、无需信用卡。 | [官网](https://docs.litellm.ai/blog/agent-platform-alpha) / [GitHub](https://github.com/BerriAI/litellm-agent-platform) / [文档](https://docs.litellm.ai/blog/agent-platform-alpha) | 2026-05-08 | GitHub/社区 |

## 详细信息

### 1. TheYgent

- **功能描述**：本地优先的无代码 AI 智能体构建与运行工作室，可视化拖拽编排智能体工作流；推理可完全在本地（llama.cpp / MLX / vLLM）运行，或对接任意 OpenAI 兼容 API。与 WorkBench 相似度：高 —— 具备可视化的多工具/多模型 Agent 编排、自托管、数据不出本机，是 WorkBench 类「本地优先 Agent 构建平台」的轻量替代。适用场景：个人/团队在隐私敏感环境下快速搭建生产级 AI Agent，无需编写代码。
- **免费使用方式**：采用 Fair-code（Sustainable Use License）许可，可免费用于自用、修改、自托管及内部业务/个人目的；禁止将 TheYgent 本身作为托管服务商业化。无信用卡要求，本地部署免费，仅需自备模型（本地或 API）费用。
- **官网**：https://github.com/al2m4n/TheYgent
- **GitHub**：https://github.com/al2m4n/TheYgent
- **文档**：https://github.com/al2m4n/TheYgent
- **最后更新日期**：2026-08-04
- **发现渠道**：GitHub

### 2. LiveContext CE

- **功能描述**：自托管的 AI 自动化平台：用自然语言对话即可生成可读工作流、限定范围的 scoped AI Agent 和团队小应用，Chat / Workflow / Agent / App 统一于单一画布，定位为 n8n / Zapier / Make 的开源自托管替代。与 WorkBench 相似度：高 —— 对话驱动的工作流 + Agent 编排 + 自托管，能力形态与 WorkBench 高度重合。适用场景：业务/运营团队无需编码即可将重复流程自动化，数据保留在自有基础设施。
- **免费使用方式**：AGPL-3.0 开源；Community Edition 可免费自托管并用于组织内部生产环境，允许自由使用、自托管、修改与再分发（含商业用途，但作为网络服务修改后需依 AGPL 提供源码）。无信用卡要求，仅模型 API 费用自理。
- **官网**：https://github.com/livecontext-ai/livecontext-ce
- **GitHub**：https://github.com/livecontext-ai/livecontext-ce
- **文档**：https://github.com/livecontext-ai/livecontext-ce
- **最后更新日期**：2026-08-04
- **发现渠道**：GitHub

### 3. ForestHub Edge Agents

- **功能描述**：约 30MB 的开源边缘 AI 智能体运行时，可在 Linux 边缘设备（网关 / NUC / Jetson / 树莓派）上完全离线运行 AI 代理；以「图即程序」方式编排 LLM 节点、规则逻辑与本地小模型。与 WorkBench 相似度：中 —— 更偏边缘/离线 Agent 运行时与编排，而非通用低代码构建平台，但同属可自托管的 Agent 编排工具。适用场景：在资源受限或离线的边缘设备上运行确定性、可控的 AI 工作流。
- **免费使用方式**：双许可：contract/ 与 workflow-core 为 Apache-2.0；go 引擎、workflow-builder、workflow-cli、py/onnx 为 AGPL-3.0-only 或商业许可。AGPL 组件可按 AGPL 条款免费自托管使用，商业不兼容场景需购买商业许可。免费起步、无需信用卡；离线运行无 API 费用。
- **官网**：https://www.foresthub.ai/en/platform
- **GitHub**：https://github.com/ForestHubAI/edge-agents
- **文档**：https://www.foresthub.ai/en/platform
- **最后更新日期**：2026-07-29
- **发现渠道**：GitHub

### 4. Cindy

- **功能描述**：心动公司（TapTap）开源、开箱即用的 AI Agent 客户端，统一接入大语言/图像/视频/音频等多模型与工具，首批兼容 Claude Code 与 Codex 两套 Harness，支持本地模式、多引擎混合编排、以及通过 MCP / AI Gateway / VPC 接入内部系统。与 WorkBench 相似度：中高 —— 以「桌面/移动端 Agent 工作环境」形态出现的开源 Agent 客户端，强调开箱即用与本地运行，偏终端用户而非低代码平台。适用场景：个人/团队用自然语言驱动 Agent 在本地完成文件操作、应用管理与自动化（内置 TapTap 制造，可用于 AI 游戏创作）。
- **免费使用方式**：Apache-2.0 开源。软件本身免费：接入自己的 API Key、本地模型或已有 Claude Code / Codex 订阅时无需额外付费（FREE 档）；官方模型服务按量充值（最低 50 元）或订阅 PLUS（单月 100 元，连续订阅 80 元/月）；企业版含额度管理与团队 Skill 治理。无信用卡要求（自备模型）。
- **官网**：https://cindy.cn
- **GitHub**：https://github.com/makecindy/cindy
- **文档**：https://cindy.cn/download
- **最后更新日期**：2026-08-12
- **发现渠道**：导航站/社区

### 5. Odysseus

- **功能描述**：开源的自托管一体化 AI 工作台（类本地版 ChatGPT），在自有设备 / NAS / 服务器通过 Docker 运行；内置 Agent 模块（赋予工具后自主执行任务，支持 MCP、网页、文件、Shell、技能与记忆）、深度研究、Cookbook 模型库、IMAP 邮箱与日历等。与 WorkBench 相似度：中 —— 偏「自托管 AI 工作空间 + Agent」，含 Agent 编排与记忆系统，与 WorkBench 的本地优先/自托管定位相符。适用场景：希望完全掌控数据、摆脱订阅制的个人/团队，在本地运行带 Agent 的生产力工作台。
- **免费使用方式**：AGPL-3.0-or-later 开源，可免费自托管使用，数据默认本地处理、不上报；仅需自备模型（Ollama / OpenAI API 等）费用。无信用卡要求。
- **官网**：https://github.com/odysseus-dev/odysseus
- **GitHub**：https://github.com/odysseus-dev/odysseus
- **文档**：https://github.com/odysseus-dev/odysseus
- **最后更新日期**：2026-08-12
- **发现渠道**：导航站

### 6. LiteLLM Agent Platform

- **功能描述**：BerriAI（LiteLLM Gateway 团队）开源的自托管 Agent 基础设施层，用于在 Kubernetes 上运行生产级智能体：提供 Next.js 仪表盘、基于 kubernetes-sigs/agent-sandbox CRD 的每会话隔离沙箱、Postgres 持久化会话，并对接 100+ LLM 提供商。与 WorkBench 相似度：中 —— 是面向平台的「Agent 运行/编排基础设施」而非终端用户低代码构建器，但同属可自托管、多提供商的 Agent 运行底座。适用场景：需要数据驻留/合规、在自有 K8s 集群隔离运行多个生产智能体的平台/工程团队（当前为 alpha 阶段，建议先试点评估）。
- **免费使用方式**：MIT 许可，开源免费、可完全自托管（数据不出环境）；当前为 alpha public preview（2026-05-08 发布），处于快速迭代中。需自备 K8s 集群与 LLM 网关，仅产生云资源与模型 API 成本，无软件授权费、无需信用卡。
- **官网**：https://docs.litellm.ai/blog/agent-platform-alpha
- **GitHub**：https://github.com/BerriAI/litellm-agent-platform
- **文档**：https://docs.litellm.ai/blog/agent-platform-alpha
- **最后更新日期**：2026-05-08
- **发现渠道**：GitHub/社区
