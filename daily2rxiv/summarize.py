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

PHRASE_TRANSLATIONS = (
    ("single-cell", "单细胞"),
    ("single cell", "单细胞"),
    ("genomics", "基因组学"),
    ("genome", "基因组"),
    ("immune", "免疫"),
    ("disease-associated", "疾病相关"),
    ("disease associated", "疾病相关"),
    ("programs", "程序"),
    ("program", "程序"),
    ("cohort", "队列"),
    ("cohorts", "队列"),
    ("patient", "患者"),
    ("patients", "患者"),
    ("model", "模型"),
    ("models", "模型"),
    ("benchmark", "基准评估"),
    ("benchmarks", "基准评估"),
    ("treatment response", "治疗反应"),
    ("cell-state", "细胞状态"),
    ("cell state", "细胞状态"),
    ("signals", "信号"),
    ("reveals", "揭示"),
    ("identifies", "识别"),
    ("identify", "识别"),
    ("analysis", "分析"),
    ("learning", "学习"),
    ("deep learning", "深度学习"),
    ("machine learning", "机器学习"),
    ("protein", "蛋白质"),
    ("clinical", "临床"),
    ("biomedical", "生物医学"),
    ("foundation model", "基础模型"),
    ("large language model", "大语言模型"),
    ("language model", "语言模型"),
    ("preprint", "预印本"),
)


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
    title_zh = fallback_translate_title(paper.title)
    abstract_zh = fallback_translate_abstract(abstract, max_chars=720)
    if not abstract:
        text = "暂无摘要，建议直接阅读论文页面。"
    else:
        text = _first_sentences(abstract, max_chars=max_chars)
        text = f"该研究摘要显示：{fallback_translate_abstract(text, max_chars=max_chars)}"
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


def fallback_translate_title(title: str) -> str:
    text = normalize_text(title)
    if not text:
        return ""
    return _rule_translate_text(text)


def fallback_translate_abstract(abstract: str, *, max_chars: int = 720) -> str:
    text = normalize_text(abstract)
    if not text:
        return "暂无中文摘要。"
    translated = _rule_translate_text(_first_sentences(text, max_chars=max_chars))
    return translated


def _rule_translate_text(text: str) -> str:
    translated = text
    for source, target in PHRASE_TRANSLATIONS:
        translated = re.sub(
            rf"\b{re.escape(source)}\b",
            target,
            translated,
            flags=re.IGNORECASE,
        )
    if translated == text:
        return f"规则翻译草稿：{text}"
    return f"规则翻译草稿：{translated}"


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
