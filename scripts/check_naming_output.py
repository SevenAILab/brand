#!/usr/bin/env python3
"""检查品牌命名输出是否遗漏关键决策结构。"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_MARKERS = [
    "[商标待核实]",
    "[域名待核实]",
    "[账号待核实]",
    "[语义待核实]",
]

SLOP_SUFFIX_RE = re.compile(r"\b[A-Za-z]{3,}(?:ly|ify|ora|exa|ium|able)\b")


def count_any(text: str, needles: list[str]) -> int:
    return sum(text.count(needle) for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser(description="检查品牌命名方案的硬性输出结构。")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()

    if not args.file.exists():
        raise SystemExit(f"文件不存在：{args.file}")

    text = args.file.read_text(encoding="utf-8")
    issues: list[str] = []

    if count_any(text, REQUIRED_MARKERS) == 0:
        issues.append("未发现任何待核实标记：至少应出现商标/域名/账号/语义待核实之一")

    if "最可能死在哪" not in text and "最大风险" not in text and "fatal" not in text.lower():
        issues.append("未发现 fatal flaw / 最大风险 / 最可能死在哪")

    if "可调旋钮" not in text:
        issues.append("未发现可调旋钮")

    if "shortlist" in text.lower() or "候选" in text:
        if "是否可推进" not in text and "不推进" not in text:
            issues.append("候选/shortlist 输出缺少是否可推进判断")

    slop_hits = sorted(set(SLOP_SUFFIX_RE.findall(text)))
    if slop_hits:
        issues.append("疑似 AI slop 后缀候选需人工复核：" + ", ".join(slop_hits[:20]))

    print(f"# 品牌命名输出检查：{args.file}")
    if not issues:
        print("结论：通过")
        return 0

    print("结论：需复核")
    for issue in issues:
        print(f"- {issue}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
