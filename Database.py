import sqlite3

conn = sqlite3.connect('Createdb.db')  

cur = conn.cursor()

with open('Createdb.sql', 'r') as file:
    sql_script = file.read()

cur.executescript(sql_script)


conn.commit()
conn.close()

