from __future__ import annotations

import json
import os
import re
from collections import Counter
from urllib.parse import urlencode
from urllib.request import Request, urlopen

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


def summarize_paper(paper: Paper) -> SummaryResult:
    return fallback_summary(paper)


def fallback_summary(paper: Paper, max_chars: int = 360) -> SummaryResult:
    abstract = normalize_text(paper.abstract)
    title_zh, abstract_zh = translate_paper_fields(paper)
    if not abstract:
        text = "暂无摘要，建议直接阅读论文页面。"
    elif abstract_zh:
        text = f"机器翻译摘要显示：{_first_sentences(abstract_zh, max_chars=max_chars)}"
    else:
        keywords = extract_keywords(paper, limit=3)
        keyword_text = "、".join(keywords) if keywords else "论文主题"
        text = (
            f"当前使用 fallback，未进行机器翻译。该论文的关键词包括 {keyword_text}；"
            "请结合英文摘要阅读，或设置 DAILY2RXIV_TRANSLATION_PROVIDER=google 以生成中文标题、中文摘要和中文概括。"
        )
    return SummaryResult(
        summary=text,
        keywords=extract_keywords(paper),
        method="fallback",
        title_zh=title_zh,
        abstract_zh=abstract_zh,
    )


def extract_keywords(paper: Paper, limit: int = 5) -> list[str]:
    text = f"{paper.title} {paper.abstract}".lower()
    words = re.findall(r"[a-z][a-z0-9-]{3,}", text)
    counts = Counter(word for word in words if word not in STOPWORDS)
    return [word for word, _ in counts.most_common(limit)]


def translate_paper_fields(paper: Paper) -> tuple[str, str]:
    provider = os.getenv("DAILY2RXIV_TRANSLATION_PROVIDER", "").strip().lower()
    if provider not in {"google", "google-translate"}:
        return "", ""
    title = normalize_text(paper.title)
    abstract = normalize_text(paper.abstract)
    try:
        title_zh = translate_text(title) if title else ""
        abstract_zh = translate_text(_first_sentences(abstract, max_chars=900)) if abstract else ""
    except Exception:
        return "", ""
    return title_zh, abstract_zh


def translate_text(text: str) -> str:
    params = urlencode(
        {
            "client": "gtx",
            "sl": "en",
            "tl": "zh-CN",
            "dt": "t",
            "q": text,
        }
    )
    request = Request(
        f"https://translate.googleapis.com/translate_a/single?{params}",
        headers={"User-Agent": "daily2rxiv/0.1"},
    )
    with urlopen(request, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8", errors="replace"))
    chunks = payload[0] if payload and isinstance(payload[0], list) else []
    translated = "".join(str(chunk[0]) for chunk in chunks if chunk and chunk[0])
    return normalize_text(translated)


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
