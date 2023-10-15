import sqlite3
conn = sqlite3.connect('my_friends.db')
c = conn.cursor()
c.execute(
    "CREATE TABLE fRIENDS (FIRST_NAME TEXT, LAST_NAME TEXT, CLOSENESS INTEGER);")
conn.commit()
conn.close()
