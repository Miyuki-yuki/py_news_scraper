# filename: news_scraper.p
import sys
from bs4 import BeautifulSoup
import requests
from datetime import datetime

def scrape_news(start_date, end_date):
    url = "https://www.bbc.com/news"  # replace with the URL of the news website you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for news in soup.find_all('div', class_='news'):  # replace with the appropriate HTML tags and classes
        headline = news.find('h2').text
        source = news.find('p', class_='source').text
        publication_date = datetime.strptime(news.find('p', class_='date').text, '%Y-%m-%d')

        if start_date <= publication_date <= end_date:
            print(f'Headline: {headline}')
            print(f'Source: {source}')
            print(f'Publication Date: {publication_date.strftime("%Y-%m-%d")}')
            print()

if __name__ == "__main__":
    start_date = datetime.strptime(sys.argv[1], '%Y-%m-%d') if len(sys.argv) > 1 else datetime.now()
    end_date = datetime.strptime(sys.argv[2], '%Y-%m-%d') if len(sys.argv) > 2 else datetime.now()
    scrape_news(start_date, end_date)