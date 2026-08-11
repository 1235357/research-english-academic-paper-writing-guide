#!/usr/bin/env python3
"""Measure prose rhythm (monotony) of a manuscript.

Companion to references/playbooks/09-concise-and-rigorous.md and
references/playbooks/17-native-register-and-ai-detection.md.

Reports sentence-length distribution and its coefficient of variation
(SD / mean, the standard "burstiness" measure in the general literature on
this topic) plus a histogram. Python 3 stdlib only.

This is a readability diagnostic, not a detector proxy, and it deliberately
has no "target" to hit. An earlier version of this script printed a
LOW/HIGH/ok verdict against a fixed numeric band; that framing was removed
because playbook 17 section 2.4 documents that "rewrite toward a specific
statistical profile" cannot be separated, mechanically, from helping
AI-generated text evade detection -- the primary source behind this
playbook's own bias evidence demonstrates that directly. What this script
still does, and does well: flag prose that is unusually *uniform* in
rhythm, which reads as monotonous to a human reader independent of any
detector question, and point at playbook 09/17's rewrite techniques for
fixing that specific defect.

Usage:
    python3 measure_prose_rhythm.py paper.tex
    python3 measure_prose_rhythm.py paper.txt --plain
    python3 measure_prose_rhythm.py paper.tex --keep-abstract
    python3 measure_prose_rhythm.py old.tex new.tex        # compare two

For a PDF, extract text first:  pdftotext -f 1 -l 7 paper.pdf - > body.txt
(then pass --plain), but .tex is preferred: PDF extraction mixes table cells
and caption fragments into the sentence stream and inflates the short bucket.
"""

from __future__ import annotations

import argparse
import re
import statistics
import sys
from pathlib import Path

# Sentence-length bands, in words.
BANDS = [("<10", 0, 9), ("10-19", 10, 19), ("20-29", 20, 29), ("30+", 30, 10**9)]

# Informational monotony flags only -- NOT targets to rewrite toward. These
# mark "this distribution is unusually concentrated," nothing more. See the
# module docstring and playbook 17 section 2.4 for why this script does not
# supply a target band.
MONOTONY_CV_FLAG = 0.35          # below this, sentence length barely varies
MONOTONY_BAND_SHARE_FLAG = 0.85  # one band holding this much of the mass


def strip_latex(src: str, keep_abstract: bool = False) -> str:
    """Reduce a .tex source to running prose.

    Removes float environments, the abstract, math, comments, and macros, so
    table cells and captions do not pollute the sentence stream.
    """
    if not keep_abstract:
        src = re.sub(r"\\begin\{abstract\}.*?\\end\{abstract\}", " ", src, flags=re.S)
    # Float and tabular environments carry no running prose.
    src = re.sub(
        r"\\begin\{(table|figure|tabular|align|equation)\*?\}.*?\\end\{\1\*?\}",
        " ",
        src,
        flags=re.S,
    )
    src = re.sub(r"(?<!\\)%.*", " ", src)          # comments
    src = re.sub(r"\$\$.*?\$\$", " X ", src, flags=re.S)
    src = re.sub(r"\$[^$]*\$", " X ", src)          # inline math -> one token
    # Macros whose *argument* is not prose: structural markers (environment
    # names), headings, and front matter. Drop the control word AND its
    # argument together -- e.g. \section{Related Work} must not leave the
    # bare word "Related Work" glued onto whatever prose follows it with no
    # punctuation between them. `\*?` covers starred variants (\section*{}).
    # Known limitation: a `{...}` argument containing its own nested braces
    # (e.g. \title{A \textbf{Novel} Method}) is not matched here, since this
    # is a regex pass, not a balanced-brace parser; it falls through to the
    # generic macro strip below and the heading text can still leak. This is
    # rare in practice (titles/headings are usually plain text) and is a
    # pre-existing limitation of the regex approach, not new in this fix.
    src = re.sub(
        r"\\(input|include|includegraphics|label|ref|eqref|cite\w*|bibliography"
        r"|usepackage|documentclass|setlength|newcommand|renewcommand"
        r"|section|subsection|subsubsection|paragraph|title|author|date"
        r"|begin|end)\*?"
        r"\s*(\[[^\]]*\])?\s*(\{[^{}]*\})*",
        " ",
        src,
    )
    # Remaining macros: drop the control word, keep any prose argument.
    src = re.sub(r"\\[a-zA-Z]+\*?\s*(\[[^\]]*\])?", " ", src)
    src = src.replace("{", " ").replace("}", " ")
    src = re.sub(r"~", " ", src)
    return re.sub(r"\s+", " ", src).strip()


def sentences(text: str, min_words: int = 4) -> list[str]:
    """Split into sentences, ignoring fragments below `min_words`.

    The min_words floor drops list labels and stray tokens that would
    otherwise be counted as very short sentences.
    """
    # Protect common abbreviations so they do not end a sentence.
    protected = re.sub(
        r"\b(Fig|Sec|Eq|Tab|et al|i\.e|e\.g|cf|vs|approx|Ref)\.",
        lambda m: m.group(0).replace(".", "\x00"),
        text,
    )
    parts = re.split(r"(?<=[.!?])\s+", protected)
    out = []
    for p in parts:
        p = p.replace("\x00", ".").strip()
        if len(p.split()) >= min_words:
            out.append(p)
    return out


