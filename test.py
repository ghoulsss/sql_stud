import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score LIMIT 5")
    result = cur.fetchall()
    print(result)