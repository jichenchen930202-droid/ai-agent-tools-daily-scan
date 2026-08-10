# 每日 AI Agent 工具扫描报告 - 2026-08-10

> 搜索截止日期：2026-08-10 ｜ 生成时间：2026-08-10 10:13:03 ｜ 发现工具数：11

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | AxisAgentic | 长周期（long-horizon）智能体运行时 + 轨迹采集框架，支持多步任务规划、工具调用与可回放的轨迹记录，定位接近 WorkBench 的「自主智能体执行」能力。开源可自部署，需自备 OpenAI 兼容模型端点。 | Apache-2.0 开源，可免费自托管；需 Python 3.12+ 与 OpenAI 兼容 API 端点（自付模型费用），无商业限制。 | [官网](https://github.com/XYZ-AI-Lab/AxisAgentic) / [GitHub](https://github.com/XYZ-AI-Lab/AxisAgentic) | 2026-07-24 | GitHub |
| 2 | phone-harness | 让智能体通过 macOS「iPhone 镜像」远程控制真实 iPhone 的 harness：结合 screencapture 截图 + Vision OCR + CoreGraphics 事件注入，无需越狱即可让 Agent 操作手机 App，与 WorkBench「让 Agent 操控图形界面」思路一致。 | MIT 开源，免费自托管；仅需 macOS + iPhone 镜像，无需付费或 API 密钥（可接任意本地/云端视觉模型）。 | [官网](https://github.com/ShawnPana/phone-harness) / [GitHub](https://github.com/ShawnPana/phone-harness) | 2026-08-10 | GitHub |
| 3 | KADATH | 进化式（evolutionary）多智能体运行时：以种群/迭代方式演化 Agent 策略并自我改进，提供编排、评估与回放，类似 WorkBench 的多智能体协作编排能力。 | Apache-2.0 开源，可免费自部署（Docker）；需自备 OpenAI API Key（自付模型费用）。 | [官网](https://github.com/i3T4AN/KADATH) / [GitHub](https://github.com/i3T4AN/KADATH) | 2026-08-09 | GitHub |
| 4 | DeterminFlow | 面向生产的 AI 工作流运行时，提供可视化编排与稳定的确定性执行（Docker + Web UI :8020），对标 WorkBench 的「低代码/可视化 Agent 工作流编排」能力。 | AGPL-3.0 开源，可免费自托管（含商用自有部署义务的场景需留意 AGPL）；v0.1.0 已发布，需自备 DeepSeek API Key。 | [官网](https://github.com/alikon-art/DeterminFlow) / [GitHub](https://github.com/alikon-art/DeterminFlow) | 2026-08-09 | GitHub |
| 5 | grok-build | xAI 出品的编码智能体 harness（TUI），内置 MCP / skills / plugins / hooks / subagents 机制，定位类似 WorkBench「可扩展智能体工作台」，但偏向代码场景。 | Apache-2.0 开源；需 xAI 账号与 API Key（仅限 xAI 模型），免费层取决于 xAI 账户政策。 | [官网](https://github.com/xai-org/grok-build) / [GitHub](https://github.com/xai-org/grok-build) | 2026-08-09 | GitHub |
| 6 | better-harness | 面向编码智能体（Claude Code / Codex / Cursor / Qoder / Copilot）的「循环级（loop-level）」洞察工具，记录并分析 Agent 的每一步决策以优化 harness，提供可观测与调优能力，类似 WorkBench 背后的执行可观测理念。 | MIT 开源，免费自托管；0.5.0 已发布，连接你已有的编码智能体即可使用。 | [官网](https://github.com/QoderAI/better-harness) / [GitHub](https://github.com/QoderAI/better-harness) | 2026-08-06 | GitHub |
| 7 | agentsmith | 模型无关（model-agnostic）的 AI 智能体操作 harness，统一封装不同模型的 Agent 运行/工具调用，与 WorkBench「跨模型 Agent 运行」目标一致。 | MIT 开源，免费自托管；需自备模型 API（自付费用），无订阅限制。 | [官网](https://github.com/PromptPartner/agentsmith) / [GitHub](https://github.com/PromptPartner/agentsmith) | 2026-08-08 | GitHub |
| 8 | operator-oss | 本地优先（local-first）的并行智能体编排器：用 git worktree 隔离多个 Claude Code / Codex 会话并行工作，无需 API Key（使用订阅登录），类似 WorkBench 的并行任务编排。 | Apache-2.0 开源，免费自托管；需 Node 20.9+，使用你的订阅账号登录，无额外密钥费用。 | [官网](https://github.com/iishyfishyy/operator-oss) / [GitHub](https://github.com/iishyfishyy/operator-oss) | 2026-08-09 | GitHub |
| 9 | agents-council | Claude Code 的多智能体协作插件：让多个角色 Agent 组成「委员会」共同拆解与执行任务，对标 WorkBench 的多 Agent 协作编排。 | MIT 开源，免费自托管；作为 Claude Code 插件使用，需自备 Claude 订阅/API。 | [官网](https://github.com/0xwilliamortiz/agents-council) / [GitHub](https://github.com/0xwilliamortiz/agents-council) | 2026-07-30 | GitHub |
| 10 | frakio-work | 多智能体 AI 工作台，采用 Hermes + Pi 双核架构协同处理任务，提供 Agent 编排与工作流面板，与 WorkBench 的「多智能体工作台」定位接近。 | MIT 开源，免费自托管；需自备模型 API（自付费用）。 | [官网](https://github.com/MadsGao/frakio-work) / [GitHub](https://github.com/MadsGao/frakio-work) | 2026-08-07 | GitHub |
| 11 | Toolport | 免费的本地 MCP 网关：一次性配置 MCP server（GitHub/Slack/数据库等工具连接器），所有 Agent（Claude/Cursor/Codex 等）共享同一套工具；按需懒加载工具定义以大幅降低上下文 token 占用，并内置工具完整性校验与密钥本地保管，是 Agent 工具接入层的开源基础设施。 | MIT 开源，完全免费；无账号、无云端，本地运行；Teams 版最多 5 人免费。 | [官网](https://toolport.app/) / [GitHub](https://github.com/tsouth89/toolport) / [文档](https://toolport.app/) | 2026-08-08 | ProductHunt |

## 详细信息

### 1. AxisAgentic

- **功能描述**：长周期（long-horizon）智能体运行时 + 轨迹采集框架，支持多步任务规划、工具调用与可回放的轨迹记录，定位接近 WorkBench 的「自主智能体执行」能力。开源可自部署，需自备 OpenAI 兼容模型端点。
- **免费使用方式**：Apache-2.0 开源，可免费自托管；需 Python 3.12+ 与 OpenAI 兼容 API 端点（自付模型费用），无商业限制。
- **官网**：https://github.com/XYZ-AI-Lab/AxisAgentic
- **GitHub**：https://github.com/XYZ-AI-Lab/AxisAgentic
- **文档**：-
- **最后更新日期**：2026-07-24
- **发现渠道**：GitHub

### 2. phone-harness

- **功能描述**：让智能体通过 macOS「iPhone 镜像」远程控制真实 iPhone 的 harness：结合 screencapture 截图 + Vision OCR + CoreGraphics 事件注入，无需越狱即可让 Agent 操作手机 App，与 WorkBench「让 Agent 操控图形界面」思路一致。
- **免费使用方式**：MIT 开源，免费自托管；仅需 macOS + iPhone 镜像，无需付费或 API 密钥（可接任意本地/云端视觉模型）。
- **官网**：https://github.com/ShawnPana/phone-harness
- **GitHub**：https://github.com/ShawnPana/phone-harness
- **文档**：-
- **最后更新日期**：2026-08-10
- **发现渠道**：GitHub

### 3. KADATH

- **功能描述**：进化式（evolutionary）多智能体运行时：以种群/迭代方式演化 Agent 策略并自我改进，提供编排、评估与回放，类似 WorkBench 的多智能体协作编排能力。
- **免费使用方式**：Apache-2.0 开源，可免费自部署（Docker）；需自备 OpenAI API Key（自付模型费用）。
- **官网**：https://github.com/i3T4AN/KADATH
- **GitHub**：https://github.com/i3T4AN/KADATH
- **文档**：-
- **最后更新日期**：2026-08-09
- **发现渠道**：GitHub

### 4. DeterminFlow

- **功能描述**：面向生产的 AI 工作流运行时，提供可视化编排与稳定的确定性执行（Docker + Web UI :8020），对标 WorkBench 的「低代码/可视化 Agent 工作流编排」能力。
- **免费使用方式**：AGPL-3.0 开源，可免费自托管（含商用自有部署义务的场景需留意 AGPL）；v0.1.0 已发布，需自备 DeepSeek API Key。
- **官网**：https://github.com/alikon-art/DeterminFlow
- **GitHub**：https://github.com/alikon-art/DeterminFlow
- **文档**：-
- **最后更新日期**：2026-08-09
- **发现渠道**：GitHub

### 5. grok-build

- **功能描述**：xAI 出品的编码智能体 harness（TUI），内置 MCP / skills / plugins / hooks / subagents 机制，定位类似 WorkBench「可扩展智能体工作台」，但偏向代码场景。
- **免费使用方式**：Apache-2.0 开源；需 xAI 账号与 API Key（仅限 xAI 模型），免费层取决于 xAI 账户政策。
- **官网**：https://github.com/xai-org/grok-build
- **GitHub**：https://github.com/xai-org/grok-build
- **文档**：-
- **最后更新日期**：2026-08-09
- **发现渠道**：GitHub

### 6. better-harness

- **功能描述**：面向编码智能体（Claude Code / Codex / Cursor / Qoder / Copilot）的「循环级（loop-level）」洞察工具，记录并分析 Agent 的每一步决策以优化 harness，提供可观测与调优能力，类似 WorkBench 背后的执行可观测理念。
- **免费使用方式**：MIT 开源，免费自托管；0.5.0 已发布，连接你已有的编码智能体即可使用。
- **官网**：https://github.com/QoderAI/better-harness
- **GitHub**：https://github.com/QoderAI/better-harness
- **文档**：-
- **最后更新日期**：2026-08-06
- **发现渠道**：GitHub

### 7. agentsmith

- **功能描述**：模型无关（model-agnostic）的 AI 智能体操作 harness，统一封装不同模型的 Agent 运行/工具调用，与 WorkBench「跨模型 Agent 运行」目标一致。
- **免费使用方式**：MIT 开源，免费自托管；需自备模型 API（自付费用），无订阅限制。
- **官网**：https://github.com/PromptPartner/agentsmith
- **GitHub**：https://github.com/PromptPartner/agentsmith
- **文档**：-
- **最后更新日期**：2026-08-08
- **发现渠道**：GitHub

### 8. operator-oss

- **功能描述**：本地优先（local-first）的并行智能体编排器：用 git worktree 隔离多个 Claude Code / Codex 会话并行工作，无需 API Key（使用订阅登录），类似 WorkBench 的并行任务编排。
- **免费使用方式**：Apache-2.0 开源，免费自托管；需 Node 20.9+，使用你的订阅账号登录，无额外密钥费用。
- **官网**：https://github.com/iishyfishyy/operator-oss
- **GitHub**：https://github.com/iishyfishyy/operator-oss
- **文档**：-
- **最后更新日期**：2026-08-09
- **发现渠道**：GitHub

### 9. agents-council

- **功能描述**：Claude Code 的多智能体协作插件：让多个角色 Agent 组成「委员会」共同拆解与执行任务，对标 WorkBench 的多 Agent 协作编排。
- **免费使用方式**：MIT 开源，免费自托管；作为 Claude Code 插件使用，需自备 Claude 订阅/API。
- **官网**：https://github.com/0xwilliamortiz/agents-council
- **GitHub**：https://github.com/0xwilliamortiz/agents-council
- **文档**：-
- **最后更新日期**：2026-07-30
- **发现渠道**：GitHub

### 10. frakio-work

- **功能描述**：多智能体 AI 工作台，采用 Hermes + Pi 双核架构协同处理任务，提供 Agent 编排与工作流面板，与 WorkBench 的「多智能体工作台」定位接近。
- **免费使用方式**：MIT 开源，免费自托管；需自备模型 API（自付费用）。
- **官网**：https://github.com/MadsGao/frakio-work
- **GitHub**：https://github.com/MadsGao/frakio-work
- **文档**：-
- **最后更新日期**：2026-08-07
- **发现渠道**：GitHub

### 11. Toolport

- **功能描述**：免费的本地 MCP 网关：一次性配置 MCP server（GitHub/Slack/数据库等工具连接器），所有 Agent（Claude/Cursor/Codex 等）共享同一套工具；按需懒加载工具定义以大幅降低上下文 token 占用，并内置工具完整性校验与密钥本地保管，是 Agent 工具接入层的开源基础设施。
- **免费使用方式**：MIT 开源，完全免费；无账号、无云端，本地运行；Teams 版最多 5 人免费。
- **官网**：https://toolport.app/
- **GitHub**：https://github.com/tsouth89/toolport
- **文档**：https://toolport.app/
- **最后更新日期**：2026-08-08
- **发现渠道**：ProductHunt
