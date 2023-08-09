

import database_control
import bot




"""commented database operations
dbName = 'sport_dairy.db'


conn = sqlite3.connect(dbName)
cursor = conn.cursor()
print("the fatabase has been created")
create_query = '''CREATE TABLE IF NOT EXISTS pushups(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
date_time INTEGER NOT NULL,
pushups_count INTEGER,
notes TEXT);
'''
cursor.execute(create_query)
print("the table has been created")


conn.commit()
conn.close()
end of comment"""


"""except Exception as e:
    print("database does not exist, err:",e)
    if conn:
        conn.close()"""




def top3():
    pass

add_pushups()
