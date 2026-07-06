from __future__ import annotations

from datetime import date
from urllib.parse import quote, urlencode
from xml.etree import ElementTree as ET

from daily2rxiv.http import HttpGetter
from daily2rxiv.models import Paper, normalize_text, parse_date

ARXIV_API_URL = "https://export.arxiv.org/api/query"
ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"


def fetch_arxiv(
    *,
    run_date: date,
    categories: tuple[str, ...],
    terms: tuple[str, ...],
    limit: int,
    http_get: HttpGetter,
) -> list[Paper]:
    query = build_arxiv_query(
        run_date=run_date,
        categories=categories,
        terms=terms,
        include_date=True,
    )
    papers = _fetch_query(query, limit=limit, http_get=http_get, fallback_date=run_date)
    if papers:
        return papers[:limit]

    recent_query = build_arxiv_query(
        run_date=run_date,
        categories=categories,
        terms=terms,
        include_date=False,
    )
    return _fetch_query(
        recent_query,
        limit=limit,
        http_get=http_get,
        fallback_date=run_date,
    )[:limit]


def build_arxiv_query(
    *,
    run_date: date,
    categories: tuple[str, ...],
    terms: tuple[str, ...],
    include_date: bool = True,
) -> str:
    date_window = run_date.strftime("%Y%m%d")
    category_query = " OR ".join(f"cat:{category}" for category in categories)
    term_query = " OR ".join(
        f'all:"{term}"' if " " in term else f"all:{term}" for term in terms
    )
    topical = f"({category_query})" if category_query else ""
    if term_query:
        topical = f"({topical} OR ({term_query}))" if topical else f"({term_query})"
    if include_date:
        return f"{topical} AND submittedDate:[{date_window}0000 TO {date_window}2359]"
    return topical


def _fetch_query(
    query: str,
    *,
    limit: int,
    http_get: HttpGetter,
    fallback_date: date,
) -> list[Paper]:
    params = urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": limit,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        },
        quote_via=quote,
    )
    payload = http_get(f"{ARXIV_API_URL}?{params}")
    return parse_arxiv_feed(payload, fallback_date=fallback_date)


def parse_arxiv_feed(payload: str, fallback_date: date | None = None) -> list[Paper]:
    root = ET.fromstring(payload)
    papers: list[Paper] = []
    for entry in root.findall(f"{ATOM_NS}entry"):
        arxiv_id = normalize_text(_text(entry, f"{ATOM_NS}id"))
        title = normalize_text(_text(entry, f"{ATOM_NS}title"))
        abstract = normalize_text(_text(entry, f"{ATOM_NS}summary"))
        published = parse_date(_text(entry, f"{ATOM_NS}published"), fallback_date)
        authors = [
            normalize_text(_text(author, f"{ATOM_NS}name"))
            for author in entry.findall(f"{ATOM_NS}author")
        ]
        authors = [author for author in authors if author]
        doi = normalize_text(_text(entry, f"{ARXIV_NS}doi")) or None
        category = _primary_category(entry)
        url = _alternate_url(entry) or arxiv_id
        paper_id = arxiv_id.rsplit("/", 1)[-1] if arxiv_id else url
        papers.append(
            Paper(
                id=paper_id,
                source="arxiv",
                title=title,
                abstract=abstract,
                authors=authors,
                published_date=published,
                url=url,
                doi=doi,
                category=category,
                raw={"arxiv_id": arxiv_id},
            )
        )
    return papers


def _text(parent: ET.Element, path: str) -> str:
    child = parent.find(path)
    return child.text if child is not None and child.text else ""


def _primary_category(entry: ET.Element) -> str | None:
    primary = entry.find(f"{ARXIV_NS}primary_category")
    if primary is not None and primary.get("term"):
        return primary.get("term")
    category = entry.find(f"{ATOM_NS}category")
    if category is not None and category.get("term"):
        return category.get("term")
    return None


def _alternate_url(entry: ET.Element) -> str | None:
    for link in entry.findall(f"{ATOM_NS}link"):
        if link.get("rel") == "alternate" and link.get("href"):
            return link.get("href")
    return None
