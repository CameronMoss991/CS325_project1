"""SOLID principle: Single Responsibility Principle (SRP)
This module is responsible for scraping news articles from URLs.
It expects a URL as input and outputs the text content of the article.
"""

import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    """Scrape news article from the given URL.

    Args:
        url (str): The URL of the news article.

    Returns:
        str: Text content of the news article, or None if failed to fetch.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        main_content = soup.find('div', class_='Page-twoColumn')
        if main_content:
            article_text = main_content.get_text()
            return article_text.strip()
        else:
            return None
    else:
        print(f"Failed to fetch {url}")
        return None
