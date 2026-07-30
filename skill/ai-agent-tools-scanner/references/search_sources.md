# 搜索源清单与查询策略

## 搜索目标定义

寻找与 **WorkBench** 功能相似的产品：AI Agent 智能体构建平台/框架/低代码编排工具，具备如下一项或多项能力：
- 自然语言驱动的任务执行（agent loop）
- 工作流/多智能体编排（orchestration）
- 工具调用 / MCP / 插件生态
- 定时任务与自动化
- 本地文件/系统访问、浏览器自动化
- 知识库 / 记忆系统

**免费判定标准**（截止 search_date）：开源可自部署 / 有永久免费层 / 免费试用期内。需记录：免费额度、试用期限、限制条件、是否需要信用卡。

## 各渠道查询词模板（用 WebSearch 分渠道执行）

### 1. HuggingFace
- `site:huggingface.co AI agent builder platform <当年>`
- `HuggingFace Spaces agent framework free <当年>`

### 2. GitHub
- `github open source AI agent framework free <当月/当年> trending`
- `github low-code AI agent builder self-hosted`
- `site:github.com autonomous agent orchestration framework stars`
- 建议用 query_keyword_groups 一次覆盖多个变体

### 3. ProductHunt
- `site:producthunt.com AI agent builder <当月> <当年>`
- `ProductHunt launch AI agent platform free tier`

### 4. AI 工具导航站
- 国外：`Futurepedia OR "There's An AI For That" AI agent builder free`
- 国内：`AI工具集 OR Toolify 智能体搭建平台 免费`
- `AI agent 构建平台 免费 <当年> 新工具`

### 5. 开发者社区
- `reddit r/AI_Agents best free agent builder <当年>`
- `Hacker News AI agent framework Show HN <当年>`
- `掘金 OR 知乎 OR V2EX 智能体平台 免费 开源 <当年>`

## 已知同类工具基线（避免重复报告为"新发现"，但状态有更新时可收录）

Dify、Coze（扣子）、n8n、Flowise、Langflow、LangChain/LangGraph、AutoGen、CrewAI、AutoGPT、AgentGPT、SuperAGI、Zapier Agents、Make、腾讯元器、百度千帆 AgentBuilder、阿里百炼、字节 HiAgent、OpenAI Agents SDK / AgentKit、Anthropic Claude Agent SDK、Manus、Devin、Cursor/Windsurf（编码类 agent）。

收录判定优先级：
1. **新发布/新开源**（近 30 天）→ 必收录
2. 老牌工具有**重大免费政策变化或大版本更新** → 收录并注明
3. 基线内工具无变化 → 不收录

## 采集时的核实要求

- 至少通过 WebFetch 打开官网或 GitHub 页面确认：工具仍可访问、免费政策描述准确、最后更新日期（GitHub 看最近 commit/release；产品站看 changelog/blog）。
- 无法核实的字段填 `unknown`，不要编造。
- links 中官网必填，github/docs 找不到填 null。
