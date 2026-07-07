from __future__ import annotations

from daily2rxiv.config import AppConfig
from daily2rxiv.http import make_http_getter
from daily2rxiv.models import Paper, dedupe_papers
from daily2rxiv.render import write_outputs
from daily2rxiv.sources import fetch_arxiv, fetch_biorxiv
from daily2rxiv.summarize import summarize_paper


def run_fetch(config: AppConfig) -> list[Paper]:
    http_get = make_http_getter(config.request_timeout)
    papers: list[Paper] = []

    if "arxiv" in config.sources:
        papers.extend(
            fetch_arxiv(
                run_date=config.run_date,
                categories=config.arxiv_categories,
                terms=config.arxiv_terms,
                limit=config.limit,
                http_get=http_get,
            )
        )
    for server in ("biorxiv", "medrxiv"):
        if server in config.sources:
            papers.extend(
                fetch_biorxiv(
                    server=server,
                    run_date=config.run_date,
                    limit=config.limit,
                    http_get=http_get,
                    lookback_days=config.biorxiv_lookback_days,
                )
            )

    papers = dedupe_papers(papers)
    for paper in papers:
        paper.with_summary(
            summarize_paper(paper, use_llm=config.use_llm, model=config.openai_model)
        )
    write_outputs(papers, config)
    return papers
