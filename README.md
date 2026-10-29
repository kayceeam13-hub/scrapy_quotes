# scrapy_quotes

A small [Scrapy](https://scrapy.org/) project that crawls [quotes.toscrape.com](http://quotes.toscrape.com/) and collects every quote's author, text, and tags, following pagination until the last page.

## Setup

Requires Python 3.9 and [Pipenv](https://pipenv.pypa.io/).

```sh
pipenv install
```

## Running the spider

From the project root:

```sh
# Write results to JSON
pipenv run scrapy crawl quotes -O quotes.json

# Or to CSV
pipenv run scrapy crawl quotes -O quotes.csv
```

`-O` overwrites the output file; use `-o` to append instead. Output files are ignored by git.

A full crawl yields 100 quotes across 10 pages.

## Output

Each item has three fields:

| Field    | Description                                   |
|----------|-----------------------------------------------|
| `author` | Name of the quote's author                    |
| `text`   | The quote, with surrounding curly quotes removed |
| `tags`   | List of tags attached to the quote            |

Example (JSON):

```json
{"author": "J.K. Rowling", "text": "It is our choices, Harry, that show what we truly are, far more than our abilities.", "tags": ["abilities", "choices"]}
```

## Project layout

```
quotes/
  spiders/quotes_spider.py  # QuoteSpider: parses quotes and follows "Next" links
  items.py                  # QuotesItem definition
  pipelines.py              # QuotesPipeline: strips curly quote marks from text
  settings.py               # Scrapy settings (pipeline enabled, robots.txt obeyed)
scrapy.cfg
Pipfile
```
