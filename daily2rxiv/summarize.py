from __future__ import annotations

import json
import os
import re
from collections import Counter

from daily2rxiv.models import Paper, SummaryResult, normalize_text

STOPWORDS = {
    "about",
    "after",
    "also",
    "among",
    "based",
    "between",
    "could",
    "data",
    "from",
    "have",
    "into",
    "more",
    "most",
    "paper",
    "study",
    "than",
    "that",
    "their",
    "these",
    "this",
    "using",
    "were",
    "with",
}


def summarize_paper(
    paper: Paper,
    *,
    use_llm: bool,
    model: str,
) -> SummaryResult:
    if use_llm and os.getenv("OPENAI_API_KEY"):
        try:
            return summarize_with_openai(paper, model=model)
        except Exception:
            return fallback_summary(paper)
    return fallback_summary(paper)


def fallback_summary(paper: Paper, max_chars: int = 360) -> SummaryResult:
    abstract = normalize_text(paper.abstract)
    if not abstract:
        text = "暂无摘要，建议直接阅读论文页面。"
    else:
        text = _first_sentences(abstract, max_chars=max_chars)
        text = f"该研究摘要显示：{text}"
    return SummaryResult(summary=text, keywords=extract_keywords(paper), method="fallback")


def extract_keywords(paper: Paper, limit: int = 5) -> list[str]:
    text = f"{paper.title} {paper.abstract}".lower()
    words = re.findall(r"[a-z][a-z0-9-]{3,}", text)
    counts = Counter(word for word in words if word not in STOPWORDS)
    return [word for word, _ in counts.most_common(limit)]


def summarize_with_openai(paper: Paper, *, model: str) -> SummaryResult:
    from openai import OpenAI

    client = OpenAI()
    prompt = (
        "请用中文概括下面的科研论文。返回严格 JSON，字段为 summary 和 keywords。"
        "summary 用 2 句，面向想快速了解前沿论文的科研用户；keywords 为 3 到 5 个短语。"
        f"\n标题：{paper.title}\n摘要：{paper.abstract}"
    )
    response = client.responses.create(model=model, input=prompt)
    text = getattr(response, "output_text", "") or ""
    parsed = _parse_json_object(text)
    summary = normalize_text(str(parsed.get("summary") or text))
    keywords_raw = parsed.get("keywords") or extract_keywords(paper)
    keywords = [normalize_text(str(item)) for item in keywords_raw if normalize_text(str(item))]
    return SummaryResult(
        summary=summary or fallback_summary(paper).summary,
        keywords=keywords[:5] or extract_keywords(paper),
        method="llm",
    )


def _first_sentences(text: str, *, max_chars: int) -> str:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    selected: list[str] = []
    total = 0
    for sentence in sentences:
        if not sentence:
            continue
        if total + len(sentence) > max_chars and selected:
            break
        selected.append(sentence)
        total += len(sentence)
    summary = " ".join(selected) or text
    if len(summary) > max_chars:
        return summary[: max_chars - 1].rstrip() + "..."
    return summary


def _parse_json_object(text: str) -> dict[str, object]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if not match:
            return {}
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            return {}
