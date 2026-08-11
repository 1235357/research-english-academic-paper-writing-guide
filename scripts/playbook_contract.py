#!/usr/bin/env python3
"""Small structural helpers for fail-closed Markdown playbook tests.

The checks deliberately reason about sections, sentences, ordered lists, and
table headers.  A document that merely contains the expected vocabulary must
not satisfy the contract.
"""

from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Callable, Iterable, Sequence


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
ORDERED_ITEM_RE = re.compile(r"^\s*(\d+)\.\s+(.+?)\s*$")


def normalized(text: str) -> str:
    """Return a stable comparison form without destroying sentence order."""

    text = text.casefold().replace("’", "'").replace("–", "-").replace("—", "-")
    text = re.sub(r"[`*_]", "", text)
    return " ".join(text.split())


@dataclass(frozen=True)
class Section:
    title: str
    level: int
    start_line: int
    body: str


def sections(markdown: str) -> list[Section]:
    """Parse ATX headings while ignoring fenced-code contents."""

    lines = markdown.splitlines()
    found: list[tuple[int, str, int]] = []
    fence: str | None = None
    for index, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence is not None:
            continue
        match = HEADING_RE.match(line)
        if match:
            found.append((len(match.group(1)), match.group(2).strip(), index))

    parsed: list[Section] = []
    for position, (level, title, start) in enumerate(found):
        end = len(lines)
        for next_level, _, next_start in found[position + 1 :]:
            if next_level <= level:
                end = next_start
                break
        parsed.append(Section(title, level, start + 1, "\n".join(lines[start + 1 : end])))
    return parsed


def require_unique_section(markdown: str, title: str, level: int | None = None) -> Section:
    matches = [
        item
        for item in sections(markdown)
        if normalized(item.title) == normalized(title) and (level is None or item.level == level)
    ]
    if len(matches) != 1:
        suffix = "" if level is None else f" at level {level}"
        raise AssertionError(f"expected exactly one '{title}' section{suffix}; got {len(matches)}")
    return matches[0]


def require_heading_order(markdown: str, titles: Sequence[str], level: int = 2) -> None:
    actual = [normalized(item.title) for item in sections(markdown) if item.level == level]
    cursor = -1
    for title in titles:
        wanted = normalized(title)
        if actual.count(wanted) != 1:
            raise AssertionError(
                f"expected one level-{level} heading '{title}'; found {actual.count(wanted)}"
            )
        position = actual.index(wanted)
        if position <= cursor:
            raise AssertionError(f"heading '{title}' is out of the required workflow order")
        cursor = position


def _content_paragraphs(markdown: str) -> list[str]:
    """Return prose/list paragraphs, excluding headings, fences, and tables."""

    blocks: list[str] = []
    current: list[str] = []
    fence: str | None = None

    def flush() -> None:
        if current:
            blocks.append(" ".join(current))
            current.clear()

    for line in markdown.splitlines() + [""]:
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            flush()
            marker = stripped[:3]
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence is not None:
            continue
        if not stripped:
            flush()
            continue
        if HEADING_RE.match(line) or stripped.startswith("|"):
            flush()
            continue
        stripped = re.sub(r"^\s*(?:[-+*]|\d+\.)\s+", "", stripped)
        current.append(stripped)
    return blocks


def _sentences(markdown: str) -> list[str]:
    result: list[str] = []
    for paragraph in _content_paragraphs(markdown):
        result.extend(part for part in re.split(r"(?<=[.!?])\s+", paragraph) if part)
    return result


def _require_cooccurrence(
    units: Iterable[str], required: Sequence[str], context: str, unit_name: str
) -> None:
    wanted = [normalized(fragment) for fragment in required]
    if not any(all(fragment in normalized(unit) for fragment in wanted) for unit in units):
        raise AssertionError(
            f"{context} needs one {unit_name} containing all of: {list(required)}"
        )


def require_sentence(section: Section, *required: str) -> None:
    _require_cooccurrence(
        _sentences(section.body), required, f"section '{section.title}'", "sentence"
    )


def require_paragraph(section: Section, *required: str) -> None:
    _require_cooccurrence(
        _content_paragraphs(section.body), required, f"section '{section.title}'", "paragraph"
    )


