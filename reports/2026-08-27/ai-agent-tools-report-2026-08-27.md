# 每日 AI Agent 工具扫描报告 - 2026-08-27

> 搜索截止日期：2026-08-27 ｜ 生成时间：2026-08-27 10:11:21 ｜ 发现工具数：4

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | Offloop | AI-native 共享工作区，让团队成员与多个 AI Agent 在同一空间内规划、执行、追踪多步工作；支持按请求拆任务、跨 Agent/人员委派、可复用 Agent 与 Flow、审批门控、BYO 模型（无加价）。相似度：高（与 WorkBench 同为「人 + Agent 协作编排 / 工作流」平台）。适用：AI-native 小团队把个人 AI 产出转化为可追踪的团队进度。 | 免费额度——创建工作区后整个团队获 30 天免费 AI 额度（free AI credits）；支持自带模型订阅（BYOP）且不对运行加价。无明确长期免费档，属 freemium（Product Hunt 2026-08-24 上线，当日 #3）。 | [官网](https://www.producthunt.com/products/offloop) | 2026-08-24 | ProductHunt |
| 2 | LightAgent | 超轻量、可「成长」的 Python 智能体框架，原生支持 Skill；融合记忆（mem0）、工具、思维树（ToT）与多智能体协作，MCP（stdio/sse）开箱即连，零成本切换底层模型（OpenAI/智谱 ChatGLM/DeepSeek/阶跃/通义等），开箱即用 OpenAI 流式 API。相似度：高（开源 Agent 框架，对标 WorkBench 的 Agent 构建 / 编排）。2026-08-15 发布 v0.10.0 开发版（统一事件溯源 Agent Runtime、可持久化 Session、异步执行、Jobs/子 Agent、标准化 Skills/MCP 适配器）。 | 开源 Apache-2.0，免费自托管/本地运行（pip 安装），无付费墙。 | [官网](https://github.com/wanxingai/LightAgent) / [GitHub](https://github.com/wanxingai/LightAgent) | 2026-08-21 | GitHub |
| 3 | Agent Mesh | 面向「人 + 多 Agent」的本地可审计协调与决策追踪库（Python 标准库实现，无第三方依赖），通过 SQLite 共享记忆 / 决策日志减少 Agent drift，支持 CLAUDE.md/AGENTS.md 自动迁移工作流、Workbench 看板；Agent 无关，可接入任意 Agent。相似度：中（Agent 间协调 / 共享记忆基础设施，辅助构建多 Agent 系统，非完整构建平台）。适用：已有 coding agent 的团队做多 Agent 协同与审计。 | 开源 MIT，可 pip install my-agent-mesh 免费使用，无托管依赖、无模型供应商绑定。 | [官网](https://github.com/cbalgeman/agent-mesh) / [GitHub](https://github.com/cbalgeman/agent-mesh) | 2026-08-15 | 社区 |
| 4 | Pacific Slate | 自托管、模型无关的多智能体 AI 助手系统（架构蓝图 / 可复刻实现）：8 个 Agent（1 路由 + 7 专家：代码/研究/分析/效率/审查/评估等）按任务路由到最合适的模型；四层记忆架构、混合检索、数据私有权（可导出/删除、不用作训练）；支持 Ollama 本地与外接 API。相似度：中高（自托管多 Agent 编排、私有 AI 助手基础设施，对标 WorkBench 的本地 Agent 编排）。适用：个人/小团队构建隐私优先的私有 Agent 系统。 | 开源架构/实现，可自托管，模型无关（接 Ollama 或任意 OpenAI 兼容端点），无许可费用。 | [官网](https://pacslate.com) | unknown | 社区 |

## 详细信息

### 1. Offloop

- **功能描述**：AI-native 共享工作区，让团队成员与多个 AI Agent 在同一空间内规划、执行、追踪多步工作；支持按请求拆任务、跨 Agent/人员委派、可复用 Agent 与 Flow、审批门控、BYO 模型（无加价）。相似度：高（与 WorkBench 同为「人 + Agent 协作编排 / 工作流」平台）。适用：AI-native 小团队把个人 AI 产出转化为可追踪的团队进度。
- **免费使用方式**：免费额度——创建工作区后整个团队获 30 天免费 AI 额度（free AI credits）；支持自带模型订阅（BYOP）且不对运行加价。无明确长期免费档，属 freemium（Product Hunt 2026-08-24 上线，当日 #3）。
- **官网**：https://www.producthunt.com/products/offloop
- **GitHub**：-
- **文档**：-
- **最后更新日期**：2026-08-24
- **发现渠道**：ProductHunt

### 2. LightAgent

- **功能描述**：超轻量、可「成长」的 Python 智能体框架，原生支持 Skill；融合记忆（mem0）、工具、思维树（ToT）与多智能体协作，MCP（stdio/sse）开箱即连，零成本切换底层模型（OpenAI/智谱 ChatGLM/DeepSeek/阶跃/通义等），开箱即用 OpenAI 流式 API。相似度：高（开源 Agent 框架，对标 WorkBench 的 Agent 构建 / 编排）。2026-08-15 发布 v0.10.0 开发版（统一事件溯源 Agent Runtime、可持久化 Session、异步执行、Jobs/子 Agent、标准化 Skills/MCP 适配器）。
- **免费使用方式**：开源 Apache-2.0，免费自托管/本地运行（pip 安装），无付费墙。
- **官网**：https://github.com/wanxingai/LightAgent
- **GitHub**：https://github.com/wanxingai/LightAgent
- **文档**：-
- **最后更新日期**：2026-08-21
- **发现渠道**：GitHub

### 3. Agent Mesh

- **功能描述**：面向「人 + 多 Agent」的本地可审计协调与决策追踪库（Python 标准库实现，无第三方依赖），通过 SQLite 共享记忆 / 决策日志减少 Agent drift，支持 CLAUDE.md/AGENTS.md 自动迁移工作流、Workbench 看板；Agent 无关，可接入任意 Agent。相似度：中（Agent 间协调 / 共享记忆基础设施，辅助构建多 Agent 系统，非完整构建平台）。适用：已有 coding agent 的团队做多 Agent 协同与审计。
- **免费使用方式**：开源 MIT，可 pip install my-agent-mesh 免费使用，无托管依赖、无模型供应商绑定。
- **官网**：https://github.com/cbalgeman/agent-mesh
- **GitHub**：https://github.com/cbalgeman/agent-mesh
- **文档**：-
- **最后更新日期**：2026-08-15
- **发现渠道**：社区

### 4. Pacific Slate

- **功能描述**：自托管、模型无关的多智能体 AI 助手系统（架构蓝图 / 可复刻实现）：8 个 Agent（1 路由 + 7 专家：代码/研究/分析/效率/审查/评估等）按任务路由到最合适的模型；四层记忆架构、混合检索、数据私有权（可导出/删除、不用作训练）；支持 Ollama 本地与外接 API。相似度：中高（自托管多 Agent 编排、私有 AI 助手基础设施，对标 WorkBench 的本地 Agent 编排）。适用：个人/小团队构建隐私优先的私有 Agent 系统。
- **免费使用方式**：开源架构/实现，可自托管，模型无关（接 Ollama 或任意 OpenAI 兼容端点），无许可费用。
- **官网**：https://pacslate.com
- **GitHub**：-
- **文档**：-
- **最后更新日期**：unknown
- **发现渠道**：社区
