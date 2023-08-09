import sqlite3
from datetime import date, datetime


con = sqlite3.connect("sport_dairy.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS pushups
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                time TEXT,
                count INTEGER)
                """)


def add_pushups():
    dtnow = datetime.now()
    print(dtnow, type(dtnow))

    present_day = dtnow.strftime('%Y-%m-%d')
    print(present_day, type(present_day))

    present_time = dtnow.strftime('%H:%M:%S')
    print(present_time, type(present_time))

    quantity = 15

    minced_oath = 'HUINya'
    print(minced_oath, type(minced_oath))

    exercise_pushups = (present_day, present_time, quantity)

    cursor.execute("INSERT INTO pushups (date,time,count) Values (?,?,?)", exercise_pushups)
    con.commit()

add_pushups()
