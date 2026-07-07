from __future__ import annotations

import json
from datetime import date, timedelta
from urllib.parse import quote

from daily2rxiv.http import HttpGetter
from daily2rxiv.models import Paper, normalize_text, parse_date

BIORXIV_API_URL = "https://api.biorxiv.org/details"
PAGE_SIZE = 30


def fetch_biorxiv(
    *,
    server: str,
    run_date: date,
    limit: int,
    http_get: HttpGetter,
    lookback_days: int = 3,
) -> list[Paper]:
    for offset in range(lookback_days + 1):
        query_date = run_date - timedelta(days=offset)
        papers = _fetch_biorxiv_date(
            server=server,
            query_date=query_date,
            limit=limit,
            http_get=http_get,
        )
        if papers:
            return papers
    return []


def _fetch_biorxiv_date(
    *,
    server: str,
    query_date: date,
    limit: int,
    http_get: HttpGetter,
) -> list[Paper]:
    cursor = 0
    papers: list[Paper] = []
    interval = f"{query_date.isoformat()}/{query_date.isoformat()}"
    while len(papers) < limit:
        url = (
            f"{BIORXIV_API_URL}/{quote(server)}/"
            f"{quote(interval, safe='/')}/{cursor}/json"
        )
        page = parse_biorxiv_payload(http_get(url), server=server, fallback_date=query_date)
        if not page:
            break
        papers.extend(page)
        if len(page) < PAGE_SIZE:
            break
        cursor += len(page)
    return papers[:limit]


def parse_biorxiv_payload(
    payload: str,
    *,
    server: str,
    fallback_date: date | None = None,
) -> list[Paper]:
    data = json.loads(payload)
    collection = data.get("collection") or []
    papers: list[Paper] = []
    for item in collection:
        doi = normalize_text(item.get("doi")) or None
        version = normalize_text(str(item.get("version") or ""))
        paper_id = doi or _stable_id(server, item)
        url = _paper_url(server, doi, version)
        authors = _parse_authors(item.get("authors"))
        papers.append(
            Paper(
                id=paper_id,
                source=server,
                title=normalize_text(item.get("title")),
                abstract=normalize_text(item.get("abstract")),
                authors=authors,
                published_date=parse_date(item.get("date"), fallback_date),
                url=url,
                doi=doi,
                category=normalize_text(item.get("category")) or None,
                raw={
                    "version": version or None,
                    "type": item.get("type"),
                    "license": item.get("license"),
                    "published": item.get("published"),
                },
            )
        )
    return papers


def _parse_authors(value: str | None) -> list[str]:
    if not value:
        return []
    delimiter = ";" if ";" in value else ","
    return [normalize_text(author) for author in value.split(delimiter) if author.strip()]


def _paper_url(server: str, doi: str | None, version: str) -> str:
    host = "www.medrxiv.org" if server == "medrxiv" else "www.biorxiv.org"
    if doi:
        suffix = f"v{version}" if version else ""
        return f"https://{host}/content/{doi}{suffix}"
    return f"https://{host}/"


def _stable_id(server: str, item: dict[str, object]) -> str:
    title = normalize_text(str(item.get("title") or "untitled")).lower().replace(" ", "-")
    date_value = parse_date(str(item.get("date") or ""))
    return f"{server}:{date_value}:{title[:80]}"
