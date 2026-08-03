#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
git_push.py — 将 skill 自身代码 + 每日报告提交并推送到指定 Git 仓库。

Agent 无关：仅依赖 Python 标准库 + git CLI，全部行为由命令行参数决定；配置文件为可选默认值来源。
参数优先级：命令行参数 > --config 指向的 JSON > 内置默认值。

用法:
  python git_push.py [--work-dir DIR] [--date YYYY-MM-DD] [--repo-url URL] [--branch NAME]
                     [--auth-method token|ssh] [--token-env NAME] [--skill-dir DIR]
                     [--retries N] [--retry-interval SEC] [--config <config.json>]

安全: PAT 仅从环境变量读取，且在所有日志/回显中脱敏为 ***TOKEN***。

退出码: 0 成功或跳过 / 1 内部异常 / 2 认证缺失 / 3 重试耗尽仍失败
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import traceback
from datetime import datetime

DEFAULTS = {
    "branch": "main",
    "auth_method": "token",
    "token_env": "GITHUB_TOKEN",
    "retries": 3,
    "retry_interval": 30,
    "commit_prefix": "[Auto] 每日AI Agent工具扫描报告",
}

# 单条 git 命令的最长执行时间（秒），防止无人值守时无限挂起
GIT_TIMEOUT = 180

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
        line = "[%s] [%s] [git_push] %s\n" % (now_ts(), level, msg)
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


def non_interactive_env():
    """构造禁止一切交互式凭据提示的环境。

    无人值守场景下，git 在缺少凭据时会弹出终端/GUI 提示并永久挂起，
    必须显式关闭，让其立即失败以触发重试与错误日志。
    """
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"      # 禁止终端询问用户名/密码
    env["GCM_INTERACTIVE"] = "never"      # 禁止 Git Credential Manager 弹窗
    env["GIT_ASKPASS"] = ""               # 禁用 askpass 助手
    env["SSH_ASKPASS"] = ""
    # 彻底禁用凭据助手，避免 GCM 用错误/过期的缓存凭据覆盖 URL 内嵌的 token
    env["GIT_CONFIG_COUNT"] = "1"
    env["GIT_CONFIG_KEY_0"] = "credential.helper"
    env["GIT_CONFIG_VALUE_0"] = ""
    env.setdefault(
        "GIT_SSH_COMMAND",
        "ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=15",
    )
    return env


def mask(text, secret):
    if secret and text:
        return str(text).replace(secret, "***TOKEN***")
    return text


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


_GIT_EXE_CACHE = []


def resolve_git_exe(logger=None):
    """定位 git 可执行文件。

    PATH 中找不到 git 时（常见于便携版 Git 被重命名/未注册 PATH 的 Windows 环境），
    回退扫描常见安装位置，避免直接抛 FileNotFoundError 导致整个推送失败。
    """
    if _GIT_EXE_CACHE:
        return _GIT_EXE_CACHE[0]

    found = shutil.which("git")
    if not found:
        import glob as _glob
        home = os.path.expanduser("~")
        candidates = []
        # 便携版 Git（含升级过程中遗留的 *.old.* 目录）
        for pattern in (
            os.path.join(home, ".workbuddy", "vendor", "PortableGit*", "cmd", "git.exe"),
            os.path.join(home, ".workbuddy", "vendor", "PortableGit*", "bin", "git.exe"),
            os.path.join(home, "AppData", "Local", "Programs", "Git", "cmd", "git.exe"),
        ):
            candidates.extend(sorted(_glob.glob(pattern)))
        candidates.extend([
            r"C:\Program Files\Git\cmd\git.exe",
            r"C:\Program Files (x86)\Git\cmd\git.exe",
            "/usr/bin/git", "/usr/local/bin/git", "/opt/homebrew/bin/git",
        ])
        for c in candidates:
            if os.path.exists(c):
                found = c
                if logger:
                    logger.info("PATH 中未找到 git，回退使用：%s" % c)
                break

    if not found:
        raise RuntimeError("未找到 git 可执行文件，请安装 git 或将其加入 PATH")
    _GIT_EXE_CACHE.append(found)
    return found


