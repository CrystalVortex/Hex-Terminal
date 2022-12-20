import sqlite3

def connect(name):
    global con
    con = sqlite3.connect(name+".db")
    print(f"Connected to: {name}.db")


def execute(val):
        cur = con.cursor()
        cur.execute(val)
