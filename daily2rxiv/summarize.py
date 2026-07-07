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
        keywords = extract_keywords(paper, limit=3)
        keyword_text = "、".join(keywords) if keywords else "论文主题"
        text = (
            f"当前使用 fallback，未进行机器翻译。该论文的关键词包括 {keyword_text}；"
            "请结合英文摘要阅读，或检查 OpenAI API 配置以生成中文标题、中文摘要和中文概括。"
        )
    return SummaryResult(
        summary=text,
        keywords=extract_keywords(paper),
        method="fallback",
        title_zh="",
        abstract_zh="",
    )


def extract_keywords(paper: Paper, limit: int = 5) -> list[str]:
    text = f"{paper.title} {paper.abstract}".lower()
    words = re.findall(r"[a-z][a-z0-9-]{3,}", text)
    counts = Counter(word for word in words if word not in STOPWORDS)
    return [word for word, _ in counts.most_common(limit)]


def summarize_with_openai(paper: Paper, *, model: str) -> SummaryResult:
    from openai import OpenAI

    client = OpenAI()
    prompt = (
        "请翻译并概括下面的科研论文。返回严格 JSON，字段为 "
        "title_zh, abstract_zh, summary, keywords。"
        "title_zh 是中文标题翻译；abstract_zh 是完整中文摘要翻译；"
        "summary 用中文 2 句概括，面向想快速了解前沿论文的科研用户；"
        "keywords 为 3 到 5 个中文或英文短语。"
        f"\n标题：{paper.title}\n摘要：{paper.abstract}"
    )
    response = client.responses.create(model=model, input=prompt)
    text = getattr(response, "output_text", "") or ""
    parsed = _parse_json_object(text)
    fallback = fallback_summary(paper)
    title_zh = normalize_text(str(parsed.get("title_zh") or fallback.title_zh))
    abstract_zh = normalize_text(str(parsed.get("abstract_zh") or fallback.abstract_zh))
    summary = normalize_text(str(parsed.get("summary") or text))
    keywords_raw = parsed.get("keywords") or extract_keywords(paper)
    keywords = [normalize_text(str(item)) for item in keywords_raw if normalize_text(str(item))]
    return SummaryResult(
        summary=summary or fallback.summary,
        keywords=keywords[:5] or extract_keywords(paper),
        method="llm",
        title_zh=title_zh,
        abstract_zh=abstract_zh,
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
