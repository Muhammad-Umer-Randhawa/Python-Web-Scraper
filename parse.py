from bs4 import BeautifulSoup
import logging
def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    quote_divs = soup.find_all("div", class_="quote")

    quotes = []
    for quote_div in quote_divs:
        text_tag = quote_div.find("span", class_="text")
        author_tag = quote_div.find("small", class_="author")
        if text_tag is None or author_tag is None:
            logging.warning("Skipping malformed quote block")
            continue
        quotes.append({"text": text_tag.text, "author": author_tag.text})

    return quotes