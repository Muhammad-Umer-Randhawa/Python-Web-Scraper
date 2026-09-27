from fetch import fetch_quotes
from parse import parse_quotes
from storage import save_quotes

html = fetch_quotes("https://quotes.toscrape.com/")
quotes = parse_quotes(html)
for q in quotes:
    print(q)
save_quotes(quotes)
