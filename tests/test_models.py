import unittest

from daily2rxiv.models import Paper, dedupe_papers, normalize_text, parse_date


class ModelTests(unittest.TestCase):
    def test_dedupe_prefers_doi(self):
        first = Paper(
            id="a",
            source="arxiv",
            title="First",
            abstract="",
            authors=[],
            published_date="2026-07-06",
            url="https://example.test/a",
            doi="10.1101/example",
        )
        duplicate = Paper(
            id="b",
            source="biorxiv",
            title="Duplicate",
            abstract="",
            authors=[],
            published_date="2026-07-06",
            url="https://example.test/b",
            doi="10.1101/EXAMPLE",
        )
        self.assertEqual(dedupe_papers([first, duplicate]), [first])

    def test_text_and_date_normalization(self):
        self.assertEqual(normalize_text("  a\n\n b\tc  "), "a b c")
        self.assertEqual(parse_date("2026-07-06T01:02:03Z"), "2026-07-06")
        self.assertEqual(parse_date("20260706"), "2026-07-06")


if __name__ == "__main__":
    unittest.main()
