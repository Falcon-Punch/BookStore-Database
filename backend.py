import sqlite3

def connect():
    conn=sqlite3.connect("bookList.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

connect()
