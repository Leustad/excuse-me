import sqlite3

with sqlite3.connect('excuses.db') as connection:
    cur = connection.cursor()
    cur.execute("DROP TABLE excuses_data")

    cur.execute("""CREATE TABLE excuses_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        excuse TEXT)
      """)

    with open('excuses.txt') as o_file:
        content = o_file.readlines()
        for row in content:
            cur.execute("INSERT INTO excuses_data(excuse) VALUES(?)", (row.strip(),))
