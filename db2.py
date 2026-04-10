import sqlite3 as sq

con = sq.connect("baza.db")
cur = con.cursor()


cur.execute(""" CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    level INTEGER,
    age INTEGER
            )""")

cur.execute(""" CREATE TABLE IF NOT EXISTS xaridlar(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_name TEXT,
    price INTEGER
            )""")

cur.execute("""INSERT OR IGNORE INTO users (id, first_name, last_name, age)
            VALUES (1, 'Rasulbek', 'Xakimbayev', 15)""")

cur.execute("""INSERT OR IGNORE INTO users (id, first_name, last_name, age)
            VALUES (2, 'Shokirjon', 'Salayev', 17)""")

cur.execute("""INSERT OR IGNORE INTO users (id, first_name, last_name, age)
            VALUES (3, 'Durbek', 'Hayotbekov', 15)""")

cur.execute("""INSERT OR IGNORE INTO users (id, first_name, last_name, age)
            VALUES (4, 'Farhod', 'Abdulayev', 15)""")

cur.execute("""INSERT OR IGNORE INTO users (id, first_name, last_name, age)
            VALUES (5, 'Lobarxon', 'Qodirova', 15)""")

cur.execute("""INSERT OR IGNORE INTO users (id, first_name, last_name, age)
            VALUES (6, 'Navroz', 'Rajabov', 15)""")

cur.execute("""INSERT OR IGNORE INTO users (id, first_name, last_name, age)
            VALUES (7, 'Behzod', 'Lozayev', 17)""")





cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (1, 1, 'Olma', 10000)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (2, 2, 'Uzum', 25000)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (3, 3, 'banan', 15000)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (4, 4, 'baliq', 55000)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (5, 5, 'gosht', 100000)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (6, 6, 'ace tea', 10000)""")

cur.execute("""INSERT OR IGNORE INTO xaridlar (id, user_id, product_name, price)
            VALUES (7, 7, 'telefon', 5000000)""")

con.commit()