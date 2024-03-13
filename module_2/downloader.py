"""SOLID principle: Open/Closed Principle (OCP)
This module is responsible for downloading news articles using the scraper module.
It expects a file containing URLs as input and saves the downloaded articles to the folder processed.
"""

import os
import sys
sys.path.append(os.path.abspath('C:\\Users\\camer\\Documents\\Homework\\CS325\\Project2\\CS325_p2'))
from module_1.scraper import scrape_news

def download_articles(urls_file):
    """Download news articles from URLs provided in the file.

    Args:
        urls_file (str): Path to the file containing URLs of news articles.
    """
    if not os.path.exists('Processed'):
        os.makedirs('Processed')
    
    with open(urls_file, 'r') as file:
        urls = file.readlines()
    
    for index, url in enumerate(urls):
        url = url.strip()
        article_text = scrape_news(url)
        if article_text:
            with open(f'Processed/article_{index + 1}.txt', 'w') as file:
                file.write(article_text)
                print(f"Article {index + 1} downloaded successfully.")
        else:
            print(f"Failed to download article {index + 1}.")

if __name__ == "__main__":
    urls_file = './Data/raw/rawFileName.txt'
    download_articles(urls_file)
