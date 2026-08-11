#!/usr/bin/env python3
"""Quick deterministic checks for English academic paper titles.

This script does not judge scientific quality. It catches surface-level issues
from Lecture 2: excessive length, unsupported phrases, strange acronym casing,
redundancy signals, and low-specificity patterns.
"""
import argparse
import re

RED_FLAGS = {
    "too_broad_phrase": [r"from shallow to deeper", r"towards? .+ human", r"like humans?"],
    "unsupported_claim": [r"understanding like humans?", r"human[- ]like understanding"],
    "redundancy_signal": [r"plug-and-play", r"novel", r"upgraded", r"framework.*function", r"function.*framework"],
    "generic_method_for_task": [r"graph neural networks for", r"deep learning for", r"neural networks for"],
}


def word_count(title: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)?", title))


def strange_midword_caps(title: str):
    tokens = re.findall(r"\b[A-Za-z]+\b", title)
    out = []
    for tok in tokens:
        if len(tok) >= 4 and re.search(r"[a-z][A-Z][a-z]", tok):
            out.append(tok)
    return out


def analyze(title: str):
    title_l = title.lower()
    issues = []
    wc = word_count(title)
    if wc > 15:
        issues.append(f"length: {wc} words; lecture recommends about 15 words or fewer")
    mids = strange_midword_caps(title)
    if mids:
        issues.append("nonstandard mid-word capitalization: " + ", ".join(mids))
    for group, patterns in RED_FLAGS.items():
        for pat in patterns:
            if re.search(pat, title_l):
                issues.append(f"{group}: matched '{pat}'")
    if ":" not in title and wc > 8:
        issues.append("consider whether a method/model name plus subtitle would make contribution clearer")
    return wc, issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="title to evaluate")
    args = parser.parse_args()
    wc, issues = analyze(args.title)
    print(f"Title: {args.title}")
    print(f"Word count: {wc}")
    if issues:
        print("Potential issues:")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. {issue}")
    else:
        print("No deterministic red flags found. Still review core problem, technical innovation, and memorability manually.")

if __name__ == "__main__":
    main()