def analyse(path: Path, plain: bool, keep_abstract: bool) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = raw if plain else strip_latex(raw, keep_abstract)
    sents = sentences(text)
    if len(sents) < 5:
        raise SystemExit(
            f"{path}: only {len(sents)} sentences found -- wrong file, or use --plain?"
        )
    lengths = [len(s.split()) for s in sents]
    mean = statistics.mean(lengths)
    sd = statistics.pstdev(lengths)
    counts = {name: 0 for name, _, _ in BANDS}
    for n in lengths:
        for name, lo, hi in BANDS:
            if lo <= n <= hi:
                counts[name] += 1
                break
    return {
        "path": path,
        "n": len(lengths),
        "mean": mean,
        "sd": sd,
        "cv": sd / mean if mean else 0.0,
        "counts": counts,
        "pct": {k: 100.0 * v / len(lengths) for k, v in counts.items()},
        "sents": sents,
        "lengths": lengths,
    }


def report(r: dict, show_long: int) -> None:
    print(f"\n=== {r['path']} ===")
    print(f"prose sentences : {r['n']}")
    print(f"mean length     : {r['mean']:.1f} words")
    print(f"std deviation   : {r['sd']:.1f}")
    print(f"CV (SD / mean)  : {r['cv']:.3f}")

    print("\ndistribution:")
    max_band_pct = 0.0
    for name, _, _ in BANDS:
        pct = r["pct"][name]
        max_band_pct = max(max_band_pct, pct / 100.0)
        bar = "#" * int(round(pct / 2))
        print(f"  {name:6s} {r['counts'][name]:4d}  {pct:5.1f}%  {bar}")

    flags = []
    if r["cv"] < MONOTONY_CV_FLAG:
        flags.append(
            f"CV is {r['cv']:.2f} -- sentence length barely varies across the "
            "manuscript. This is an informational flag, not a target to clear:"
        )
    if max_band_pct >= MONOTONY_BAND_SHARE_FLAG:
        flags.append(
            f"one length band holds {max_band_pct * 100:.0f}% of all sentences -- "
            "unusually concentrated."
        )
    if flags:
        print("\nmonotony flag:")
        for f in flags:
            print(f"  - {f}")
        print(
            "  This reads as flat to a human reader independent of any detector\n"
            "  question. See playbook 09 (concise/rigorous prose) and playbook 17\n"
            "  R2-R3 (split a judgment from its supporting detail into its own\n"
            "  sentence) for how to fix it -- there is no numeric band to aim for,\n"
            "  only 'does every sentence here carry the same weight.'"
        )

    if show_long:
        print(f"\nlongest {show_long} sentences (split candidates):")
        for s in sorted(r["sents"], key=lambda z: -len(z.split()))[:show_long]:
            print(f"  {len(s.split()):3d}w: {s[:100]}...")

    print(
        "\nNOTE: this measures rhythm only. It does not reproduce, estimate, or\n"
        "      correlate with any AI-detection vendor's score, and this skill\n"
        "      does not provide a target range to rewrite toward -- see\n"
        "      playbook 17 section 2.4 for why."
    )


def compare(a: dict, b: dict) -> None:
    print("\n=== comparison ===")
    print(f"{'metric':<18}{'before':>10}{'after':>10}{'delta':>10}")
    rows = [
        ("sentences", a["n"], b["n"], "{:+d}"),
        ("mean words", a["mean"], b["mean"], "{:+.1f}"),
        ("SD", a["sd"], b["sd"], "{:+.1f}"),
        ("CV", a["cv"], b["cv"], "{:+.3f}"),
        ("short <10w %", a["pct"]["<10"], b["pct"]["<10"], "{:+.1f}"),
        ("mid 10-29w %", a["pct"]["10-19"] + a["pct"]["20-29"],
         b["pct"]["10-19"] + b["pct"]["20-29"], "{:+.1f}"),
        ("long 30+w %", a["pct"]["30+"], b["pct"]["30+"], "{:+.1f}"),
    ]
    for name, av, bv, fmt in rows:
        if isinstance(av, int):
            print(f"{name:<18}{av:>10d}{bv:>10d}{fmt.format(bv - av):>10}")
        else:
            print(f"{name:<18}{av:>10.3f}{bv:>10.3f}{fmt.format(bv - av):>10}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=Path,
                    help="one manuscript, or two to compare (before after)")
    ap.add_argument("--plain", action="store_true",
                    help="input is plain text, not LaTeX")
    ap.add_argument("--keep-abstract", action="store_true",
                    help="include the abstract (default: excluded)")
    ap.add_argument("--show-long", type=int, default=5, metavar="N",
                    help="list the N longest sentences (0 to disable)")
    args = ap.parse_args()

    for f in args.files:
        if not f.exists():
            raise SystemExit(f"no such file: {f}")

    results = [analyse(f, args.plain, args.keep_abstract) for f in args.files[:2]]
    for r in results:
        report(r, args.show_long)
    if len(results) == 2:
        compare(results[0], results[1])


if __name__ == "__main__":
    sys.exit(main())
