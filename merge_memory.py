#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把散落在各工作区的 .workbuddy/memory 记忆文件合并成结构化导出包。

规则：
- journal/YYYY-MM-DD.md  同一天多个工作区的日志按内容去重后合并
- memory/MEMORY.md        各工作区的长期项目备注合并去重
- memory/automations.md   自动化巡检记录

用法：
    python merge_memory.py --out <导出目录> [--root <扫描根目录>] ...
扫描根目录默认取 WORKBUDDY_HOME / WORKSPACE_ROOT / HOME 下的常见位置。
"""
import argparse
import hashlib
import os
import re
from collections import defaultdict

DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.md$")

DEFAULT_ROOT_SUFFIXES = [
    os.path.join(".workbuddy", "memory"),
    os.path.join("WorkBuddy"),
]


def default_roots():
    """自动探测常见的 WorkBuddy 记忆所在目录。"""
    roots = []
    home = os.path.expanduser("~")
    env_home = os.environ.get("WORKBUDDY_HOME")
    if env_home:
        roots.append(env_home)
    roots.append(home)
    ws = os.environ.get("WORKSPACE_ROOT")
    if ws:
        roots.append(ws)
    # 常见下载/工作目录
    for d in ("D:/360Downloads", "C:/Users/Public", os.path.join(home, "Documents")):
        if os.path.isdir(d):
            roots.append(d)
    # 去重保序
    seen, out = set(), []
    for r in roots:
        key = os.path.abspath(r)
        if key not in seen and os.path.isdir(key):
            seen.add(key)
            out.append(r)
    return out



def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", "ignore")).hexdigest()


def collect(roots, exclude=()):
    """返回 (daily: {date: [(path, text)]}, longterm: [(path, text)], autos: [(path, text)])"""
    daily = defaultdict(list)
    longterm = []
    autos = []
    ex = [os.path.abspath(e).replace("\\", "/") for e in exclude]
    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root):
            norm = dirpath.replace("\\", "/")
            if "/.workbuddy/memory" not in norm and not norm.endswith("/.workbuddy/memory"):
                continue
            if any(norm.startswith(e) for e in ex):
                continue
            for fn in filenames:
                fp = os.path.join(dirpath, fn)
                try:
                    with open(fp, "r", encoding="utf-8") as f:
                        text = f.read()
                except (UnicodeDecodeError, OSError):
                    try:
                        with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                            text = f.read()
                    except OSError:
                        continue
                rel = fp.replace("\\", "/")
                m = DATE_RE.match(fn)
                if m:
                    daily[m.group(1)].append((rel, text))
                elif fn == "MEMORY.md":
                    longterm.append((rel, text))
                elif fn == "memory.md" and "automations" in rel:
                    autos.append((rel, text))
    return daily, longterm, autos


def strip_h1(text: str) -> str:
    lines = text.splitlines()
    out = []
    for ln in lines:
        if ln.startswith("# ") and not out:
            continue  # 去掉重复的一级标题
        out.append(ln)
    return "\n".join(out).strip()


def merge_daily(daily, out):
    os.makedirs(os.path.join(out, "journal"), exist_ok=True)
    written = []
    for date in sorted(daily):
        seen = set()
        blocks = []
        for path, text in sorted(daily[date], key=lambda x: -len(x[1])):
            body = strip_h1(text)
            if not body:
                continue
            h = sha(body)
            if h in seen:
                continue
            seen.add(h)
            blocks.append(body)
        if not blocks:
            continue
        content = "# {}\n\n".format(date) + "\n\n".join(blocks) + "\n"
        fp = os.path.join(out, "journal", "{}.md".format(date))
        with open(fp, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        written.append((date, len(blocks), len(content)))
    return written


def merge_longterm(longterm, out):
    if not longterm:
        return None
    os.makedirs(os.path.join(out, "memory"), exist_ok=True)
    seen = set()
    blocks = []
    for path, text in sorted(longterm, key=lambda x: -len(x[1])):
        body = text.strip()
        if not body:
            continue
        h = sha(body)
        if h in seen:
            continue
        seen.add(h)
        blocks.append((path, body))
    parts = [
        "# 项目长期记忆（合并自各工作区 MEMORY.md）\n",
        "> 本文件由多个工作区的 `MEMORY.md` 去重合并而成，内容按来源块保留。\n",
    ]
    for path, body in blocks:
        parts.append("\n---\n\n<!-- source: {} -->\n\n".format(path))
        parts.append(body)
        parts.append("\n")
    content = "".join(parts)
    fp = os.path.join(out, "memory", "MEMORY.md")
    with open(fp, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return len(blocks), len(content)


def merge_autos(autos, out):
    if not autos:
        return None
    os.makedirs(os.path.join(out, "memory"), exist_ok=True)
    blocks = []
    seen = set()
    for path, text in sorted(autos, key=lambda x: -len(x[1])):
        body = text.strip()
        h = sha(body)
        if h in seen:
            continue
        seen.add(h)
        blocks.append((path, body))
    parts = ["# 自动化任务记忆\n"]
    for path, body in blocks:
        parts.append("\n---\n\n<!-- source: {} -->\n\n".format(path))
        parts.append(body)
        parts.append("\n")
    content = "".join(parts)
    fp = os.path.join(out, "memory", "automations.md")
    with open(fp, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return len(blocks), len(content)


def main():
    ap = argparse.ArgumentParser(description="合并 WorkBuddy 记忆文件为结构化导出包")
    ap.add_argument("--out", required=True, help="导出目录")
    ap.add_argument("--root", action="append", default=[], help="扫描根目录（可多次指定）")
    ap.add_argument("--exclude", action="append", default=[], help="排除的目录前缀（可多次指定）")
    ap.add_argument("--copy-identity", action="append", default=[],
                    help="复制身份文件（SOUL/IDENTITY/USER.md）所在目录")
    args = ap.parse_args()

    out = os.path.abspath(args.out)
    roots = args.root if args.root else default_roots()
    roots = [r for r in roots if os.path.isdir(r)]
    exclude = list(args.exclude) + [out]

    daily, longterm, autos = collect(roots, exclude)
    print("扫描根目录：")
    for r in roots:
        print("  - " + r)
    print("收集：daily {} 天 / longterm {} 份 / autos {} 份".format(
        len(daily), len(longterm), len(autos)))

    w = merge_daily(daily, out)
    for date, blocks, size in w:
        print("  journal/{}.md  ({} 块, {} 字节)".format(date, blocks, size))

    lt = merge_longterm(longterm, out)
    if lt:
        print("  memory/MEMORY.md  ({} 源, {} 字节)".format(*lt))
    au = merge_autos(autos, out)
    if au:
        print("  memory/automations.md  ({} 源, {} 字节)".format(*au))

    for ident_dir in args.copy_identity:
        for fn in ("SOUL.md", "IDENTITY.md", "USER.md"):
            src = os.path.join(ident_dir, fn)
            if os.path.isfile(src):
                dst_dir = os.path.join(out, "identity")
                os.makedirs(dst_dir, exist_ok=True)
                with open(src, "r", encoding="utf-8") as f:
                    data = f.read()
                with open(os.path.join(dst_dir, fn), "w", encoding="utf-8", newline="\n") as f:
                    f.write(data)
                print("  identity/{}  <- {}".format(fn, src))

    total = 0
    for dirpath, _, filenames in os.walk(out):
        for fn in filenames:
            total += os.path.getsize(os.path.join(dirpath, fn))
    print("导出包合计 {} 字节".format(total))


if __name__ == "__main__":
    main()
