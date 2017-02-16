import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import sqlite3

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
cur.executescript("""
DROP TABLE IF EXISTS items;

CREATE TABLE items{
    items_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
};

INSERT INTO items(name, price)VALUES('Apple', 800);
INSERT INTO items(name, price)VALUES('Orenge', 780);
INSERT INTO items(name, price)VALUES('Banana', 430);
""")

conn.commit()

cur = conn.cursor()
cur.execute("SELECT items_id,name,price FROM items")
item_list = cur.fetchall()

for it in item_list:
    print(it)
