from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from daily2rxiv.config import DEFAULT_SOURCES, AppConfig
from daily2rxiv.pipeline import run_fetch


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "fetch":
        try:
            sources = _parse_sources(args.sources)
            _validate_limit(args.limit)
        except ValueError as exc:
            parser.error(str(exc))
        config = AppConfig.from_env(
            run_date=_parse_date_arg(args.date),
            output_dir=Path(args.output),
            limit=args.limit,
            sources=sources,
            use_llm=not args.no_llm,
        )
        papers = run_fetch(config)
        print(f"Wrote {len(papers)} papers to {config.output_dir}")
        return 0
    parser.print_help()
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="daily2rxiv")
    subparsers = parser.add_subparsers(dest="command")
    fetch = subparsers.add_parser("fetch", help="Fetch daily papers and render outputs.")
    fetch.add_argument("--date", default=None, help="Digest date in YYYY-MM-DD format.")
    fetch.add_argument("--output", default="data", help="Output directory.")
    fetch.add_argument("--limit", type=int, default=30, help="Maximum papers per source.")
    fetch.add_argument(
        "--sources",
        default=",".join(DEFAULT_SOURCES),
        help="Comma-separated source list: arxiv,biorxiv,medrxiv.",
    )
    fetch.add_argument("--no-llm", action="store_true", help="Disable OpenAI summaries.")
    return parser


def _parse_date_arg(value: str | None) -> date:
    if not value:
        return date.today()
    return date.fromisoformat(value)


def _parse_sources(value: str) -> tuple[str, ...]:
    sources = tuple(item.strip().lower() for item in value.split(",") if item.strip())
    if not sources:
        raise ValueError("At least one source is required.")
    allowed = set(DEFAULT_SOURCES)
    unknown = sorted(set(sources) - allowed)
    if unknown:
        raise ValueError(f"Unknown sources: {', '.join(unknown)}")
    return sources


def _validate_limit(value: int) -> None:
    if value < 1:
        raise ValueError("--limit must be at least 1.")
