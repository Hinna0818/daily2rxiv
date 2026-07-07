from __future__ import annotations

import os
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path


DEFAULT_ARXIV_CATEGORIES = (
    "q-bio.BM",
    "q-bio.CB",
    "q-bio.GN",
    "q-bio.MN",
    "q-bio.NC",
    "q-bio.OT",
    "q-bio.PE",
    "q-bio.QM",
    "q-bio.SC",
    "q-bio.TO",
    "cs.LG",
    "stat.ML",
)

DEFAULT_ARXIV_TERMS = (
    "bioinformatics",
    "genomics",
    "single-cell",
    "biomedicine",
    "clinical",
    "protein",
    "drug discovery",
)

DEFAULT_SOURCES = ("arxiv", "biorxiv", "medrxiv")


@dataclass(slots=True)
class AppConfig:
    run_date: date
    output_dir: Path
    limit: int = 30
    sources: tuple[str, ...] = DEFAULT_SOURCES
    use_llm: bool = True
    openai_model: str = "gpt-5.5-mini"
    arxiv_categories: tuple[str, ...] = DEFAULT_ARXIV_CATEGORIES
    arxiv_terms: tuple[str, ...] = DEFAULT_ARXIV_TERMS
    biorxiv_lookback_days: int = 3
    request_timeout: int = 30
    generated_by: str = "daily2rxiv"
    extra: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_env(
        cls,
        *,
        run_date: date,
        output_dir: Path,
        limit: int,
        sources: tuple[str, ...],
        use_llm: bool,
    ) -> "AppConfig":
        model = os.getenv("DAILY2RXIV_OPENAI_MODEL", "gpt-5.5-mini")
        categories = _csv_env("DAILY2RXIV_ARXIV_CATEGORIES", DEFAULT_ARXIV_CATEGORIES)
        terms = _csv_env("DAILY2RXIV_ARXIV_TERMS", DEFAULT_ARXIV_TERMS)
        lookback_days = int(os.getenv("DAILY2RXIV_BIORXIV_LOOKBACK_DAYS", "3"))
        timeout = int(os.getenv("DAILY2RXIV_TIMEOUT", "30"))
        return cls(
            run_date=run_date,
            output_dir=output_dir,
            limit=limit,
            sources=sources,
            use_llm=use_llm,
            openai_model=model,
            arxiv_categories=categories,
            arxiv_terms=terms,
            biorxiv_lookback_days=lookback_days,
            request_timeout=timeout,
        )


def _csv_env(name: str, default: tuple[str, ...]) -> tuple[str, ...]:
    value = os.getenv(name)
    if not value:
        return default
    parsed = tuple(item.strip() for item in value.split(",") if item.strip())
    return parsed or default
