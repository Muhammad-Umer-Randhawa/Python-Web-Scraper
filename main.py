import logging
from fetch import fetch_quotes
from parse import parse_quotes
from storage import save_quotes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("scraper.log"),
        logging.StreamHandler()
    ]
)

html = fetch_quotes("https://quotes.toscrape.com/")
if html is None:
    logging.error("Failed to fetch page. Exiting.")
else:
    quotes = parse_quotes(html)
    for q in quotes:
        print(q)
    save_quotes(quotes)
