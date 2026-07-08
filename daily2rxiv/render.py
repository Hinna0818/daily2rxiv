from __future__ import annotations

import json
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

from daily2rxiv.config import AppConfig
from daily2rxiv.models import Paper


def write_outputs(papers: list[Paper], config: AppConfig) -> tuple[Path, Path, Path]:
    payload = build_payload(papers, config)
    day_dir = config.output_dir / config.run_date.isoformat()
    day_dir.mkdir(parents=True, exist_ok=True)

    json_path = day_dir / "papers.json"
    digest_path = day_dir / "digest.md"
    latest_path = config.output_dir / "latest.json"

    json_text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    json_path.write_text(json_text, encoding="utf-8")
    latest_path.parent.mkdir(parents=True, exist_ok=True)
    latest_path.write_text(json_text, encoding="utf-8")
    digest_path.write_text(render_markdown(payload), encoding="utf-8")
    return json_path, digest_path, latest_path


def build_payload(papers: list[Paper], config: AppConfig) -> dict[str, object]:
    return {
        "date": config.run_date.isoformat(),
        "generated_at": datetime.now(UTC).isoformat(),
        "generated_by": config.generated_by,
        "source_count": _source_counts(papers),
        "paper_count": len(papers),
        "papers": [paper.to_dict() for paper in papers],
    }


def render_markdown(payload: dict[str, object]) -> str:
    date_value = payload["date"]
    papers = payload.get("papers") or []
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for paper in papers:
        grouped[str(paper.get("source") or "unknown")].append(paper)

    lines = [
        f"# daily2rxiv Digest - {date_value}",
        "",
        f"共收录 {payload.get('paper_count', 0)} 篇论文。",
        "",
    ]
    if not papers:
        lines.extend(["今天没有抓取到符合条件的论文。", ""])
        return "\n".join(lines)

    for source in ("arxiv", "biorxiv", "medrxiv"):
        source_papers = grouped.get(source)
        if not source_papers:
            continue
        lines.extend([f"## {source}", ""])
        for index, paper in enumerate(source_papers, start=1):
            title = _escape_md(str(paper.get("title") or "Untitled"))
            title_zh = _escape_md(str(paper.get("title_zh") or ""))
            url = str(paper.get("url") or "")
            authors = ", ".join(str(author) for author in paper.get("authors", [])[:5])
            if len(paper.get("authors", [])) > 5:
                authors += " et al."
            meta = " | ".join(
                item
                for item in [
                    str(paper.get("published_date") or ""),
                    str(paper.get("category") or ""),
                    f"DOI: {paper.get('doi')}" if paper.get("doi") else "",
                ]
                if item
            )
            summary = str(paper.get("summary") or "暂无摘要。")
            abstract = str(paper.get("abstract") or "")
            abstract_zh = str(paper.get("abstract_zh") or "")
            method = str(paper.get("summary_method") or "unknown")
            keywords = ", ".join(str(item) for item in paper.get("keywords", []))

            heading = title_zh or title
            lines.append(
                f"### {index}. [{heading}]({url})" if url else f"### {index}. {heading}"
            )
            if title_zh and title_zh != title:
                lines.append(f"- Original title: {title}")
            if authors:
                lines.append(f"- Authors: {authors}")
            if meta:
                lines.append(f"- Meta: {meta}")
            if method == "fallback" and not abstract_zh:
                lines.append("- 中文翻译: 暂未生成（当前使用 fallback，请检查翻译接口或 DAILY2RXIV_TRANSLATION_PROVIDER 配置）。")
            elif abstract_zh:
                lines.append(f"- 中文摘要: {abstract_zh}")
            if abstract:
                lines.append(f"- Abstract: {_clip(abstract, 420)}")
            lines.append(f"- Summary ({method}): {summary}")
            if keywords:
                lines.append(f"- Keywords: {keywords}")
            lines.append("")
    return "\n".join(lines)


def _source_counts(papers: list[Paper]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for paper in papers:
        counts[paper.source] = counts.get(paper.source, 0) + 1
    return counts


def _escape_md(value: str) -> str:
    return value.replace("[", "\\[").replace("]", "\\]")


def _clip(value: str, max_chars: int) -> str:
    if len(value) <= max_chars:
        return value
    return value[: max_chars - 1].rstrip() + "..."
