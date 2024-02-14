# News Article Downloader/Scraper

This is a Python program designed to collect and download news articles from a specified list of URLS. It uses `requests` to fetch the HTML contents and `BeautifulSoup` to extract the text from news articles. 

## How it Works

1. Create a text file named `links.txt` in the same directory as the Python script (`newsdownloader.py`).
2. In `links.txt`, add the URLs of the news articles you want to download, with each URL on a new line.
3. Run the `news_downloader.py` script. It will read the URLs from `links.txt`, visit each URL, and download the main content of the news articles.
4. The downloaded articles will be saved as individual text files in a directory named `downloaded_articles`.

## Instructions

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).
3. Install the required Python packages by running the following command in your terminal:

For example in Miniconda:
   conda install beautifulsoup4
   conda install requests

4. Optional if you use yaml
   1. conda env create -f requirements.yml
   2. conda activate cammoss

## Note
-The Scrapper was tested primarily used with Associated Press News (AP news) and nothing else. 
-There are some problems with the text that still need need to get worked out. Examples: line spaces, question marks, social media.