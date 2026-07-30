# AI Agent Tools Daily Scan

每日自动扫描**可免费使用**的、与 **WorkBench** 功能相似的 AI Agent 智能体构建平台/工具，生成结构化报告并按日期归档。

由 [`ai-agent-tools-scanner`](skill/ai-agent-tools-scanner/) skill 驱动 —— 该 skill 为 **agent 无关**设计，任意 agent 或纯 cron 脚本均可集成调用。

## 仓库结构

```
├── reports/
│   └── YYYY-MM-DD/
│       ├── ai-agent-tools-report-YYYY-MM-DD.md     # Markdown 主报告
│       └── ai-agent-tools-report-YYYY-MM-DD.json   # 机器可读报告
├── skill/
│   └── ai-agent-tools-scanner/                     # skill 源码（自动同步）
│       ├── SKILL.md
│       ├── config.example.json
│       ├── scripts/
│       ├── references/
│       └── assets/
└── logs/                                           # 运行日志（默认不入库）
```

## 扫描范围

| 渠道 | 说明 |
|---|---|
| HuggingFace | Spaces / 官方博客中的 agent 构建工具 |
| GitHub | 开源 AI Agent 框架与低代码 Agent 平台 |
| ProductHunt | 近期发布的 AI Agent builder 产品 |
| AI 工具导航站 | Toolify、AI工具集、Futurepedia、There's An AI For That 等 |
| 开发者社区 | Reddit r/AI_Agents、Hacker News、V2EX、掘金、知乎 |

## 收录标准

工具需**同时满足**：

1. **功能相似** — 具备 AI Agent 构建 / 编排 / 自动化工作流能力
2. **免费可用** — 截止搜索日期有永久免费层、可用免费额度、有效试用期，或开源可自部署
3. **非重复** — 不在已知基线清单内（基线内工具仅在免费政策重大变化或大版本更新时收录）

每条记录包含：工具名称、功能描述（含与 WorkBench 相似度）、免费使用方式（额度/期限/限制/是否需信用卡）、访问链接、最后更新日期、发现渠道。

## 报告数据格式

```json
{
  "report_date": "YYYY-MM-DD",
  "generated_at": "YYYY-MM-DD HH:MM:SS",
  "tool_count": 0,
  "no_new_tools": true,
  "note": "当日未发现新工具",
  "tools": [
    {
      "name": "工具名称",
      "description": "核心能力 + 与 WorkBench 相似度 + 适用场景",
      "free_usage": "免费额度 / 试用期限 / 限制条件 / 是否需要信用卡",
      "links": { "website": "https://...", "github": null, "docs": null },
      "last_updated": "YYYY-MM-DD",
      "source_channel": "GitHub"
    }
  ]
}
```

## 自行部署

```bash
# 1. 复制配置模板并填写
cp skill/ai-agent-tools-scanner/config.example.json config.json

# 2. 生成报告（collected.json 由 agent 检索后产出）
python skill/ai-agent-tools-scanner/scripts/generate_report.py \
  --input collected-$(date +%F).json --work-dir . --date $(date +%F)

# 3. 推送到自己的仓库
export GITHUB_TOKEN=<your_pat>
python skill/ai-agent-tools-scanner/scripts/git_push.py \
  --work-dir . --date $(date +%F) \
  --repo-url https://github.com/<you>/<repo> --branch main
```

依赖：Python ≥ 3.8（仅标准库）+ git。集成到不同 agent 的方式见 [`references/integration_examples.md`](skill/ai-agent-tools-scanner/references/integration_examples.md)。

## 免责声明

报告内容由自动化检索生成，免费政策变动频繁，**请以各工具官方最新说明为准**。

## License

[MIT](LICENSE)
