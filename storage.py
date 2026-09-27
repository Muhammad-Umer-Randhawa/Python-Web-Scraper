from connector import get_connection
def save_quotes(quotes):
    conn = get_connection()
    cursor = conn.cursor()

    for q in quotes:
        cursor.execute(
            "INSERT IGNORE INTO quotes (quote_text, author) VALUES (%s, %s)", 
            (q["text"], q["author"])
        )
    conn.commit()
    cursor.close()
    conn.close()