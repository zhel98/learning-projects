import sqlite3

#A4
connect = sqlite3.connect("users.db")
#рука с ручкой
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
           name VARCHAR(50) NOT NULL,
           age INTEGER NOT NULL,
           hobby TEXT
        )       
''')
