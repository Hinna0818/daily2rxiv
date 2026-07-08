import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

from daily2rxiv.config import AppConfig
from daily2rxiv.models import Paper
from daily2rxiv.pipeline import run_fetch
from daily2rxiv.render import build_payload, render_markdown, write_outputs
from daily2rxiv.summarize import fallback_summary, summarize_paper


def sample_paper(source="arxiv"):
    return Paper(
        id=f"{source}:1",
        source=source,
        title="Single-cell genomics reveals disease-associated programs",
        abstract=(
            "Single-cell genomics can identify disease-associated programs. "
            "We benchmarked models across cohorts and found robust signals."
        ),
        authors=["Ada Lovelace", "Grace Hopper"],
        published_date="2026-07-06",
        url="https://example.test/paper",
        doi=None,
        category="q-bio.GN",
    )


class SummarizeRenderPipelineTests(unittest.TestCase):
    def test_no_api_key_path_uses_fallback(self):
        paper = sample_paper()
        with patch.dict("os.environ", {}, clear=True):
            result = summarize_paper(paper)
        self.assertEqual(result.method, "fallback")
        self.assertIn("当前使用 fallback", result.summary)
        self.assertEqual(result.title_zh, "")
        self.assertEqual(result.abstract_zh, "")
        self.assertTrue(result.keywords)

    def test_fallback_handles_missing_abstract(self):
        paper = sample_paper()
        paper.abstract = ""
        result = fallback_summary(paper)
        self.assertEqual(result.method, "fallback")
        self.assertIn("暂无摘要", result.summary)

    def test_translation_provider_populates_chinese_fields(self):
        paper = sample_paper()
        translations = {
            paper.title: "单细胞基因组学揭示疾病相关程序",
            paper.abstract: "单细胞基因组学可以识别疾病相关程序。我们在多个队列中评估模型，并发现稳健信号。",
        }

        def fake_translate(text):
            return translations[text]

        with patch.dict("os.environ", {"DAILY2RXIV_TRANSLATION_PROVIDER": "google"}):
            with patch("daily2rxiv.summarize.translate_text", side_effect=fake_translate):
                result = fallback_summary(paper)

        self.assertEqual(result.method, "fallback")
        self.assertEqual(result.title_zh, "单细胞基因组学揭示疾病相关程序")
        self.assertIn("单细胞基因组学", result.abstract_zh)
        self.assertIn("机器翻译摘要显示", result.summary)

    def test_markdown_contains_core_fields(self):
        paper = sample_paper().with_summary(fallback_summary(sample_paper()))
        config = AppConfig(run_date=date(2026, 7, 6), output_dir=Path("data"))
        markdown = render_markdown(build_payload([paper], config))
        self.assertIn("# daily2rxiv Digest - 2026-07-06", markdown)
        self.assertIn("## arxiv", markdown)
        self.assertNotIn("Original title:", markdown)
        self.assertIn("中文翻译: 暂未生成", markdown)
        self.assertIn("Abstract:", markdown)
        self.assertIn("Summary (fallback)", markdown)
        self.assertIn("Keywords:", markdown)

    def test_write_outputs_creates_daily_and_latest_json(self):
        paper = sample_paper().with_summary(fallback_summary(sample_paper()))
        with tempfile.TemporaryDirectory() as tmpdir:
            config = AppConfig(run_date=date(2026, 7, 6), output_dir=Path(tmpdir))
            json_path, digest_path, latest_path = write_outputs([paper], config)
            self.assertTrue(json_path.exists())
            self.assertTrue(digest_path.exists())
            self.assertTrue(latest_path.exists())
            data = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(data["paper_count"], 1)
            self.assertIn("title_zh", data["papers"][0])
            self.assertIn("abstract_zh", data["papers"][0])
            self.assertEqual(data["papers"][0]["title_zh"], "")

    def test_pipeline_uses_mocked_fetchers_and_writes_outputs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            config = AppConfig(
                run_date=date(2026, 7, 6),
                output_dir=Path(tmpdir),
                limit=2,
                sources=("arxiv", "biorxiv"),
                use_llm=False,
            )
            with patch("daily2rxiv.pipeline.fetch_arxiv", return_value=[sample_paper("arxiv")]):
                with patch(
                    "daily2rxiv.pipeline.fetch_biorxiv",
                    return_value=[sample_paper("biorxiv")],
                ):
                    papers = run_fetch(config)
            self.assertEqual(len(papers), 2)
            self.assertTrue((Path(tmpdir) / "2026-07-06" / "papers.json").exists())
            self.assertTrue((Path(tmpdir) / "2026-07-06" / "digest.md").exists())


if __name__ == "__main__":
    unittest.main()
