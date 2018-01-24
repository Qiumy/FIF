import feedparser
import time
from ..models import News
from .. import db


def getLatestNews():
    rss_url = "http://finance.yahoo.com/news/rss"
    feeds = feedparser.parse(rss_url)
    entries = feeds['entries']
    for i in range(len(entries)-2):
        entry = entries[i]
        if News.query.filter_by(title=entry["title"]).first() is None:
            new = News(title=entry["title"], link=entry["link"],
                       time=time.strftime("%Y-%m-%d %H:%M:%S", entry["published_parsed"]))
            db.session.add(new)
            db.session.commit()
    return entries[:-2]


if __name__ == '__main__':
    getLatestNews()