def run_git(args_list, cwd, logger, secret=None, check=True, timeout=GIT_TIMEOUT):
    cmd_str = mask("git " + " ".join(args_list), secret)
    logger.info("执行: %s (cwd=%s)" % (cmd_str, cwd))
    git_exe = resolve_git_exe(logger)
    try:
        result = subprocess.run(
            [git_exe] + args_list, cwd=cwd, capture_output=True, text=True,
            encoding="utf-8", errors="replace",
            env=non_interactive_env(), stdin=subprocess.DEVNULL, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        msg = "git 命令超时（%ds）: %s" % (timeout, cmd_str)
        logger.error(msg)
        if check:
            raise RuntimeError(msg)
        return subprocess.CompletedProcess(args_list, 124, "", msg)
    out = (result.stdout or "").strip()
    err = (result.stderr or "").strip()
    if out:
        logger.info("stdout: " + mask(out, secret))
    if err:
        logger.info("stderr: " + mask(err, secret))
    if check and result.returncode != 0:
        raise RuntimeError("git 命令失败 (%s): %s" % (cmd_str, mask(err or out, secret)))
    return result


def read_token(token_file, token_env, logger):
    """优先从文件读取 PAT（确定性、不依赖进程环境），否则回退到环境变量。"""
    if token_file:
        try:
            with open(token_file, "r", encoding="utf-8") as f:
                tok = f.read().strip()
            if tok:
                logger.info("已从文件读取凭据：%s" % token_file)
                return tok
            logger.info("凭据文件为空：%s，回退到环境变量 %s" % (token_file, token_env))
        except Exception as e:
            logger.info("读取凭据文件失败（%s）：%s，回退到环境变量" % (token_file, e))
    return os.environ.get(token_env, "").strip()


def build_auth_url(repo_url, auth_method, token):
    """token 模式下把 PAT 注入 https URL；ssh 模式原样返回。"""
    if auth_method == "token" and token and repo_url.startswith("https://"):
        return repo_url.replace("https://", "https://%s@" % token, 1)
    return repo_url

def seed_repo_template(work_dir, skill_dir, logger):
    """从 assets/repo_template/ 补齐仓库骨架文件（已存在则不覆盖）。"""
    template_dir = os.path.join(skill_dir, "assets", "repo_template")
    if not os.path.isdir(template_dir):
        return
    for name in os.listdir(template_dir):
        src = os.path.join(template_dir, name)
        dst = os.path.join(work_dir, name)
        if os.path.exists(dst):
            continue
        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
        logger.info("已补齐仓库骨架文件：%s" % name)


def sync_skill_code(work_dir, skill_dir, logger):
    """复制 skill 自身代码到仓库 skill/<skill-name>/。"""
    dest = os.path.join(work_dir, "skill", os.path.basename(skill_dir))
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(
        skill_dir, dest,
        ignore=shutil.ignore_patterns(
            "__pycache__", "*.pyc", ".git", "_skillhub_meta.json", "_knot_meta.json", "config.json"
        ),
    )
    logger.info("skill 代码已同步到：%s" % dest)


def ensure_repo(work_dir, auth_url, branch, logger, secret):
    """确保 work_dir 是绑定了 origin 的 git 仓库。"""
    if os.path.exists(os.path.join(work_dir, ".git")):
        r = run_git(["remote", "get-url", "origin"], work_dir, logger, secret, check=False)
        if r.returncode != 0:
            run_git(["remote", "add", "origin", auth_url], work_dir, logger, secret)
        else:
            run_git(["remote", "set-url", "origin", auth_url], work_dir, logger, secret)
        return

    tmp_clone = work_dir.rstrip("/\\") + "_clone_tmp"
    if os.path.exists(tmp_clone):
        shutil.rmtree(tmp_clone, ignore_errors=True)

    try:
        r = subprocess.run(
            ["git", "clone", "--branch", branch, "--single-branch", auth_url, tmp_clone],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            env=non_interactive_env(), stdin=subprocess.DEVNULL, timeout=GIT_TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        logger.error("git clone 超时（%ds），回退本地初始化" % GIT_TIMEOUT)
        r = subprocess.CompletedProcess([], 124, "", "clone timeout")

    if r.returncode == 0:
        for name in os.listdir(tmp_clone):
            src = os.path.join(tmp_clone, name)
            dst = os.path.join(work_dir, name)
            if name == ".git" or not os.path.exists(dst):
                if os.path.exists(dst):
                    shutil.rmtree(dst, ignore_errors=True)
                shutil.move(src, dst)
        shutil.rmtree(tmp_clone, ignore_errors=True)
        logger.info("已 clone 远端仓库并合并到工作目录")
    else:
        logger.info("clone 失败（可能是空仓库或分支不存在），回退 git init: %s"
                    % mask((r.stderr or "").strip(), secret))
        shutil.rmtree(tmp_clone, ignore_errors=True)
        run_git(["init", "-b", branch], work_dir, logger, secret, check=False)
        if not os.path.exists(os.path.join(work_dir, ".git")):
            run_git(["init"], work_dir, logger, secret)
            run_git(["checkout", "-b", branch], work_dir, logger, secret, check=False)
        run_git(["remote", "add", "origin", auth_url], work_dir, logger, secret, check=False)
        run_git(["remote", "set-url", "origin", auth_url], work_dir, logger, secret, check=False)


def main():
    parser = argparse.ArgumentParser(description="推送 AI Agent 工具扫描报告到 Git 仓库")
    parser.add_argument("--work-dir", dest="work_dir", default=None)
    parser.add_argument("--date", default=None)
    parser.add_argument("--repo-url", dest="repo_url", default=None)
    parser.add_argument("--branch", default=None)
    parser.add_argument("--auth-method", dest="auth_method", default=None, choices=["token", "ssh"])
    parser.add_argument("--token-env", dest="token_env", default=None)
    parser.add_argument("--token-file", dest="token_file", default=None,
                        help="从文件读取 PAT（优先级高于 --token-env），文件应置于 git 仓库之外")
    parser.add_argument("--skill-dir", dest="skill_dir", default=None, help="skill 根目录，默认脚本上级目录")
    parser.add_argument("--retries", type=int, default=None)
    parser.add_argument("--retry-interval", dest="retry_interval", type=int, default=None)
    parser.add_argument("--config", default=None)
    args = parser.parse_args()

    config = load_json(args.config, {}) or {}

    work_dir = resolve(args.work_dir, config, "work_dir", os.getcwd())
    date = args.date or config.get("search_date") or datetime.now().strftime("%Y-%m-%d")
    if date == "auto":
        date = datetime.now().strftime("%Y-%m-%d")
    repo_url = str(resolve(args.repo_url, config, "github_repo_url", "") or "").strip()
    branch = str(resolve(args.branch, config, "github_branch", DEFAULTS["branch"])).strip()
    auth_method = str(resolve(args.auth_method, config, "github_auth_method",
                              DEFAULTS["auth_method"])).strip().lower()
    token_env = str(resolve(args.token_env, config, "github_token_env", DEFAULTS["token_env"])).strip()
    token_file = str(resolve(args.token_file, config, "github_token_file", "") or "").strip()
    skill_dir = resolve(args.skill_dir, config, "skill_dir", SKILL_DIR)
    retries = int(resolve(args.retries, config, "push_retries", DEFAULTS["retries"]))
    retry_interval = int(resolve(args.retry_interval, config, "push_retry_interval",
                                 DEFAULTS["retry_interval"]))

    os.makedirs(work_dir, exist_ok=True)
    logger = Logger(work_dir, date)

    token = read_token(token_file, token_env, logger)

    if not repo_url:
        logger.info("repo_url 未配置，跳过推送（报告保留在本地 %s）" % work_dir)
        print("PUSH_RESULT=SKIPPED")
        return 0

    if auth_method == "token" and repo_url.startswith("https://") and not token:
        logger.error("认证方式为 token，但既未配置 token 文件也未设置环境变量 %s，无法推送" % token_env)
        print("PUSH_RESULT=NO_TOKEN")
        return 2

    try:
        auth_url = build_auth_url(repo_url, auth_method, token)
        ensure_repo(work_dir, auth_url, branch, logger, token)
        seed_repo_template(work_dir, skill_dir, logger)
        sync_skill_code(work_dir, skill_dir, logger)

        run_git(["config", "user.name", "AI Agent Tools Scanner"], work_dir, logger, token, check=False)
        run_git(["config", "user.email", "ai-agent-tools-scanner@localhost"], work_dir, logger, token, check=False)

        run_git(["add", "-A"], work_dir, logger, token)
        commit_msg = "%s - %s" % (DEFAULTS["commit_prefix"], date)
        r = run_git(["commit", "-m", commit_msg], work_dir, logger, token, check=False)
        if r.returncode != 0:
            combined = (r.stdout or "") + (r.stderr or "")
            if "nothing to commit" in combined or "no changes added" in combined:
                logger.info("没有新的变更需要提交")
            else:
                raise RuntimeError("commit 失败: " + mask(combined, token))

        last_err = None
        for attempt in range(1, retries + 1):
            logger.info("推送尝试 %d/%d -> %s (%s)" % (attempt, retries, mask(repo_url, token), branch))
            r = run_git(["push", "-u", "origin", branch], work_dir, logger, token, check=False)
            if r.returncode == 0:
                h = run_git(["rev-parse", "--short", "HEAD"], work_dir, logger, token, check=False)
                commit_hash = (h.stdout or "").strip()
                logger.info("推送成功，commit=%s" % commit_hash)
                print("PUSH_RESULT=SUCCESS COMMIT=%s" % commit_hash)
                return 0
            last_err = mask((r.stderr or r.stdout or "").strip(), token)
            logger.error("推送失败（第 %d 次）: %s" % (attempt, last_err))
            # 远端领先（non-fast-forward）时，先 pull --rebase 再重试，避免盲目重试必然失败
            if "rejected" in last_err or "fetch first" in last_err or "non-fast-forward" in last_err:
                logger.info("检测到远端领先，执行 git pull --rebase 后重试")
                pr = run_git(["pull", "--rebase", "origin", branch], work_dir, logger, token, check=False)
                if pr.returncode != 0:
                    logger.error("pull --rebase 失败，中止 rebase: %s" % mask((pr.stderr or pr.stdout or "").strip(), token))
                    run_git(["rebase", "--abort"], work_dir, logger, token, check=False)
            if attempt < retries:
                logger.info("等待 %d 秒后重试..." % retry_interval)
                time.sleep(retry_interval)

        logger.error("推送最终失败（已重试 %d 次）: %s" % (retries, last_err))
        print("PUSH_RESULT=FAILED")
        return 3
    except Exception:
        logger.error("git_push 异常：\n" + mask(traceback.format_exc(), token))
        print("PUSH_RESULT=ERROR")
        return 1


if __name__ == "__main__":
    sys.exit(main())
