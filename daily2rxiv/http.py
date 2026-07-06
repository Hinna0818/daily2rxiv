from __future__ import annotations

from collections.abc import Callable
from urllib.request import Request, urlopen

HttpGetter = Callable[[str], str]


def make_http_getter(timeout: int = 30) -> HttpGetter:
    def get(url: str) -> str:
        request = Request(
            url,
            headers={
                "User-Agent": "daily2rxiv/0.1 (+https://github.com/Hinna0818/daily2rxiv)",
                "Accept": "application/json, application/atom+xml, application/xml, text/xml",
            },
        )
        with urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(charset, errors="replace")

    return get
