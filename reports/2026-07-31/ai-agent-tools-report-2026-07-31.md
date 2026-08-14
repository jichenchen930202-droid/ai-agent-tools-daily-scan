# 每日 AI Agent 工具扫描报告 - 2026-07-31

> 搜索截止日期：2026-07-31 ｜ 生成时间：2026-07-31 10:23:05 ｜ 发现工具数：5

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | OpenWorker | 吴恩达（Andrew Ng）团队开源的桌面 AI Agent（AI coworker），基于 aisuite 构建：自然语言任务拆解执行、25+ 办公连接器（Slack/GitHub/Jira/Notion/Gmail 等）、MCP 扩展、本地文件与终端访问、定时自动化、写操作审批门控，交付文档/表格/网页等成品。与 WorkBench 相似度：高（桌面 agent loop + 工具调用 + 定时任务 + 本地优先 + MCP，几乎同定位）。适用场景：知识工作者的日常任务自动化。发布约 5 天 GitHub 涨 7.6k Star，当前约 7k+。 | 完全免费开源（MIT 许可），无订阅、无功能限制、无需信用卡；需自带模型 API Key（BYOK）或通过 Ollama 全本地免费运行。macOS 版已签名，Windows 版可用但未签名（SmartScreen 会警告）。 | [官网](https://openworker.com) / [GitHub](https://github.com/andrewyng/openworker) / [文档](https://github.com/andrewyng/openworker/tree/main/docs) | 2026-07-31 | GitHub |
| 2 | OpenSquilla | 上海基元律动开源的微内核 AI Agent Harness 框架（Python 3.12+）：本地 LightGBM+ONNX 智能路由按复杂度选模型（宣称省 60-89% Token）、四层认知记忆、按需技能加载、三档安全沙箱、MCP 客户端/服务端、类 cron 定时任务、Web UI/CLI/IM 多入口统一 TurnRunner。7 月发布 0.4.0 引入 Coding 模式与「红绿回归」自我验证机制，当前稳定版 0.5.2。与 WorkBench 相似度：高（agent loop + 工具 + 记忆 + 技能 + 定时任务 + 沙箱）。适用场景：控制 Token 成本的 Agent 应用开发与个人助手。 | 完全免费开源（Apache-2.0），可自部署；提供免费桌面安装包（macOS/Windows，已签名公证）；需自带模型 API Key，支持 Ollama 本地模型零成本运行。 | [官网](https://www.opensquilla.ai) / [GitHub](https://github.com/opensquilla/opensquilla) / [文档](https://www.opensquilla.ai/zh/news/0.5.0-preview-2/) | 2026-07-30 | GitHub |
| 3 | Loom for AWS | AWS 官方（awslabs）开源的企业级 AI Agent 构建/部署/运营平台，基于 Amazon Bedrock AgentCore Runtime 与 Strands Agents SDK：统一管理 UI、Agent 全生命周期管理、记忆存储、MCP 服务器、A2A 集成、Agent Registry 治理、预验证配置蓝图（约 40 分钟完成部署），支持 OpenAI/Anthropic/LiteLLM 等替代模型。与 WorkBench 相似度：中（侧重企业级 Agent 部署运营编排而非个人桌面助手）。适用场景：企业在 AWS 上快速落地受管控的 AI Agent。 | 平台代码免费开源（Apache-2.0）可自部署；但运行依赖 AWS 云服务（Bedrock/ECS Fargate 等）按用量计费，模型推理费用另计。 | [官网](https://github.com/awslabs/loom) / [GitHub](https://github.com/awslabs/loom) | 2026-07-10 | 社区 |
| 4 | Multica | 前 TikTok 工程师团队开源的「受管 AI Agent 团队协作平台」：把 Claude Code、Codex、OpenClaw、OpenCode、Kimi 等 12 款编码 agent 变成看板上的正式队友——指派 issue 即自动领取、执行、汇报进度，支持技能沉淀复用、本地/云端 Runtime 统一监控、多工作空间隔离，Docker Compose/K8s 自托管。与 WorkBench 相似度：中（多智能体任务编排与管理层，厂商中立，但不含自有 agent 引擎）。适用场景：人机混合团队的多 Agent 并行开发管理。 | 开源可免费自托管（许可证对 SaaS 转售有商业限制条款）；另提供托管云版本；底层 agent 运行时费用取决于所接入的模型/CLI（用 OpenCode/OpenClaw 等开源运行时可零边际成本）。 | [官网](https://www.multica.ai) / [GitHub](https://github.com/multica-ai/multica) / [文档](https://multica.ai/docs/self-host-quickstart) | 2026-06-04 | 导航站 |
| 5 | HuggingFace ZeroGPU（免费政策重大变化） | HuggingFace 于 2026-07-13 宣布 ZeroGPU 共享 GPU 算力向全部注册用户免费开放（此前仅限 Pro 等受限用户），并发布配套 agent skill，使编码 agent 可通过一句自然语言指令自动创建并部署 GPU 加速的 Spaces 应用；每个 Gradio Space 还暴露 agents.md 供 agent 直接程序化调用。与 WorkBench 相似度：中（提供 agent 可编程调用的免费算力/部署底座，而非 agent 构建器本身）。适用场景：零成本部署 agent 演示应用、为 agent 提供免费 GPU 工具链。 | 所有注册用户免费创建 ZeroGPU Spaces（免费层 2 vCPU/16GB RAM），无需信用卡；GPU 为共享分时配额制，具体限流未公布，Pro 用户配额更高。 | [官网](https://huggingface.co/new-space) / [GitHub](https://github.com/huggingface/skills/tree/main/skills/huggingface-spaces) / [文档](https://huggingface.co/docs/hub/spaces-agents) | 2026-07-13 | HuggingFace |

## 详细信息

### 1. OpenWorker

- **功能描述**：吴恩达（Andrew Ng）团队开源的桌面 AI Agent（AI coworker），基于 aisuite 构建：自然语言任务拆解执行、25+ 办公连接器（Slack/GitHub/Jira/Notion/Gmail 等）、MCP 扩展、本地文件与终端访问、定时自动化、写操作审批门控，交付文档/表格/网页等成品。与 WorkBench 相似度：高（桌面 agent loop + 工具调用 + 定时任务 + 本地优先 + MCP，几乎同定位）。适用场景：知识工作者的日常任务自动化。发布约 5 天 GitHub 涨 7.6k Star，当前约 7k+。
- **免费使用方式**：完全免费开源（MIT 许可），无订阅、无功能限制、无需信用卡；需自带模型 API Key（BYOK）或通过 Ollama 全本地免费运行。macOS 版已签名，Windows 版可用但未签名（SmartScreen 会警告）。
- **官网**：https://openworker.com
- **GitHub**：https://github.com/andrewyng/openworker
- **文档**：https://github.com/andrewyng/openworker/tree/main/docs
- **最后更新日期**：2026-07-31
- **发现渠道**：GitHub

### 2. OpenSquilla

- **功能描述**：上海基元律动开源的微内核 AI Agent Harness 框架（Python 3.12+）：本地 LightGBM+ONNX 智能路由按复杂度选模型（宣称省 60-89% Token）、四层认知记忆、按需技能加载、三档安全沙箱、MCP 客户端/服务端、类 cron 定时任务、Web UI/CLI/IM 多入口统一 TurnRunner。7 月发布 0.4.0 引入 Coding 模式与「红绿回归」自我验证机制，当前稳定版 0.5.2。与 WorkBench 相似度：高（agent loop + 工具 + 记忆 + 技能 + 定时任务 + 沙箱）。适用场景：控制 Token 成本的 Agent 应用开发与个人助手。
- **免费使用方式**：完全免费开源（Apache-2.0），可自部署；提供免费桌面安装包（macOS/Windows，已签名公证）；需自带模型 API Key，支持 Ollama 本地模型零成本运行。
- **官网**：https://www.opensquilla.ai
- **GitHub**：https://github.com/opensquilla/opensquilla
- **文档**：https://www.opensquilla.ai/zh/news/0.5.0-preview-2/
- **最后更新日期**：2026-07-30
- **发现渠道**：GitHub

### 3. Loom for AWS

- **功能描述**：AWS 官方（awslabs）开源的企业级 AI Agent 构建/部署/运营平台，基于 Amazon Bedrock AgentCore Runtime 与 Strands Agents SDK：统一管理 UI、Agent 全生命周期管理、记忆存储、MCP 服务器、A2A 集成、Agent Registry 治理、预验证配置蓝图（约 40 分钟完成部署），支持 OpenAI/Anthropic/LiteLLM 等替代模型。与 WorkBench 相似度：中（侧重企业级 Agent 部署运营编排而非个人桌面助手）。适用场景：企业在 AWS 上快速落地受管控的 AI Agent。
- **免费使用方式**：平台代码免费开源（Apache-2.0）可自部署；但运行依赖 AWS 云服务（Bedrock/ECS Fargate 等）按用量计费，模型推理费用另计。
- **官网**：https://github.com/awslabs/loom
- **GitHub**：https://github.com/awslabs/loom
- **文档**：-
- **最后更新日期**：2026-07-10
- **发现渠道**：社区

### 4. Multica

- **功能描述**：前 TikTok 工程师团队开源的「受管 AI Agent 团队协作平台」：把 Claude Code、Codex、OpenClaw、OpenCode、Kimi 等 12 款编码 agent 变成看板上的正式队友——指派 issue 即自动领取、执行、汇报进度，支持技能沉淀复用、本地/云端 Runtime 统一监控、多工作空间隔离，Docker Compose/K8s 自托管。与 WorkBench 相似度：中（多智能体任务编排与管理层，厂商中立，但不含自有 agent 引擎）。适用场景：人机混合团队的多 Agent 并行开发管理。
- **免费使用方式**：开源可免费自托管（许可证对 SaaS 转售有商业限制条款）；另提供托管云版本；底层 agent 运行时费用取决于所接入的模型/CLI（用 OpenCode/OpenClaw 等开源运行时可零边际成本）。
- **官网**：https://www.multica.ai
- **GitHub**：https://github.com/multica-ai/multica
- **文档**：https://multica.ai/docs/self-host-quickstart
- **最后更新日期**：2026-06-04
- **发现渠道**：导航站

### 5. HuggingFace ZeroGPU（免费政策重大变化）

- **功能描述**：HuggingFace 于 2026-07-13 宣布 ZeroGPU 共享 GPU 算力向全部注册用户免费开放（此前仅限 Pro 等受限用户），并发布配套 agent skill，使编码 agent 可通过一句自然语言指令自动创建并部署 GPU 加速的 Spaces 应用；每个 Gradio Space 还暴露 agents.md 供 agent 直接程序化调用。与 WorkBench 相似度：中（提供 agent 可编程调用的免费算力/部署底座，而非 agent 构建器本身）。适用场景：零成本部署 agent 演示应用、为 agent 提供免费 GPU 工具链。
- **免费使用方式**：所有注册用户免费创建 ZeroGPU Spaces（免费层 2 vCPU/16GB RAM），无需信用卡；GPU 为共享分时配额制，具体限流未公布，Pro 用户配额更高。
- **官网**：https://huggingface.co/new-space
- **GitHub**：https://github.com/huggingface/skills/tree/main/skills/huggingface-spaces
- **文档**：https://huggingface.co/docs/hub/spaces-agents
- **最后更新日期**：2026-07-13
- **发现渠道**：HuggingFace
