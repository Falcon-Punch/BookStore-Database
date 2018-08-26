import sqlite3

def connect():
    conn=sqlite3.connect("bookList.db")
    curr=conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect("bookList.db")
    curr=conn.cursor()
    curr.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("bookList.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM book")
    rows=curr.fetchall()
    conn.close()
    return rows

connect()
insert("Decoding the Coding Interview", "John Doe", 2015, 123456789)
print(view())
