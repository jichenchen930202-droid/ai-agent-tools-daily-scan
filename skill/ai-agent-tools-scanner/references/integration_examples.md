# 集成示例：不同调用方如何绑定本 Skill

本 skill 为 agent 无关设计，只需调用方提供 `web_search` / `web_fetch` / `shell` 三类能力与显式参数。
以下为常见调用方的 `tool_binding` 填法与调度接法。

---

## 1. 通用 Agent（含 WorkBuddy / Claude / Cursor 等具备联网与命令执行能力的 agent）

```
## tool_binding
web_search: <该 agent 的联网搜索工具>
web_fetch:  <该 agent 的网页抓取工具>
shell:      <该 agent 的命令执行工具>
python:     python3        # Windows 环境常为 python
```

调度：使用该 agent 平台自带的定时任务能力，创建每日任务，prompt 中要求按 `SKILL.md` 的执行步骤走完 Step 1–7。
调度参数换算见 SKILL.md「调度集成」章节的 cron / RRULE 对照表。

> 若 agent 运行在隔离的 Python 运行时中，`python` 需绑定为该运行时的解释器绝对路径。

---

## 2. LangChain / LangGraph

```python
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.tools.requests.tool import RequestsGetTool
from langchain_experimental.tools import PythonREPLTool

# tool_binding
# web_search -> DuckDuckGoSearchResults()
# web_fetch  -> RequestsGetTool()
# shell      -> subprocess / ShellTool
```

采集完成后由 agent 写出 `collected-<date>.json`，再以 `subprocess.run` 调用两个脚本：

```python
import subprocess, datetime, pathlib

date = datetime.date.today().isoformat()
work_dir = pathlib.Path("./scan-data")
skill = pathlib.Path("./skills/ai-agent-tools-scanner")

subprocess.run([
    "python", str(skill / "scripts/generate_report.py"),
    "--input", str(work_dir / f"collected-{date}.json"),
    "--work-dir", str(work_dir), "--date", date, "--output-format", "both",
], check=True)

subprocess.run([
    "python", str(skill / "scripts/git_push.py"),
    "--work-dir", str(work_dir), "--date", date,
    "--repo-url", "https://github.com/<owner>/<repo>", "--branch", "main",
], check=False)   # 推送失败不阻断主流程
```

---

## 3. 纯脚本 / crontab（无 agent，人工或外部服务提供检索结果）

前提：由外部流程产出 `collected-<date>.json`。

```bash
# crontab -e   每日 09:00
0 9 * * * cd /opt/ai-scan && /usr/bin/env bash run_scan.sh >> /var/log/ai-scan.log 2>&1
```

`run_scan.sh`：

```bash
#!/usr/bin/env bash
set -uo pipefail          # 注意：不用 -e，保证单步失败不中断整链
DATE=$(date +%F)
WORK_DIR=/opt/ai-scan/data
SKILL=/opt/ai-scan/skills/ai-agent-tools-scanner
export GITHUB_TOKEN=$(cat /etc/ai-scan/token)   # 权限 600

python3 "$SKILL/scripts/generate_report.py" \
  --input "$WORK_DIR/collected-$DATE.json" \
  --work-dir "$WORK_DIR" --date "$DATE" --output-format both

python3 "$SKILL/scripts/git_push.py" \
  --work-dir "$WORK_DIR" --date "$DATE" \
  --repo-url https://github.com/<owner>/<repo> --branch main
```

---

## 4. systemd timer

`/etc/systemd/system/ai-agent-scan.service`：

```ini
[Unit]
Description=AI Agent Tools Daily Scan

[Service]
Type=oneshot
WorkingDirectory=/opt/ai-scan
EnvironmentFile=/etc/ai-scan/env        # 内含 GITHUB_TOKEN=...
ExecStart=/usr/bin/env bash run_scan.sh
```

`/etc/systemd/system/ai-agent-scan.timer`：

```ini
[Unit]
Description=Run AI Agent Tools Scan daily at 09:00

[Timer]
OnCalendar=*-*-* 09:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

启用：`systemctl enable --now ai-agent-scan.timer`

---

## 5. GitHub Actions（在仓库内自托管调度）

`.github/workflows/daily-scan.yml`：

```yaml
name: Daily AI Agent Tools Scan
on:
  schedule:
    - cron: '0 1 * * *'      # UTC 01:00 = 北京时间 09:00
  workflow_dispatch:

permissions:
  contents: write            # 允许工作流回写仓库

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }

      # 由外部 agent/API 产出 collected-<date>.json 的步骤置于此处

      - name: Generate report
        run: |
          DATE=$(date +%F)
          python skill/ai-agent-tools-scanner/scripts/generate_report.py \
            --input "collected-$DATE.json" --work-dir . --date "$DATE"

      - name: Commit report
        run: |
          DATE=$(date +%F)
          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git diff --staged --quiet || git commit -m "[Auto] 每日AI Agent工具扫描报告 - $DATE"
          git push
```

> 使用 Actions 内置 `GITHUB_TOKEN` 时无需 `git_push.py`，直接用工作流自带凭据提交即可。

---

## 认证方式对照

| 方式 | 配置 | 适用 |
|---|---|---|
| **Fine-grained PAT**（推荐） | 仅授予目标仓库 `Contents: Read and write`，写入环境变量 `GITHUB_TOKEN` | 权限最小化，可设过期时间 |
| Classic PAT | 勾选 `repo` scope，写入环境变量 | 权限过宽，不推荐 |
| SSH | `--auth-method ssh` + 仓库地址用 `git@github.com:owner/repo.git`，本机配好 `~/.ssh/id_ed25519` | 免轮换、长期有效 |
| Actions 内置 token | `permissions: contents: write` | 仅限 GitHub Actions 环境 |

**安全约束**：PAT 只经环境变量传递，禁止写入 `config.json` 或提交到仓库；脚本已在所有日志与命令回显中将其脱敏为 `***TOKEN***`。

生成 SSH 密钥（若选择 ssh 方式）：

```bash
ssh-keygen -t ed25519 -C "ai-agent-tools-scanner" -f ~/.ssh/id_ed25519 -N ""
cat ~/.ssh/id_ed25519.pub    # 添加到 GitHub → Settings → SSH and GPG keys
ssh -T git@github.com        # 验证
```
