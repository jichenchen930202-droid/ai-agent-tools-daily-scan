# 每日 AI Agent 工具扫描报告 - 2026-08-03

> 搜索截止日期：2026-08-03 ｜ 生成时间：2026-08-03 10:08:58 ｜ 发现工具数：7

## 汇总

| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |
|---|---------|---------|-------------|---------|---------|---------|
| 1 | QM (Quartermaster) | Y Combinator 于 2026-07-31 开源的公司级多智能体 harness（官方定位 Multiplayer agent harness for work）。为每位员工和每个项目分配相互隔离的 AI 工作区，各自拥有独立的记忆、文件、钥匙串、权限、cron 定时任务、Web 应用与沙箱，避免一个人的 agent 上下文泄漏到同事那里；原生集成 Slack 与 Web UI；模型/harness 无关，可由 Pi、OpenCode、OpenAI Codex、Claude Code 驱动同一套核心基础设施；提供 Strict（每次工具调用需人工批准）/ Auto（默认，分类器筛查外部数据）/ Dangerous 三档安全策略，agent 以员工本人凭据运行以形成可追溯审计链。与 WorkBench 相似度：高——同为通用任务型 Agent 运行时，具备工具调用、定时任务、文件与权限管理、多模型接入、沙箱执行。适用场景：中小企业与团队级 AI 智能体的统一部署、权限治理与审计。GitHub 7,323 stars / 768 forks（截至 2026-08-03）。 | MIT 许可证，完全开源、可自托管，软件本身零费用，无需信用卡。运行依赖自备 Postgres 实例（用于 session / memory / queue 持久化）与所选模型的 API 凭据，算力与模型调用成本自付。官方未提供付费托管版。 | [官网](https://qm.ycombinator.com) / [GitHub](https://github.com/yc-software/qm) | 2026-08-01 | GitHub |
| 2 | ego lite | citrolabs 开源的、专为 AI Agent 设计的 Chromium 浏览器，主张「同一浏览器，两个世界」：人类的日常标签页归人类，Agent 在隔离的 Space 中并行执行网页任务，互不抢占窗口。可迁移复用 Chrome 的书签、扩展、Cookie 与登录态，从而绕开 SSO / 2FA 反复登录问题；配套 ego-browser skill 把 snapshot / click / fill / navigate / wait / capture 暴露为 JavaScript 函数，Agent 可将多步网页任务写成一段 JS 一次执行，而非反复「调命令—看结果—再调命令」；Snapshot 语义快照集成进改造过的 Chromium 内核，能识别跨域 iframe、Shadow DOM 与第三方 SDK 组件，压缩进入模型上下文的数据量以降低 token 消耗。与 WorkBench 相似度：中——它不是完整的 Agent 编排平台，而是 Agent 的浏览器自动化执行底座，补齐「网页操作」这一关键能力。适用场景：资料调研、SaaS 后台操作、登录后页面读取、表单填写、无 API 网站取数、Vibe Coding 产物部署。2026-07-24 登上 GitHub Trending 日榜第一（当日 +884 star），截至 2026-08-03 已达 7,689 stars。 | MIT 许可证开源，官方明确为免费产品、无需注册账号即可使用，本地优先，登录态 / Cookie / 书签留在设备本地不上传。当前原生支持 macOS（ARM64 / x64 .dmg 直接下载），Windows / Linux 处于 roadmap 阶段。需自备 AI Agent（Claude Code / Codex / Cursor 等）与相应模型凭据，模型成本自付。无需信用卡。已知限制：作为完整 Chromium 分支 + 多 Space 并行，内存占用偏高。 | [官网](https://lite.ego.app) / [GitHub](https://github.com/citrolabs/ego-lite) / [文档](https://lite.ego.app/document/) | 2026-08-02 | GitHub |
| 3 | Kun | 本地优先（local-first）的 AI Agent 工作台，桌面 GUI（Electron）与终端 TUI 共享同一套本地 agent runtime，线程上下文、模型连接、审批、用量与后台任务全部互通，关闭任一客户端不中断后台工作。桌面端提供 Code / Design / Write / Connect phone 四种模式：Design 可把需求文本直接生成 UI 稿、信息图与可交互 HTML 原型；Write 集成文件树、Markdown 编辑、预览与写作助手并可导出 HTML/PDF/DOC；Connect phone 让飞书/Lark、微信、Telegram、webhook 与定时任务各走独立后台 agent 线程。核心范式为「需求→设计→计划→编码→验收」的需求驱动软件生产；Agent Graph 由 Lead 将目标拆解为带依赖、预算与验收标准的有向任务图，调度器按就绪集分派子智能体，Supervisor 聚合提交/失败/冲突/预算/求助/恢复/完成信号并扫描停滞节点触发 Lead 复盘。与 WorkBench 相似度：高——本地运行时 + 多智能体编排 + 定时任务 + 本地文件访问 + MCP 支持 + 多模型路由。适用场景：个人与小团队的编码、写作、设计、自动化一体化工作台。GitHub 5,608 stars。 | 官网提供 macOS（ARM64/x64）、Windows x64、Linux（AppImage/deb）安装包免费下载，最新版 v0.2.34（2026-08-02），客户端本身不收费，官网未列出任何付费套餐。模型侧需自带订阅（ChatGPT/Codex、Claude Pro/Max、Gemini、Cursor、Grok）或 API Key（DeepSeek、小米 MiMo、MiniMax、Kimi、GLM、Qwen、OpenAI 兼容端点、自托管模型），登录、配额与可用模型遵循各模型提供方条款，模型成本自付。注意：GitHub 仓库许可证被标记为 Other / NOASSERTION，并非标准 OSI 许可证，商用与二次分发条款需自行查阅仓库 LICENSE 文件。是否需要信用卡：unknown。 | [官网](https://www.kun-agent.com) / [GitHub](https://github.com/KunAgent/Kun) | 2026-08-02 | GitHub |
| 4 | StaffDeck | OpenBMB（面壁智能开源社区）2026 年 7 月开源的企业级数字员工平台（Enterprise Digital Employee Platform）。业务人员用大白话描述一段流程（例如「差旅报销先收集事由金额行程，再核对是否超标，超标转财务负责人审批」），平台自动将其转译为精密的可执行 Agent 流程图；运行时支持流程中断—检索企业知识库—带出处返回—回到原表单继续填写的上下文管理，遇到制度未覆盖的盲区会把完整上下文打包转交人工，人工审批后的新规则可沉淀为长期记忆。内置能力包括完全私有化部署（除源码安装外提供各操作系统一键安装包）、按每日/每周/每月或一次性计划主动执行任务并推送结果、原生 MCP 协议 + HTTP API 打通 ERP / CRM / OA 系统。Preview 预览版附带财务报销、法务合规、人事服务、IT 支持、行政管家五个现成数字员工，各配完整 SOP 与知识库。与 WorkBench 相似度：高——自然语言构建流程、工具调用、定时任务、知识库与记忆系统、私有化部署。适用场景：央国企、金融等对数据合规要求严苛、需要数据不出域的企业内部智能体落地。GitHub 1,355 stars。 | AGPL-3.0 许可证开源，可免费下载自部署，无需信用卡。需注意 AGPL-3.0 的传染性：基于其修改并对外提供网络服务时须同样开源，闭源商用存在许可证约束。模型推理与服务器成本自付。当前为 Preview 预览版，功能仍在迭代。 | [官网](http://staffdeck.openbmb.cn/) / [GitHub](https://github.com/OpenBMB/StaffDeck) | 2026-08-03 | 社区 |
| 5 | Buzz | Block（Jack Dorsey 旗下公司）开源的「蜂群思维」人机协同通信平台，基于 Nostr 协议、支持自托管。人类用户与 AI Agent 共享同一套频道、身份模型与审计日志，Agent 拥有独立密钥与身份，可打开代码仓库、发送补丁、审查代码、运行 YAML 工作流、编辑画布与管理频道；团队可围绕功能分支创建房间，把对话、补丁、CI 结果、评审与合并决策统一记录并可检索。目前中继服务、频道、画布、搜索、审计日志与 YAML 工作流已可用，工作流审批门禁与语音 Huddle 生命周期事件仍在接入中。与 WorkBench 相似度：中高——具备多智能体协作编排、工作流自动化、工具调用与审计追溯，但组织形态是团队通信频道而非单机工作台。适用场景：把 AI Agent 作为拥有独立身份与权限的团队成员纳入研发协作流程。GitHub 21,106 stars / 2,260 forks。注：仓库建于 2026-03-06，并非近 30 天新开源项目，本次因其登上 GitHub Trending 且此前未被本扫描收录而首次纳入。 | Apache-2.0 许可证开源，可免费自托管，无需信用卡。仓库自标 maturity = prototype（原型阶段），生产使用需自行评估稳定性。中继服务、模型推理与基础设施成本自付。 | [官网](https://github.com/block/buzz) / [GitHub](https://github.com/block/buzz) | 2026-08-03 | GitHub |
| 6 | CodexLoom | 前 Manus 团队成员 yan5xu 于 2026-08-02 开源的 Agent 团队编排工具，定位是「把 Codex 会话织成一个由长期在岗的领域 Agent 组成的组织」。Go 语言编写，刻意不重造执行 runtime，只在其上叠加 Agent 身份层与治理证据层；项目的 Owner 指南把产品原则、已验证实践与尚待验证的假设分开标注，强调可追溯性。与 WorkBench 相似度：中——提供多智能体编排、身份与治理能力，但依赖 OpenAI Codex 作为底层执行 runtime，并非独立的通用 Agent 平台。适用场景：已在使用 Codex 的研发团队做长周期多 Agent 分工、协作与责任追溯。项目处于早期阶段：建仓 2026-07-07，GitHub 194 stars / 14 forks。 | GitHub 公开仓库可免费克隆并自部署。许可证在 GitHub API 中标记为 Other / NOASSERTION，非标准 OSI 许可证，具体授权条款需查阅仓库 LICENSE 文件。运行依赖 OpenAI Codex 订阅或 API，模型成本自付。是否需要信用卡：unknown（取决于所用 Codex 计划）。 | [官网](https://github.com/yan5xu/codexloom) / [GitHub](https://github.com/yan5xu/codexloom) | 2026-08-02 | 社区 |
| 7 | Clark (Clark Agent / Clark Code) | Clark Labs 于 2026-07-18 在 Product Hunt 上线并拿下 Launch of the Day 的 AI coworker，形态分为两部分。云端 Clark Agent 运行在其自有虚拟电脑上，可操作浏览器、终端、文件与代码，用户关闭标签页后任务仍在后台继续；宣传支持资料研究、网站搭建、表格与演示文稿生成、审计与测试代码，能把工作拆给并行的专家子 agent，支持按计划定时运行，并交付带溯源证据链的产物，另提供 OpenAI 兼容 API 供嵌入其他系统。本地 Clark Code 则是安装在自己电脑上的 AI 编程 IDE（macOS，可经 SSH 指向远程机器），提供文件树、差异查看、审批门、内置终端与仓库级持久记忆，遇到陌生报错时可派云端 agent 去检索 GitHub issue / 论坛 / Stack Overflow / changelog 带回候选修复。与 WorkBench 相似度：高——通用任务执行 agent loop、浏览器与文件系统访问、定时任务、并行子智能体、产物交付。适用场景：网页调研、竞品资料整理、价格监控、报表与演示文稿生成、代码审计等长耗时异步任务。Web 端与 Android 已上线，iOS 未发布。风险提示：隐私政策（2026-07-13 更新）写明除非在账户设置中主动退出，用户的提示词、输出、访问过的网站、执行过的动作、运行过的代码及 agent 创建/修改的文件均可用于模型训练；Product Hunt 评价区目前仍为 No reviews yet，缺乏独立实测反馈。 | Clark Agent 提供免费入口，官方登录页标注免费使用、不需要信用卡，官方推广链接称新用户可得 500 credits（Product Hunt 页面另有 2,000 credits 的说法，两处数字不一致，以官网实际为准）。官方未公开统一价目表，付费计划名称为 Starter / Pro / Scale / Coder / BYOK / Team，Clark Code 官方在 X 上称计划 starting at $10；单次任务、浏览器动作与定时任务各消耗多少 credits 官方未说明。免费额度上限：unknown。 | [官网](https://www.clarkchat.com) | 2026-07-18 | ProductHunt |

## 详细信息

### 1. QM (Quartermaster)

- **功能描述**：Y Combinator 于 2026-07-31 开源的公司级多智能体 harness（官方定位 Multiplayer agent harness for work）。为每位员工和每个项目分配相互隔离的 AI 工作区，各自拥有独立的记忆、文件、钥匙串、权限、cron 定时任务、Web 应用与沙箱，避免一个人的 agent 上下文泄漏到同事那里；原生集成 Slack 与 Web UI；模型/harness 无关，可由 Pi、OpenCode、OpenAI Codex、Claude Code 驱动同一套核心基础设施；提供 Strict（每次工具调用需人工批准）/ Auto（默认，分类器筛查外部数据）/ Dangerous 三档安全策略，agent 以员工本人凭据运行以形成可追溯审计链。与 WorkBench 相似度：高——同为通用任务型 Agent 运行时，具备工具调用、定时任务、文件与权限管理、多模型接入、沙箱执行。适用场景：中小企业与团队级 AI 智能体的统一部署、权限治理与审计。GitHub 7,323 stars / 768 forks（截至 2026-08-03）。
- **免费使用方式**：MIT 许可证，完全开源、可自托管，软件本身零费用，无需信用卡。运行依赖自备 Postgres 实例（用于 session / memory / queue 持久化）与所选模型的 API 凭据，算力与模型调用成本自付。官方未提供付费托管版。
- **官网**：https://qm.ycombinator.com
- **GitHub**：https://github.com/yc-software/qm
- **文档**：-
- **最后更新日期**：2026-08-01
- **发现渠道**：GitHub

### 2. ego lite

- **功能描述**：citrolabs 开源的、专为 AI Agent 设计的 Chromium 浏览器，主张「同一浏览器，两个世界」：人类的日常标签页归人类，Agent 在隔离的 Space 中并行执行网页任务，互不抢占窗口。可迁移复用 Chrome 的书签、扩展、Cookie 与登录态，从而绕开 SSO / 2FA 反复登录问题；配套 ego-browser skill 把 snapshot / click / fill / navigate / wait / capture 暴露为 JavaScript 函数，Agent 可将多步网页任务写成一段 JS 一次执行，而非反复「调命令—看结果—再调命令」；Snapshot 语义快照集成进改造过的 Chromium 内核，能识别跨域 iframe、Shadow DOM 与第三方 SDK 组件，压缩进入模型上下文的数据量以降低 token 消耗。与 WorkBench 相似度：中——它不是完整的 Agent 编排平台，而是 Agent 的浏览器自动化执行底座，补齐「网页操作」这一关键能力。适用场景：资料调研、SaaS 后台操作、登录后页面读取、表单填写、无 API 网站取数、Vibe Coding 产物部署。2026-07-24 登上 GitHub Trending 日榜第一（当日 +884 star），截至 2026-08-03 已达 7,689 stars。
- **免费使用方式**：MIT 许可证开源，官方明确为免费产品、无需注册账号即可使用，本地优先，登录态 / Cookie / 书签留在设备本地不上传。当前原生支持 macOS（ARM64 / x64 .dmg 直接下载），Windows / Linux 处于 roadmap 阶段。需自备 AI Agent（Claude Code / Codex / Cursor 等）与相应模型凭据，模型成本自付。无需信用卡。已知限制：作为完整 Chromium 分支 + 多 Space 并行，内存占用偏高。
- **官网**：https://lite.ego.app
- **GitHub**：https://github.com/citrolabs/ego-lite
- **文档**：https://lite.ego.app/document/
- **最后更新日期**：2026-08-02
- **发现渠道**：GitHub

### 3. Kun

- **功能描述**：本地优先（local-first）的 AI Agent 工作台，桌面 GUI（Electron）与终端 TUI 共享同一套本地 agent runtime，线程上下文、模型连接、审批、用量与后台任务全部互通，关闭任一客户端不中断后台工作。桌面端提供 Code / Design / Write / Connect phone 四种模式：Design 可把需求文本直接生成 UI 稿、信息图与可交互 HTML 原型；Write 集成文件树、Markdown 编辑、预览与写作助手并可导出 HTML/PDF/DOC；Connect phone 让飞书/Lark、微信、Telegram、webhook 与定时任务各走独立后台 agent 线程。核心范式为「需求→设计→计划→编码→验收」的需求驱动软件生产；Agent Graph 由 Lead 将目标拆解为带依赖、预算与验收标准的有向任务图，调度器按就绪集分派子智能体，Supervisor 聚合提交/失败/冲突/预算/求助/恢复/完成信号并扫描停滞节点触发 Lead 复盘。与 WorkBench 相似度：高——本地运行时 + 多智能体编排 + 定时任务 + 本地文件访问 + MCP 支持 + 多模型路由。适用场景：个人与小团队的编码、写作、设计、自动化一体化工作台。GitHub 5,608 stars。
- **免费使用方式**：官网提供 macOS（ARM64/x64）、Windows x64、Linux（AppImage/deb）安装包免费下载，最新版 v0.2.34（2026-08-02），客户端本身不收费，官网未列出任何付费套餐。模型侧需自带订阅（ChatGPT/Codex、Claude Pro/Max、Gemini、Cursor、Grok）或 API Key（DeepSeek、小米 MiMo、MiniMax、Kimi、GLM、Qwen、OpenAI 兼容端点、自托管模型），登录、配额与可用模型遵循各模型提供方条款，模型成本自付。注意：GitHub 仓库许可证被标记为 Other / NOASSERTION，并非标准 OSI 许可证，商用与二次分发条款需自行查阅仓库 LICENSE 文件。是否需要信用卡：unknown。
- **官网**：https://www.kun-agent.com
- **GitHub**：https://github.com/KunAgent/Kun
- **文档**：-
- **最后更新日期**：2026-08-02
- **发现渠道**：GitHub

### 4. StaffDeck

- **功能描述**：OpenBMB（面壁智能开源社区）2026 年 7 月开源的企业级数字员工平台（Enterprise Digital Employee Platform）。业务人员用大白话描述一段流程（例如「差旅报销先收集事由金额行程，再核对是否超标，超标转财务负责人审批」），平台自动将其转译为精密的可执行 Agent 流程图；运行时支持流程中断—检索企业知识库—带出处返回—回到原表单继续填写的上下文管理，遇到制度未覆盖的盲区会把完整上下文打包转交人工，人工审批后的新规则可沉淀为长期记忆。内置能力包括完全私有化部署（除源码安装外提供各操作系统一键安装包）、按每日/每周/每月或一次性计划主动执行任务并推送结果、原生 MCP 协议 + HTTP API 打通 ERP / CRM / OA 系统。Preview 预览版附带财务报销、法务合规、人事服务、IT 支持、行政管家五个现成数字员工，各配完整 SOP 与知识库。与 WorkBench 相似度：高——自然语言构建流程、工具调用、定时任务、知识库与记忆系统、私有化部署。适用场景：央国企、金融等对数据合规要求严苛、需要数据不出域的企业内部智能体落地。GitHub 1,355 stars。
- **免费使用方式**：AGPL-3.0 许可证开源，可免费下载自部署，无需信用卡。需注意 AGPL-3.0 的传染性：基于其修改并对外提供网络服务时须同样开源，闭源商用存在许可证约束。模型推理与服务器成本自付。当前为 Preview 预览版，功能仍在迭代。
- **官网**：http://staffdeck.openbmb.cn/
- **GitHub**：https://github.com/OpenBMB/StaffDeck
- **文档**：-
- **最后更新日期**：2026-08-03
- **发现渠道**：社区

### 5. Buzz

- **功能描述**：Block（Jack Dorsey 旗下公司）开源的「蜂群思维」人机协同通信平台，基于 Nostr 协议、支持自托管。人类用户与 AI Agent 共享同一套频道、身份模型与审计日志，Agent 拥有独立密钥与身份，可打开代码仓库、发送补丁、审查代码、运行 YAML 工作流、编辑画布与管理频道；团队可围绕功能分支创建房间，把对话、补丁、CI 结果、评审与合并决策统一记录并可检索。目前中继服务、频道、画布、搜索、审计日志与 YAML 工作流已可用，工作流审批门禁与语音 Huddle 生命周期事件仍在接入中。与 WorkBench 相似度：中高——具备多智能体协作编排、工作流自动化、工具调用与审计追溯，但组织形态是团队通信频道而非单机工作台。适用场景：把 AI Agent 作为拥有独立身份与权限的团队成员纳入研发协作流程。GitHub 21,106 stars / 2,260 forks。注：仓库建于 2026-03-06，并非近 30 天新开源项目，本次因其登上 GitHub Trending 且此前未被本扫描收录而首次纳入。
- **免费使用方式**：Apache-2.0 许可证开源，可免费自托管，无需信用卡。仓库自标 maturity = prototype（原型阶段），生产使用需自行评估稳定性。中继服务、模型推理与基础设施成本自付。
- **官网**：https://github.com/block/buzz
- **GitHub**：https://github.com/block/buzz
- **文档**：-
- **最后更新日期**：2026-08-03
- **发现渠道**：GitHub

### 6. CodexLoom

- **功能描述**：前 Manus 团队成员 yan5xu 于 2026-08-02 开源的 Agent 团队编排工具，定位是「把 Codex 会话织成一个由长期在岗的领域 Agent 组成的组织」。Go 语言编写，刻意不重造执行 runtime，只在其上叠加 Agent 身份层与治理证据层；项目的 Owner 指南把产品原则、已验证实践与尚待验证的假设分开标注，强调可追溯性。与 WorkBench 相似度：中——提供多智能体编排、身份与治理能力，但依赖 OpenAI Codex 作为底层执行 runtime，并非独立的通用 Agent 平台。适用场景：已在使用 Codex 的研发团队做长周期多 Agent 分工、协作与责任追溯。项目处于早期阶段：建仓 2026-07-07，GitHub 194 stars / 14 forks。
- **免费使用方式**：GitHub 公开仓库可免费克隆并自部署。许可证在 GitHub API 中标记为 Other / NOASSERTION，非标准 OSI 许可证，具体授权条款需查阅仓库 LICENSE 文件。运行依赖 OpenAI Codex 订阅或 API，模型成本自付。是否需要信用卡：unknown（取决于所用 Codex 计划）。
- **官网**：https://github.com/yan5xu/codexloom
- **GitHub**：https://github.com/yan5xu/codexloom
- **文档**：-
- **最后更新日期**：2026-08-02
- **发现渠道**：社区

### 7. Clark (Clark Agent / Clark Code)

- **功能描述**：Clark Labs 于 2026-07-18 在 Product Hunt 上线并拿下 Launch of the Day 的 AI coworker，形态分为两部分。云端 Clark Agent 运行在其自有虚拟电脑上，可操作浏览器、终端、文件与代码，用户关闭标签页后任务仍在后台继续；宣传支持资料研究、网站搭建、表格与演示文稿生成、审计与测试代码，能把工作拆给并行的专家子 agent，支持按计划定时运行，并交付带溯源证据链的产物，另提供 OpenAI 兼容 API 供嵌入其他系统。本地 Clark Code 则是安装在自己电脑上的 AI 编程 IDE（macOS，可经 SSH 指向远程机器），提供文件树、差异查看、审批门、内置终端与仓库级持久记忆，遇到陌生报错时可派云端 agent 去检索 GitHub issue / 论坛 / Stack Overflow / changelog 带回候选修复。与 WorkBench 相似度：高——通用任务执行 agent loop、浏览器与文件系统访问、定时任务、并行子智能体、产物交付。适用场景：网页调研、竞品资料整理、价格监控、报表与演示文稿生成、代码审计等长耗时异步任务。Web 端与 Android 已上线，iOS 未发布。风险提示：隐私政策（2026-07-13 更新）写明除非在账户设置中主动退出，用户的提示词、输出、访问过的网站、执行过的动作、运行过的代码及 agent 创建/修改的文件均可用于模型训练；Product Hunt 评价区目前仍为 No reviews yet，缺乏独立实测反馈。
- **免费使用方式**：Clark Agent 提供免费入口，官方登录页标注免费使用、不需要信用卡，官方推广链接称新用户可得 500 credits（Product Hunt 页面另有 2,000 credits 的说法，两处数字不一致，以官网实际为准）。官方未公开统一价目表，付费计划名称为 Starter / Pro / Scale / Coder / BYOK / Team，Clark Code 官方在 X 上称计划 starting at $10；单次任务、浏览器动作与定时任务各消耗多少 credits 官方未说明。免费额度上限：unknown。
- **官网**：https://www.clarkchat.com
- **GitHub**：-
- **文档**：-
- **最后更新日期**：2026-07-18
- **发现渠道**：ProductHunt
