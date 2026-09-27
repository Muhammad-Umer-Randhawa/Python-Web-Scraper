# Web Scraper

This project is a simple Python web scraper that pulls quotes from [quotes.toscrape.com](https://quotes.toscrape.com/) and stores them in a MySQL database. It uses `requests` to fetch the page, `BeautifulSoup` to parse the HTML, and a small database layer to save each quote without inserting duplicates.


## What it does

- Fetches the quote page from the target website
- Extracts the quote text and author from each quote block
- Prints the quotes in the terminal
- Saves valid entries into MySQL
- Logs errors and skips malformed data safely

## Project structure

- `main.py` - runs the scraper end to end
- `fetch.py` - handles the HTTP request
- `parse.py` - extracts quote data from the HTML
- `storage.py` - inserts data into the database
- `connector.py` - creates the MySQL connection using environment variables
- `web_scraper.sql` - creates the database and table schema
- `.env.example` - sample database configuration

## Requirements

Make sure you have:

- Python 3.9+
- MySQL Server running locally or on a reachable host
- A database user with access to create tables and insert rows

## Setup

1. Open a terminal in the project folder.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

4. Copy the sample environment file and update the values:

```bash
copy .env.example .env
```

Then edit `.env` with your MySQL settings, for example:

```env
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=web_scraper_db
```

5. Create the database and table from the SQL file:

```bash
mysql -u root -p < web_scraper.sql
```

If you use a different username or host, adjust the command to match your setup.

## Run the scraper

From the project folder, run:

```bash
python main.py
```

The script will fetch the page, parse the quotes, print them to the console, and save them into the `quotes` table.

## Notes

- The scraper is intentionally simple and focused on a single site.

- If the database credentials are missing or invalid, the script will fail early with a clear error.

## Example output

```text
2026-09-27 12:00:00,123 [INFO] Fetching page: https://quotes.toscrape.com/
“The World as I see it is not as I wish it to be.”
— Albert Einstein
```

This project is a neat starting point if you want to learn how to scrape structured data, process HTML, and store it in a relational database.
