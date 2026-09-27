from bs4 import BeautifulSoup

def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    quote_divs = soup.find_all("div", class_="quote")

    quotes = []
    for quote_div in quote_divs:
        text = quote_div.find("span", class_="text").text
        author = quote_div.find("small", class_="author").text
        quotes.append({"text": text, "author": author})

    return quotes