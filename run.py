"""SOLID principle: Dependency Inversion Principle (DIP)
This module serves as the main program to run the news downloader.
It expects a command-line argument specifying whether to use URLs or a file.
"""

import sys
from module_1.scraper import scrape_news
from module_2.downloader import download_articles

def main():
    """Main function to run the news downloader."""
    if len(sys.argv) != 2:
        print("Usage: python3 run.py URL/File/argument")
        return
    
    argument = sys.argv[1]
    if argument.lower() == 'url':
        urls = ['https://example.com/article1', 'https://example.com/article2']
        for index, url in enumerate(urls):
            article_text = scrape_news(url)
            if article_text:
                with open(f'Processed/article_{index + 1}.txt', 'w') as file:
                    file.write(article_text)
                    print(f"Article {index + 1} downloaded successfully.")
            else:
                print(f"Failed to download article {index + 1}.")
    elif argument.lower() == 'file':
        urls_file = './Data/raw/rawFileName.txt'
        download_articles(urls_file)
    else:
        print("Invalid argument. Please specify 'URL' or 'File'.")

if __name__ == "__main__":
    main()
