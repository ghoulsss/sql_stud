import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    # cur.execute("""CREATE TABLE tab1(
    # score INTEGER,
    # from TEXT
    # )""")
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    print(result)