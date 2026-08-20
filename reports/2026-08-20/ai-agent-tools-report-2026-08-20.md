# 每日 AI Agent 工具扫描报告 - 2026-08-20

> 搜索截止日期：2026-08-20 ｜ 生成时间：2026-08-20 10:07:07 ｜ 发现工具数：4

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | Cloudflare OS | 基于 Cloudflare Workers 的开源智能体工作区 + 应用平台（被设计者称为 'Sandstorm with AI'）。团队可用自然语言构建文档、全栈'小工具'(Gadgets)与常驻 Agent；内置零信任 Gatekeeper 按能力细粒度授权、共享公司上下文与技能；模型无关，支持本地 Ollama。与 WorkBench 相似度：高（可视化智能体工作区 + 应用/工作流编排 + 多模型 + 本地优先）；适用：企业知识驱动的 Agent 协作与内部工具搭建。 | 代码 Apache-2.0 完全开源、可自托管（基于开源 workerd 运行时，支持本地 Ollama，Varda 称本地运行更快）。但部署到 Cloudflare 云端需 Workers Paid 计划（HN 反馈免费层无法运行 Dynamic Workers）；本地运行 workerd 可规避。克隆仓库无需信用卡。 | [官网](https://os.cloudflare.app) / [GitHub](https://github.com/cloudflare/cloudflare-os) / [文档](https://blog.cloudflare.com/cloudflare-os/) | 2026-08-20 | GitHub |
| 2 | OpenGEni | 面向组织的开源、可自托管智能体运行时：提供持久化、可回放的 Agent 会话、人工审批节点、受治理的凭据与记忆，运行于托管沙箱或自有硬件。与 WorkBench 相似度：高（Agent 运行时 + 编排 + 凭据/记忆治理 + 自托管）；适用：企业/团队构建可控、可审计的自动化 Agent。 | Apache-2.0 开源，可完全自托管（Docker/自有硬件），免费使用；可选托管沙箱。无使用限制与信用卡要求。 | [官网](https://opengeni.ai/) / [GitHub](https://github.com/Cloudgeni-ai/opengeni) | 2026-08-19 | GitHub |
| 3 | MkAgent | 本地优先（local-first）的 AI Agent 工作区，基于 Pi Agent 运行时，提供桌面端/WebUI/CLI 三种形态；内置浏览器与文档工具、Skills 扩展机制、会话分支与计划、多模型连接（ChatGPT Plus / Claude Pro / OpenAI·Anthropic 兼容端点 / 本地 Ollama）。同时是构建自定义桌面 Agent 产品的开发基座。与 WorkBench 相似度：高（通用 Agent 工具 + 可扩展重建为自有 Agent 产品 + 工作流）；适用：个人本地 Agent 工作台与开发者二次开发。 | Apache-2.0 开源，本地优先、BYOK（自带密钥）免费使用；支持本地 Ollama 无需云端账单。无强制付费，无需信用卡。 | [官网](https://mkagent.app) / [GitHub](https://github.com/MkThingsHQ/mkagent) | 2026-08-16 | 社区 |
| 4 | Omniwork | 面向创意工作的'Agent OS'：桌面端工作区用一组专家 Agent（趋势追踪、爆款复刻、社媒文案、视频/音乐/配音、账号监控等）围绕一个目标协作，完成'从选题到发布后监控'的全流程编排，并保留团队/项目共享记忆。与 WorkBench 相似度：中高（多 Agent 编排 + 工作流 + 共享记忆 + 目标驱动）；适用：内容创作者/营销团队的创意流水线自动化。 | Freemium：Starter 免费档含 100+ AI Agent、每月 5 次 Deep tasks、基础集成，无需信用卡；Pro 约 $69/月（官方文案 Deep tasks 额度口径不一致，约 30–90 次/月）；Ultimate 企业定制。免费层额度有限，属试用性质。 | [官网](https://www.omniwork.ai/) | 2026-08-09 | ProductHunt |

## 详细信息

### 1. Cloudflare OS

- **功能描述**：基于 Cloudflare Workers 的开源智能体工作区 + 应用平台（被设计者称为 'Sandstorm with AI'）。团队可用自然语言构建文档、全栈'小工具'(Gadgets)与常驻 Agent；内置零信任 Gatekeeper 按能力细粒度授权、共享公司上下文与技能；模型无关，支持本地 Ollama。与 WorkBench 相似度：高（可视化智能体工作区 + 应用/工作流编排 + 多模型 + 本地优先）；适用：企业知识驱动的 Agent 协作与内部工具搭建。
- **免费使用方式**：代码 Apache-2.0 完全开源、可自托管（基于开源 workerd 运行时，支持本地 Ollama，Varda 称本地运行更快）。但部署到 Cloudflare 云端需 Workers Paid 计划（HN 反馈免费层无法运行 Dynamic Workers）；本地运行 workerd 可规避。克隆仓库无需信用卡。
- **官网**：https://os.cloudflare.app
- **GitHub**：https://github.com/cloudflare/cloudflare-os
- **文档**：https://blog.cloudflare.com/cloudflare-os/
- **最后更新日期**：2026-08-20
- **发现渠道**：GitHub

### 2. OpenGEni

- **功能描述**：面向组织的开源、可自托管智能体运行时：提供持久化、可回放的 Agent 会话、人工审批节点、受治理的凭据与记忆，运行于托管沙箱或自有硬件。与 WorkBench 相似度：高（Agent 运行时 + 编排 + 凭据/记忆治理 + 自托管）；适用：企业/团队构建可控、可审计的自动化 Agent。
- **免费使用方式**：Apache-2.0 开源，可完全自托管（Docker/自有硬件），免费使用；可选托管沙箱。无使用限制与信用卡要求。
- **官网**：https://opengeni.ai/
- **GitHub**：https://github.com/Cloudgeni-ai/opengeni
- **文档**：-
- **最后更新日期**：2026-08-19
- **发现渠道**：GitHub

### 3. MkAgent

- **功能描述**：本地优先（local-first）的 AI Agent 工作区，基于 Pi Agent 运行时，提供桌面端/WebUI/CLI 三种形态；内置浏览器与文档工具、Skills 扩展机制、会话分支与计划、多模型连接（ChatGPT Plus / Claude Pro / OpenAI·Anthropic 兼容端点 / 本地 Ollama）。同时是构建自定义桌面 Agent 产品的开发基座。与 WorkBench 相似度：高（通用 Agent 工具 + 可扩展重建为自有 Agent 产品 + 工作流）；适用：个人本地 Agent 工作台与开发者二次开发。
- **免费使用方式**：Apache-2.0 开源，本地优先、BYOK（自带密钥）免费使用；支持本地 Ollama 无需云端账单。无强制付费，无需信用卡。
- **官网**：https://mkagent.app
- **GitHub**：https://github.com/MkThingsHQ/mkagent
- **文档**：-
- **最后更新日期**：2026-08-16
- **发现渠道**：社区

### 4. Omniwork

- **功能描述**：面向创意工作的'Agent OS'：桌面端工作区用一组专家 Agent（趋势追踪、爆款复刻、社媒文案、视频/音乐/配音、账号监控等）围绕一个目标协作，完成'从选题到发布后监控'的全流程编排，并保留团队/项目共享记忆。与 WorkBench 相似度：中高（多 Agent 编排 + 工作流 + 共享记忆 + 目标驱动）；适用：内容创作者/营销团队的创意流水线自动化。
- **免费使用方式**：Freemium：Starter 免费档含 100+ AI Agent、每月 5 次 Deep tasks、基础集成，无需信用卡；Pro 约 $69/月（官方文案 Deep tasks 额度口径不一致，约 30–90 次/月）；Ultimate 企业定制。免费层额度有限，属试用性质。
- **官网**：https://www.omniwork.ai/
- **GitHub**：-
- **文档**：-
- **最后更新日期**：2026-08-09
- **发现渠道**：ProductHunt
