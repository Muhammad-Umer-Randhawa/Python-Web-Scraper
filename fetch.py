import requests

def fetch_quotes(url):
    response = requests.get(url)
    return response.content.decode("utf-8")