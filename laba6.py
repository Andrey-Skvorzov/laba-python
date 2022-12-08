import sqlite3
def sql_fetch():
    with sqlite3.connect('laba6.db') as db:
        cursor = db.cursor()

        cursor.execute(""" CREATE TABLE users(
            login TEXT
        )""")
        try:
            value=['Fyffsdfs']
            cursor.executemany("INSERT INTO users(login)VALUES(?)", (value,))
            cursor.execute("SELECT * FROM users")
            result = (cursor.fetchone())
            if result:
             print(result[0])
        except:
            print('None')
sql_fetch()





'''def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM users')
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
sql_fetch(con)'''