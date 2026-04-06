import sqlite3 as sq

con = sq.connect("database.db")
cur = con.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS users(
    id INTEGER,
    jins INTEGER,
    name TEXT,
    level INTEGER,
    score INTEGER
            )""")

con.colse
