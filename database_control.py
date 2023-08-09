import sqlite3
from datetime import date, datetime


con = sqlite3.connect("sport_dairy.db")
cursor = con.cursor()


def add_pushups():
    cursor.execute("""CREATE TABLE IF NOT EXISTS pushups
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    time TEXT,
                    count INTEGER)
                    """)

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



def week_progress():
    #TODO: check the existence of the database
    #TODO: check the existence of the current table
    cursor.execute("SELECT * FROM pushups")
    print(cursor.fetchall())

add_pushups()
week_progress()
