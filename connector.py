import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    password = os.getenv("DB_PASSWORD")
    if not password:
        raise ValueError("DB_PASSWORD is not set. Add it to your .env file.")

    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        user=os.getenv("DB_USER", "root"),
        password=password,
        database=os.getenv("DB_NAME", "web_scraper_db")
    )
    return conn