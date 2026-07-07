from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Any


@dataclass(slots=True)
class SummaryResult:
    summary: str
    keywords: list[str]
    method: str
    title_zh: str = ""
    abstract_zh: str = ""


@dataclass(slots=True)
class Paper:
    id: str
    source: str
    title: str
    abstract: str
    authors: list[str]
    published_date: str
    url: str
    doi: str | None = None
    category: str | None = None
    raw: dict[str, Any] = field(default_factory=dict)
    title_zh: str | None = None
    abstract_zh: str | None = None
    summary: str | None = None
    keywords: list[str] = field(default_factory=list)
    summary_method: str | None = None

    @property
    def dedupe_key(self) -> str:
        if self.doi:
            return f"doi:{self.doi.lower().strip()}"
        if self.id:
            return f"id:{self.source}:{self.id.lower().strip()}"
        return f"url:{self.url.lower().strip()}"

    def with_summary(self, result: SummaryResult) -> "Paper":
        self.title_zh = result.title_zh
        self.abstract_zh = result.abstract_zh
        self.summary = result.summary
        self.keywords = result.keywords
        self.summary_method = result.method
        return self

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def dedupe_papers(papers: list[Paper]) -> list[Paper]:
    seen: set[str] = set()
    deduped: list[Paper] = []
    for paper in papers:
        key = paper.dedupe_key
        if key in seen:
            continue
        seen.add(key)
        deduped.append(paper)
    return deduped


def normalize_text(value: str | None) -> str:
    if not value:
        return ""
    return re.sub(r"\s+", " ", value).strip()


def parse_date(value: str | None, fallback: date | None = None) -> str:
    if not value:
        return fallback.isoformat() if fallback else ""
    match = re.search(r"\d{4}-\d{2}-\d{2}", value)
    if match:
        return match.group(0)
    match = re.search(r"(\d{4})(\d{2})(\d{2})", value)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return fallback.isoformat() if fallback else normalize_text(value)
