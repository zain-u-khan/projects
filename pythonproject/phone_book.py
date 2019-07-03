import sys
import sqlite3 as sq


conn=sq.connect("test.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS phone_book(name text,number INTEGER)")

cur.execute("SELECT * FROM phone_book")
r=cur.fetchall()

def add():
    call=(sys.argv[2],sys.argv[3])
    for search in r:
        if sys.argv[2] in search:
            print("The number already exist try modyfing")
            break
    else:
        cur.execute("INSERT INTO phone_book VALUES(?,?)",call)

def modify():
    call= (sys.argv[2],sys.argv[3])
    for search in r:
        if sys.argv[2] in search:
            cur.execute("INSERT INTO phone_book VALUES(?,?)",call)
            break
    else:
        print("The value does not exist in the phone book")

def delete():
    call=(sys.argv[2],)
    for search in r:
        if sys.argv[2] in search:
            cur.execute("DELETE FROM phone_book WHERE name IS ?",call)
            break
    else:
        print("the value does not exist try entering one first")


def get():
    call=(sys.argv[2],)
    for search in r:
        if sys.argv[2] in search:
            cur.execute("SELECT number FROM phone_book WHERE name IS ?",call)
            print(cur.fetchone())
            break
    else:
        print("The value foes not exist in the phone book")
           

if sys.argv[1]=="add":
    add()

if sys.argv[1]=="modify":
    modify()

if sys.argv[1]=="delete":
    delete()

if sys.argv[1]=="get":
    get()
r=cur.fetchall()
conn.commit()
conn.close()
