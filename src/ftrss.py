import feedparser
from typing import TypedDict


class ArticleEntry(TypedDict):
    title: str
    link: str
    published: str
    summary: str


def scan():
    url = "https://www.ft.com/myft/following/982bd69e-6c56-4be0-9fd0-8e746875fb9e.rss"

    feed = feedparser.parse(url)

    if feed is None:
        return

    for entry in feed.entries:
        print(
            entry.title,
            entry.link,
        )


scan()
