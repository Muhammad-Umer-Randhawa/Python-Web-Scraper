import requests
import logging
def fetch_quotes(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.content.decode("utf-8")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None