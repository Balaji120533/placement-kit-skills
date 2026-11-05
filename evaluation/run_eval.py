"""Runs evaluation/test-sheet.md through fresh `claude -p` sessions. Resumable."""
import json
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SHEET = Path(sys.argv[1])
OUT = Path(sys.argv[2])
ONLY = sys.argv[3] if len(sys.argv) > 3 else None     # regex on task id
WORKERS = int(sys.argv[4]) if len(sys.argv) > 4 else 4
MODEL = "sonnet"
TIMEOUT = 420
CLAUDE = str(Path.home() / ".local/bin/claude.exe")
CWD = OUT / "cwd"
OUT.mkdir(parents=True, exist_ok=True)
CWD.mkdir(exist_ok=True)

CODE_TOOLS = ["Bash(python:*)", "Bash(python3:*)", "Bash(gcc:*)", "Bash(java:*)", "Bash(javac:*)", "Bash(./*)", "Write"]
SEARCH_TOOLS = ["WebSearch", "WebFetch"]
BASE_TOOLS = ["Skill", "Read", "Glob", "Grep"]

TLE_CODE = """def has_pair(a, t):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == t:
                return True
    return False
# n = 10^5"""
EXPLAIN = "I sort the array and use two pointers from both ends, moving in based on the sum. It is O(n log n) because of the sort."
C_CODE = 'int x = 5; int y = x++ * 2; printf("%d %d", x, y);'


def section(title):
    text = SHEET.read_text(encoding="utf-8")
    return text.split(f"## {title}")[1].split("\n## ")[0]


def rows(title):
    out = []
    for line in section(title).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0].isdigit():
            out.append(cells)
    return out


def tasks():
    t = []
    for arm, tools in (("with", []), ("without", ["--disable-slash-commands"])):
        for c in rows("DSA: 15 problems"):
            t.append((f"dsa{int(c[0]):02d}_{arm}", tools, CODE_TOOLS,
                      [f"Help me solve {c[1]}", "Just give me the full solution with its time and space complexity."]))
        for name, title in (("apt", "Aptitude: 30 questions"), ("cs", "CS fundamentals: 30 MCQs")):
            for c in rows(title):
                t.append((f"{name}{int(c[0]):02d}_{arm}", tools, CODE_TOOLS,
                          [c[1].strip('"'), "My answer is A."]))
        for c in rows("Company data"):
            allowed = [] if c[0] == "1" else SEARCH_TOOLS
            t.append((f"co{c[0]}_{arm}", tools, allowed, [c[1].strip('"')]))
    for c in rows("Explain-back catches missing items"):
        t.append((f"eb{c[0]}_with", [], CODE_TOOLS, [c[1].strip('"')]))
    for c in rows("Correct skill and mode"):
        p = c[1].replace("<paste code>", TLE_CODE, 1) if "TLE" in c[1] else c[1]
        p = p.replace("<paste explanation>", EXPLAIN + " Problem: Two Sum on a sorted array.")
        p = p.replace("<paste code>", C_CODE)
        allowed = SEARCH_TOOLS if "Zoho" in p else CODE_TOOLS
        t.append((f"route{int(c[0]):02d}_with", [], allowed, [p]))
    return t


def turn(prompt, flags, allowed, session):
    cmd = [CLAUDE, "-p", "--model", MODEL, "--output-format", "stream-json", "--verbose",
           "--append-system-prompt", "On this machine run Python as `python`, not `python3`, in the Bash tool. gcc is available for C."] + flags
    cmd += ["--allowedTools", ",".join(BASE_TOOLS + allowed)]
    if session:
        cmd += ["--resume", session]
    r = subprocess.run(cmd, cwd=CWD, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=TIMEOUT, input=prompt)
    text, used, sid, res = [], [], session, {}
    for line in r.stdout.splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        sid = e.get("session_id", sid)
        if e.get("type") == "assistant":
            for b in e["message"].get("content", []):
                if b.get("type") == "text":
                    text.append(b["text"])
                elif b.get("type") == "tool_use":
                    used.append({"tool": b["name"], "input": b.get("input")})
        if e.get("type") == "result":
            res = {k: e.get(k) for k in ("is_error", "subtype", "num_turns", "duration_ms", "total_cost_usd")}
    return {"prompt": prompt, "text": "\n".join(text), "tools": used, "result": res,
            "rc": r.returncode, "stderr": r.stderr[-400:]}, sid


def run(task):
    tid, flags, allowed, prompts = task
    path = OUT / f"{tid}.json"
    if path.exists():
        return tid, "skipped"
    t0, turns, sid = time.time(), [], None
    try:
        for p in prompts:
            res, sid = turn(p, flags, allowed, sid)
            turns.append(res)
    except subprocess.TimeoutExpired:
        turns.append({"prompt": "TIMEOUT", "text": "", "tools": [], "result": {"is_error": True}, "rc": -1})
    path.write_text(json.dumps({"id": tid, "secs": round(time.time() - t0), "turns": turns}, indent=1), encoding="utf-8")
    return tid, "done"


todo = [t for t in tasks() if not ONLY or re.search(ONLY, t[0])]
print(len(todo), "tasks", flush=True)
with ThreadPoolExecutor(WORKERS) as ex:
    for i, (tid, s) in enumerate(ex.map(run, todo), 1):
        print(i, tid, s, flush=True)
