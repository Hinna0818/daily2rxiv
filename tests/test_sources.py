import json
import unittest
from datetime import date
from urllib.parse import parse_qs, urlparse

from daily2rxiv.sources.arxiv import build_arxiv_query, fetch_arxiv, parse_arxiv_feed
from daily2rxiv.sources.biorxiv import fetch_biorxiv, parse_biorxiv_payload


ARXIV_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2607.00001v1</id>
    <updated>2026-07-06T00:00:00Z</updated>
    <published>2026-07-06T00:00:00Z</published>
    <title> Example   arXiv Paper </title>
    <summary> This paper studies biomedical foundation models. </summary>
    <link href="http://arxiv.org/abs/2607.00001v1" rel="alternate" type="text/html"/>
  </entry>
</feed>
"""

EMPTY_ARXIV_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"></feed>
"""


class SourceParsingTests(unittest.TestCase):
    def test_arxiv_parser_handles_missing_optional_fields(self):
        papers = parse_arxiv_feed(ARXIV_FEED)
        self.assertEqual(len(papers), 1)
        paper = papers[0]
        self.assertEqual(paper.id, "2607.00001v1")
        self.assertEqual(paper.authors, [])
        self.assertIsNone(paper.doi)
        self.assertIsNone(paper.category)
        self.assertEqual(paper.published_date, "2026-07-06")

    def test_arxiv_query_includes_date_and_topics(self):
        query = build_arxiv_query(
            run_date=date(2026, 7, 6),
            categories=("q-bio.BM", "cs.LG"),
            terms=("drug discovery",),
        )
        self.assertIn("submittedDate:[202607060000 TO 202607062359]", query)
        self.assertIn("cat:q-bio.BM", query)
        self.assertIn('all:"drug discovery"', query)

    def test_arxiv_fetch_falls_back_to_recent_when_date_query_is_empty(self):
        payloads = [EMPTY_ARXIV_FEED, ARXIV_FEED]
        urls = []

        def fake_get(url):
            urls.append(url)
            return payloads.pop(0)

        papers = fetch_arxiv(
            run_date=date(2026, 7, 6),
            categories=("q-bio.BM",),
            terms=(),
            limit=1,
            http_get=fake_get,
        )
        self.assertEqual(len(papers), 1)
        self.assertEqual(len(urls), 2)
        first_query = parse_qs(urlparse(urls[0]).query)["search_query"][0]
        second_query = parse_qs(urlparse(urls[1]).query)["search_query"][0]
        self.assertIn("submittedDate", first_query)
        self.assertNotIn("submittedDate", second_query)

    def test_biorxiv_parser_handles_empty_collection(self):
        self.assertEqual(
            parse_biorxiv_payload('{"messages": [], "collection": []}', server="biorxiv"),
            [],
        )

    def test_biorxiv_fetch_paginates_until_short_page(self):
        first_page = {
            "collection": [
                {
                    "doi": f"10.1101/2026.07.06.{index:06d}",
                    "title": f"Paper {index}",
                    "abstract": "Abstract",
                    "authors": "A; B",
                    "date": "2026-07-06",
                    "version": 1,
                    "category": "Bioinformatics",
                }
                for index in range(30)
            ]
        }
        second_page = {
            "collection": [
                {
                    "doi": "10.1101/2026.07.06.999999",
                    "title": "Paper 31",
                    "abstract": "Abstract",
                    "authors": "C, D",
                    "date": "2026-07-06",
                    "version": 2,
                    "category": "Genomics",
                }
            ]
        }
        payloads = [json.dumps(first_page), json.dumps(second_page)]
        urls = []

        def fake_get(url):
            urls.append(url)
            return payloads.pop(0)

        papers = fetch_biorxiv(
            server="biorxiv",
            run_date=date(2026, 7, 6),
            limit=31,
            http_get=fake_get,
        )
        self.assertEqual(len(papers), 31)
        self.assertEqual(len(urls), 2)
        self.assertIn("/0/json", urls[0])
        self.assertIn("/30/json", urls[1])


if __name__ == "__main__":
    unittest.main()
