# filename: news_scraper.p
import sys
import feedparser
from datetime import datetime

def scrape_news(start_date, end_date):
    url = "http://feeds.bbci.co.uk/news/rss.xml"  # BBC News RSS feed

    feed = feedparser.parse(url)

    for entry in feed.entries:
        publication_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')
        if start_date <= publication_date <= end_date:
            print(f'Headline: {entry.title}')
            print(f'Link: {entry.link}')
            print(f'Publication Date: {publication_date.strftime("%Y-%m-%d")}')
            print()

if __name__ == "__main__":
    if len(sys.argv) > 2:
        try:
            start_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
            end_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please provide dates in YYYY-MM-DD format.")
            sys.exit(1)
    else:
        start_date = datetime.now()
        end_date = datetime.now()

    scrape_news(start_date, end_date)
