# daily2rxiv

daily2rxiv 是一个每日论文摘要生成器，面向想快速浏览前沿生命科学、医学和计算生物学论文的用户。v1 会从 arXiv、bioRxiv、medRxiv 抓取标题、作者、摘要、日期和链接，并生成 Markdown 日报与 JSON 数据。

## 功能

- arXiv：使用官方 Atom API，默认关注 `q-bio.*`、`cs.LG`、`stat.ML` 以及生命医学相关关键词。
- bioRxiv / medRxiv：使用 `api.biorxiv.org/details/{server}/{date}/{cursor}/json` 接口分页抓取。
- 输出：
  - `data/YYYY-MM-DD/papers.json`
  - `data/YYYY-MM-DD/digest.md`
  - `data/latest.json`
- 摘要：
  - GitHub Actions 默认不使用 OpenAI/LLM。
  - 设置 `DAILY2RXIV_TRANSLATION_PROVIDER=google` 时，会用无密钥机器翻译生成中文标题、中文摘要和中文概括。
  - 翻译接口不可用时自动 fallback；fallback 不伪造中文翻译，会保留英文标题/摘要并明确提示中文翻译未生成。

## 本地运行

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

生成当天日报：

```bash
daily2rxiv fetch --output data --limit 30
```

不使用 LLM，仅运行抓取和 fallback：

```bash
daily2rxiv fetch --date 2026-07-06 --output data --limit 5 --no-llm
```

启用无密钥机器翻译：

```bash
DAILY2RXIV_TRANSLATION_PROVIDER=google daily2rxiv fetch --date 2026-07-06 --output data --limit 5 --no-llm
```

也可以直接用模块方式运行：

```bash
python -m daily2rxiv fetch --sources arxiv,biorxiv,medrxiv --no-llm
```

## 配置

- `DAILY2RXIV_TRANSLATION_PROVIDER`：可选，设置为 `google` 时启用无密钥机器翻译。
- `DAILY2RXIV_ARXIV_CATEGORIES`：可选，逗号分隔的 arXiv 分类。
- `DAILY2RXIV_ARXIV_TERMS`：可选，逗号分隔的 arXiv 检索词。
- `DAILY2RXIV_BIORXIV_LOOKBACK_DAYS`：可选，bioRxiv/medRxiv 当天为空时向前回看的天数，默认 3。
- `DAILY2RXIV_TIMEOUT`：可选，HTTP 超时时间，默认 30 秒。

## 测试

```bash
python -m compileall daily2rxiv tests
python -m unittest discover -s tests
```

常规测试不访问外部网络。需要真实接口 smoke test 时，可手动运行：

```bash
daily2rxiv fetch --date 2026-07-06 --limit 5 --no-llm --output tmp/smoke
```

## GitHub Actions

仓库包含两个 workflow：

- `CI`：每次 push/PR 运行编译和单元测试。
- `Daily Digest`：每天北京时间 22:00 定时生成日报并提交到仓库；默认不使用 OpenAI/LLM，使用无密钥机器翻译生成中文标题和摘要。
