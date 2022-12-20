import sqlite3

def connect(name):
    global con
    con = sqlite3.connect(name+".db")
    print(f"Connected to: {name}.db, execute commands with db.execute(value)")


def execute(val):
        cur = con.cursor()
        cur.execute(val)
