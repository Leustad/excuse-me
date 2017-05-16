import sqlite3

with sqlite3.connect('excuses.db') as connection:
    cur = connection.cursor()

    cur.execute("""CREATE TABLE excuses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        excuse TEXT)
      """)

    with open('excuses.txt') as o_file:
        content = o_file.readlines()
        for row in content:
            cur.execute("INSERT INTO excuses(excuse) VALUES(?)", (row.strip(),))
