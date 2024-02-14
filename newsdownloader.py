import requests
from bs4 import BeautifulSoup
import os

def scrape_news(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the main content of the news article
        main_content = soup.find('div', class_='Page-twoColumn')
        
        # Extract text from the main content
        if main_content:
            article_text = main_content.get_text()
            return article_text.strip()
        else:
            return None
    else:
        print(f"Failed to fetch {url}")
        return None

def download_articles(urls_file):
    # Create a directory to store downloaded articles
    if not os.path.exists('downloaded_articles'):
        os.makedirs('downloaded_articles')
    
    # Read the URLs from the file
    with open(urls_file, 'r') as file:
        urls = file.readlines()
    
    # Process each URL
    for index, url in enumerate(urls):
        url = url.strip()  # Remove leading/trailing whitespaces
        
        # Scrape the news article
        article_text = scrape_news(url)
        
        # Save the article text to a file
        if article_text:
            with open(f'downloaded_articles/article_{index + 1}.txt', 'w') as file:
                file.write(article_text)
                print(f"Article {index + 1} downloaded successfully.")
        else:
            print(f"Failed to download article {index + 1}.")

if __name__ == "__main__":
    urls_file = 'links.txt'  # Path to the file containing URLs
    download_articles(urls_file)
