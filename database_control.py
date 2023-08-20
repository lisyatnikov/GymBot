import sqlite3
from datetime import date, datetime


def set_connection_database():
    con = sqlite3.connect("sport_dairy.db")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS pushups
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date TEXT,
                            time TEXT,
                            count INTEGER)
                            """)
    return con, cursor

def add_pushups(quantity):
    con, cursor = set_connection_database()

    dtnow = datetime.now()
    print(dtnow, type(dtnow))

    present_day = dtnow.strftime('%Y-%m-%d')
    print(present_day, type(present_day))

    present_time = dtnow.strftime('%H:%M:%S')
    print(present_time, type(present_time))

    #quantity = 15
    #minced_oath = 'HUINya'


    exercise_pushups = (present_day, present_time, quantity)

    cursor.execute("INSERT INTO pushups (date,time,count) Values (?,?,?)", exercise_pushups)
    con.commit()



def show_week_progress():
    #TODO: check the existence of the database
    #TODO: check the existence of the current table
    con, cursor = set_connection_database()
    cursor.execute("SELECT * FROM pushups WHERE date > date('now', '-6 days');")
    print(cursor.fetchall())

def show_top5():
    con, cursor = set_connection_database()
    cursor.execute("SELECT * FROM pushups ORDER BY count DESC LIMIT 5")
    print(cursor.fetchall())
    #return(cursor.fetchall())

def monkey_func(banana):
    return (banana - 4)
