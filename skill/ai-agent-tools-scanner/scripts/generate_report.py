#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_report.py — 将采集到的 AI Agent 工具数据生成 Markdown + JSON 报告并按日期归档。

Agent 无关：仅依赖 Python 标准库，全部行为由命令行参数决定；配置文件为可选的默认值来源。
参数优先级：命令行参数 > --config 指向的 JSON > 内置默认值。

用法:
  python generate_report.py --input <collected.json> [--work-dir DIR] [--date YYYY-MM-DD]
                            [--output-format markdown|json|both] [--config <config.json>]

退出码: 0 成功（含空结果） / 1 内部异常
"""
import argparse
import json
import os
import sys
import traceback
from datetime import datetime

DEFAULTS = {
    "work_dir": os.getcwd(),
    "output_format": "both",
}

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def now_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Logger:
    """运行日志 + 错误日志双写。"""

    def __init__(self, work_dir, date):
        self.log_dir = os.path.join(work_dir, "logs")
        os.makedirs(self.log_dir, exist_ok=True)
        self.run_log = os.path.join(self.log_dir, "run-%s.log" % date)
        self.err_log = os.path.join(self.log_dir, "error-%s.log" % date)

    def _write(self, path, level, msg):
        line = "[%s] [%s] [generate_report] %s\n" % (now_ts(), level, msg)
        try:
            with open(path, "a", encoding="utf-8") as f:
                f.write(line)
        except Exception:
            pass
        print(line.rstrip())

    def info(self, msg):
        self._write(self.run_log, "INFO", msg)

    def error(self, msg):
        self._write(self.run_log, "ERROR", msg)
        self._write(self.err_log, "ERROR", msg)


def load_json(path, default=None):
    if not path or not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def resolve(cli_value, config, key, default):
    """参数优先级：CLI > config > default。"""
    if cli_value is not None:
        return cli_value
    if config and config.get(key) not in (None, ""):
        return config.get(key)
    return default


def md_escape(s):
    if s is None:
        return "-"
    return str(s).replace("|", "\\|").replace("\n", "<br>")


def build_markdown(tools, date):
    lines = [
        "# 每日 AI Agent 工具扫描报告 - %s" % date,
        "",
        "> 搜索截止日期：%s ｜ 生成时间：%s ｜ 发现工具数：%d" % (date, now_ts(), len(tools)),
        "",
    ]

    if not tools:
        lines += [
            "**当日未发现新工具。**",
            "",
            "搜索范围已覆盖 HuggingFace、GitHub、ProductHunt、国内外 AI 工具导航站及开发者社区，"
            "未发现符合条件（与 WorkBench 功能相似且可免费使用）的新工具。",
            "",
        ]
        return "\n".join(lines)

    lines += [
        "## 汇总",
        "",
        "| # | 工具名称 | 功能描述 | 免费使用方式 | 访问链接 | 最后更新 | 发现渠道 |",
        "|---|---------|---------|-------------|---------|---------|---------|",
    ]
    for i, t in enumerate(tools, 1):
        links = t.get("links") or {}
        parts = []
        if links.get("website"):
            parts.append("[官网](%s)" % links["website"])
        if links.get("github"):
            parts.append("[GitHub](%s)" % links["github"])
        if links.get("docs"):
            parts.append("[文档](%s)" % links["docs"])
        lines.append("| %d | %s | %s | %s | %s | %s | %s |" % (
            i,
            md_escape(t.get("name", "-")),
            md_escape(t.get("description", "-")),
            md_escape(t.get("free_usage", "-")),
            " / ".join(parts) if parts else "-",
            md_escape(t.get("last_updated", "unknown")),
            md_escape(t.get("source_channel", "-")),
        ))

    lines += ["", "## 详细信息", ""]
    for i, t in enumerate(tools, 1):
        links = t.get("links") or {}
        lines += [
            "### %d. %s" % (i, t.get("name", "未知工具")),
            "",
            "- **功能描述**：%s" % (t.get("description") or "-"),
            "- **免费使用方式**：%s" % (t.get("free_usage") or "-"),
            "- **官网**：%s" % (links.get("website") or "-"),
            "- **GitHub**：%s" % (links.get("github") or "-"),
            "- **文档**：%s" % (links.get("docs") or "-"),
            "- **最后更新日期**：%s" % (t.get("last_updated") or "unknown"),
            "- **发现渠道**：%s" % (t.get("source_channel") or "-"),
            "",
        ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="生成 AI Agent 工具扫描报告")
    parser.add_argument("--input", required=True, help="采集数据 JSON 文件路径")
    parser.add_argument("--work-dir", dest="work_dir", default=None, help="输出根目录")
    parser.add_argument("--date", default=None, help="报告日期 YYYY-MM-DD，默认当天")
    parser.add_argument("--output-format", dest="output_format", default=None,
                        choices=["markdown", "json", "both"], help="输出格式")
    parser.add_argument("--config", default=None, help="可选配置文件，提供默认值")
    args = parser.parse_args()

    config = load_json(args.config, {}) or {}
    work_dir = resolve(args.work_dir, config, "work_dir", DEFAULTS["work_dir"])
    date = args.date or config.get("search_date") or datetime.now().strftime("%Y-%m-%d")
    if date == "auto":
        date = datetime.now().strftime("%Y-%m-%d")
    output_format = str(resolve(args.output_format, config, "output_format",
                                DEFAULTS["output_format"])).lower()

    os.makedirs(work_dir, exist_ok=True)
    logger = Logger(work_dir, date)

    try:
        logger.info("开始生成报告 date=%s work_dir=%s format=%s" % (date, work_dir, output_format))

        tools = load_json(args.input, default=None)
        if tools is None:
            logger.error("采集文件不存在：%s，按空结果处理" % args.input)
            tools = []
        elif not isinstance(tools, list):
            logger.error("采集文件格式异常（顶层非数组），按空结果处理")
            tools = []
        logger.info("采集到工具数量：%d" % len(tools))

        report_dir = os.path.join(work_dir, "reports", date)
        os.makedirs(report_dir, exist_ok=True)

        written = []
        if output_format in ("markdown", "both"):
            md_path = os.path.join(report_dir, "ai-agent-tools-report-%s.md" % date)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(build_markdown(tools, date))
            written.append(md_path)
            logger.info("Markdown 报告已生成：%s" % md_path)

        if output_format in ("json", "both"):
            json_path = os.path.join(report_dir, "ai-agent-tools-report-%s.json" % date)
            payload = {
                "report_date": date,
                "generated_at": now_ts(),
                "tool_count": len(tools),
                "no_new_tools": len(tools) == 0,
                "note": "当日未发现新工具" if not tools else "",
                "tools": tools,
            }
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
            written.append(json_path)
            logger.info("JSON 报告已生成：%s" % json_path)

        logger.info("报告生成完成，共 %d 个文件" % len(written))
        print("REPORT_FILES=" + ";".join(written))
        print("TOOL_COUNT=%d" % len(tools))
        return 0
    except Exception:
        logger.error("报告生成失败：\n" + traceback.format_exc())
        return 1


if __name__ == "__main__":
    sys.exit(main())
