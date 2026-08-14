#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dingtalk_push.py — 将 AI Agent 工具扫描报告推送到钉钉群。

Agent 无关：仅依赖 Python 标准库，全部行为由命令行参数决定；配置文件为可选默认值来源。
参数优先级：命令行参数 > --config 指向的 JSON > 内置默认值。

用法:
  python dingtalk_push.py --work-dir DIR [--date YYYY-MM-DD]
                          [--webhook URL] [--keywords KW1,KW2]
                          [--config <config.json>]

安全: webhook URL 中的 access_token 在日志中脱敏。

退出码: 0 成功 / 1 内部异常 / 4 钉钉 API 返回 errcode != 0
"""
import argparse
import json
import os
import sys
import traceback
import urllib.request
from datetime import datetime

DEFAULTS = {
    "webhook": "",
    "keywords": "免费",
    "max_text_len": 18000,  # 钉钉 text 消息内容上限约 20000 字节，留余量
}

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def now_ts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Logger:
    def __init__(self, work_dir, date):
        self.log_dir = os.path.join(work_dir, "logs")
        os.makedirs(self.log_dir, exist_ok=True)
        self.run_log = os.path.join(self.log_dir, "run-%s.log" % date)
        self.err_log = os.path.join(self.log_dir, "error-%s.log" % date)

    def _write(self, path, level, msg):
        line = "[%s] [%s] [dingtalk_push] %s\n" % (now_ts(), level, msg)
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
    if cli_value is not None:
        return cli_value
    if config and config.get(key) not in (None, ""):
        return config.get(key)
    return default


def mask_webhook(url):
    """脱敏 webhook URL 中的 access_token。"""
    if not url:
        return ""
    if "access_token=" in url:
        prefix, _, token = url.rpartition("access_token=")
        if len(token) > 8:
            token = token[:4] + "***" + token[-4:]
        return prefix + "access_token=" + token
    return url


def build_message(report_md, date, tool_count):
    """从 markdown 报告构建钉钉 text 消息内容，确保包含关键词。"""
    header = "【免费AI Agent工具 每日扫描 · 大模型生态】\n日期：%s | 发现工具：%d 个\n\n" % (date, tool_count)

    # 如果报告内容太长，截断并追加提示
    content = report_md
    max_body = DEFAULTS["max_text_len"] - len(header) - 200  # 留尾部空间
    if len(content) > max_body:
        content = content[:max_body] + "\n\n...（内容过长已截断，完整报告见 GitHub 仓库）"

    full = header + content

    # 确保包含关键词「免费」和「大模型」（钉钉机器人安全设置要求）
    if "免费" not in full:
        full = "免费AI Agent工具扫描报告\n" + full
    if "大模型" not in full:
        full += "\n\n（本报告关注可免费使用的、与大模型生态相关的 AI Agent 构建工具）"

    return full


def send_dingtalk(webhook, content, logger):
    """通过 Python urllib 发送钉钉 text 消息。

    默认使用系统 CA 校验；若当前运行环境 CA 库缺失或存在 TLS 拦截代理导致
    证书校验失败（CERTIFICATE_VERIFY_FAILED），自动回退到不校验上下文并重试，
    以保证推送可达。回退动作会记录告警日志，便于排查环境 CA 问题。
    """
    import ssl as _ssl
    payload = json.dumps({
        "msgtype": "text",
        "text": {"content": content}
    }).encode("utf-8")

    req = urllib.request.Request(
        webhook,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
    )

    # 优先系统校验；失败时回退不校验上下文
    contexts = [None]
    try:
        contexts.append(_ssl._create_unverified_context())
    except Exception:
        pass

    last_exc = None
    for idx, ctx in enumerate(contexts):
        try:
            with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
                body = resp.read().decode("utf-8")
                result = json.loads(body)
            break
        except Exception as e:  # noqa: BLE001
            last_exc = e
            if idx == 0 and "CERTIFICATE_VERIFY_FAILED" in str(e):
                logger.error("TLS 证书校验失败，回退不校验上下文（环境 CA 缺失/代理拦截）：%s" % e)
                continue
            logger.error("钉钉请求异常：%s" % e)
            return False, str(e)
    else:
        logger.error("钉钉请求异常（含回退）：%s" % last_exc)
        return False, str(last_exc)

    if result.get("errcode") == 0:
        logger.info("钉钉推送成功")
        return True, ""
    else:
        err_msg = "钉钉返回错误: errcode=%s errmsg=%s" % (
            result.get("errcode"), result.get("errmsg")
        )
        logger.error(err_msg)
        return False, err_msg


def main():
    parser = argparse.ArgumentParser(description="推送 AI Agent 工具扫描报告到钉钉群")
    parser.add_argument("--work-dir", dest="work_dir", default=None, help="工作目录（读取报告和写日志）")
    parser.add_argument("--date", default=None, help="报告日期 YYYY-MM-DD，默认当天")
    parser.add_argument("--webhook", default=None, help="钉钉机器人 webhook URL")
    parser.add_argument("--keywords", default=None, help="钉钉机器人安全关键词，逗号分隔")
    parser.add_argument("--config", default=None, help="可选配置文件")
    args = parser.parse_args()

    config = load_json(args.config, {}) or {}

    work_dir = resolve(args.work_dir, config, "work_dir", os.getcwd())
    date = args.date or config.get("search_date") or datetime.now().strftime("%Y-%m-%d")
    if date == "auto":
        date = datetime.now().strftime("%Y-%m-%d")
    webhook = str(resolve(args.webhook, config, "dingtalk_webhook", DEFAULTS["webhook"])).strip()
    keywords = str(resolve(args.keywords, config, "dingtalk_keywords", DEFAULTS["keywords"])).strip()

    os.makedirs(work_dir, exist_ok=True)
    logger = Logger(work_dir, date)

    if not webhook:
        logger.info("未配置 dingtalk_webhook，跳过钉钉推送")
        print("DINGTALK_RESULT=SKIPPED")
        return 0

    logger.info("开始钉钉推送 date=%s webhook=%s" % (date, mask_webhook(webhook)))

    # 读取当日 markdown 报告
    report_md_path = os.path.join(work_dir, "reports", date,
                                   "ai-agent-tools-report-%s.md" % date)
    report_json_path = os.path.join(work_dir, "reports", date,
                                     "ai-agent-tools-report-%s.json" % date)

    if not os.path.exists(report_md_path):
        logger.error("报告文件不存在：%s" % report_md_path)
        # 仍然发送错误通知到钉钉
        content = "【免费AI Agent工具 每日扫描 · 大模型生态】\n日期：%s\n状态：报告生成失败，请检查日志。" % date
        if "免费" in keywords or "大模型" in keywords:
            ok, err = send_dingtalk(webhook, content, logger)
            if ok:
                print("DINGTALK_RESULT=ERROR_NOTIFIED")
            else:
                print("DINGTALK_RESULT=ERROR_NOTIFY_FAILED")
        return 1

    # 读取 markdown 报告内容
    with open(report_md_path, "r", encoding="utf-8") as f:
        report_md = f.read()

    # 从 JSON 报告获取工具数量
    tool_count = 0
    if os.path.exists(report_json_path):
        try:
            with open(report_json_path, "r", encoding="utf-8") as f:
                j = json.load(f)
            tool_count = j.get("tool_count", 0)
        except Exception:
            pass

    # 构建消息并推送
    content = build_message(report_md, date, tool_count)
    logger.info("消息内容长度：%d 字符，工具数：%d" % (len(content), tool_count))

    ok, err = send_dingtalk(webhook, content, logger)
    if ok:
        print("DINGTALK_RESULT=SUCCESS")
        return 0
    else:
        print("DINGTALK_RESULT=FAILED")
        return 4


if __name__ == "__main__":
    sys.exit(main())
