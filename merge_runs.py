#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, subprocess, sys

WD = r"C:\Users\Administrator\WorkBuddy\ai-agent-tools-scanner-data"
PREV_COMMIT = "6597ec5"
DATE = "2026-08-29"

def find_git():
    import glob
    cands = glob.glob(os.path.expanduser(r"~/.workbuddy/vendor/PortableGit*/cmd/git.exe"))
    return cands[0] if cands else "git"

def git_show(path):
    g = find_git()
    r = subprocess.run([g, "-C", WD, "show", "%s:%s" % (PREV_COMMIT, path)],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError("git show failed: " + r.stderr)
    return r.stdout

# my 3 tools
with open(os.path.join(WD, "collected-%s.json" % DATE), "r", encoding="utf-8") as f:
    mine = json.load(f)

# earlier run's tools from its committed report JSON
prev_json = json.loads(git_show("reports/%s/ai-agent-tools-report-%s.json" % (DATE, DATE)))
prev_tools = prev_json.get("tools", [])

def norm(n):
    return (n or "").strip().lower()

merged = {}
order = []
for t in prev_tools + mine:
    k = norm(t.get("name"))
    if k in merged:
        continue
    merged[k] = t
    order.append(k)

result = [merged[k] for k in order]

print("prev count=%d mine count=%d merged count=%d" % (len(prev_tools), len(mine), len(result)))
print("names:", [t.get("name") for t in result])

with open(os.path.join(WD, "collected-%s.json" % DATE), "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print("WROTE collected-%s.json with %d tools" % (DATE, len(result)))