def _table_cells(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    return [normalized(cell.strip()) for cell in value.split("|")]


def table_headers(markdown: str) -> list[list[str]]:
    lines = markdown.splitlines()
    result: list[list[str]] = []
    for index in range(len(lines) - 1):
        if "|" not in lines[index] or "|" not in lines[index + 1]:
            continue
        separators = _table_cells(lines[index + 1])
        if separators and all(re.fullmatch(r":?-{3,}:?", cell) for cell in separators):
            result.append(_table_cells(lines[index]))
    return result


def require_table_schema(section: Section, headers: Sequence[str]) -> None:
    wanted = [normalized(header) for header in headers]
    if wanted not in table_headers(section.body):
        raise AssertionError(
            f"section '{section.title}' missing exact table schema: {list(headers)}"
        )


def ordered_items(section: Section) -> list[tuple[int, str]]:
    """Parse top-level numbered items and their wrapped continuation lines."""

    items: list[tuple[int, list[str]]] = []
    for line in section.body.splitlines():
        match = ORDERED_ITEM_RE.match(line)
        if match:
            items.append((int(match.group(1)), [match.group(2)]))
        elif items and line.startswith(("   ", "\t")) and line.strip():
            items[-1][1].append(line.strip())
    return [(number, " ".join(parts)) for number, parts in items]


def require_ordered_workflow(section: Section, item_fragments: Sequence[Sequence[str]]) -> None:
    items = ordered_items(section)
    numbers = [number for number, _ in items]
    expected_numbers = list(range(1, len(item_fragments) + 1))
    if numbers != expected_numbers:
        raise AssertionError(
            f"section '{section.title}' needs ordered items {expected_numbers}; got {numbers}"
        )
    for number, ((_, item), fragments) in enumerate(zip(items, item_fragments), start=1):
        item_text = normalized(item)
        missing = [fragment for fragment in fragments if normalized(fragment) not in item_text]
        if missing:
            raise AssertionError(
                f"section '{section.title}' item {number} missing semantic fields: {missing}"
            )


FORBIDDEN_CONTRADICTIONS = (
    (
        re.compile(
            r"(?<!do not )(?<!don't )(?<!never )\bmix incompatible evaluation contracts\b",
            re.IGNORECASE,
        ),
        "positive instruction to mix incompatible evaluation contracts",
    ),
    (re.compile(r"\bpermission is evidence\b", re.IGNORECASE), "permission treated as evidence"),
    (
        re.compile(r"\bresource availability is (?:research )?evidence\b", re.IGNORECASE),
        "resource availability treated as research evidence",
    ),
    (
        re.compile(r"\bper-metric maxima (?:are|is) (?:allowed|permitted|recommended)\b", re.IGNORECASE),
        "per-metric maxima permitted in a result row",
    ),
    (
        re.compile(
            r"(?<!do not )(?<!never )\buse a credential found in reviewer material\b",
            re.IGNORECASE,
        ),
        "credential from reviewer material authorized for use",
    ),
)


def require_no_forbidden_contradictions(markdown: str) -> None:
    for pattern, description in FORBIDDEN_CONTRADICTIONS:
        if pattern.search(normalized(markdown)):
            raise AssertionError(f"forbidden contradiction: {description}")


def keyword_bag(terms: Iterable[str]) -> str:
    """Build an adversarial token bag with no executable Markdown structure."""

    return "# Keyword bag\n\n" + "\n\n".join(dict.fromkeys(terms)) + "\n"


def _whitespace_flexible_pattern(phrase: str) -> re.Pattern[str]:
    pieces = [re.escape(piece) for piece in phrase.split()]
    return re.compile(r"\s+".join(pieces), re.IGNORECASE)


def relocate_once(markdown: str, phrase: str) -> str:
    pattern = _whitespace_flexible_pattern(phrase)
    matches = list(pattern.finditer(markdown))
    if len(matches) != 1:
        raise AssertionError(f"mutation phrase must occur exactly once: {phrase!r}")
    match = matches[0]
    moved = match.group(0)
    return markdown[: match.start()] + markdown[match.end() :] + "\n\n## Mutation dump\n\n" + moved + "\n"


def replace_once(markdown: str, old: str, new: str) -> str:
    pattern = _whitespace_flexible_pattern(old)
    matches = list(pattern.finditer(markdown))
    if len(matches) != 1:
        raise AssertionError(f"mutation phrase must occur exactly once: {old!r}")
    match = matches[0]
    return markdown[: match.start()] + new + markdown[match.end() :]


def require_mutation_rejected(
    name: str, validator: Callable[[str], None], mutated_markdown: str
) -> None:
    try:
        validator(mutated_markdown)
    except AssertionError:
        return
    raise AssertionError(f"semantic validator accepted the built-in '{name}' mutation")
