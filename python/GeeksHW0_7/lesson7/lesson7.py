import sqlite3

#A4
connect = sqlite3.connect("users.db")
#рука с ручкой
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name VARCHAR(50) NOT NULL,
           age INTEGER NOT NULL,
           hobby TEXT
        )       
''')
connect.commit()


# CRUD - Create, Read, Update, Delete

# INSERT INTO users(name, age, hobby) → говорим базе: в какие колонки вставляем
# VALUES ("Eldar", 28, "лыжи") → говорим: какие значения туда пойдут

def create_user(name, age, hobby): #---Create---#
        #cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES ("{name}", {age}, "{hobby}")') - неправильный вариант
        cursor.execute(
                'INSERT INTO users(name,age,hobby) VALUES(?,?,?)',
                (name, age, hobby)
        )
        connect.commit()
        print("Пользователь добавлен")
        
# create_user("Eldiiar", 28,"likes to suck dick")


def read_user(): #---Read---#
        cursor.execute('SELECT * FROM users')
        # data = cursor.fetchmany(2) #возвращает первые две записи (1,2)
        data = cursor.fetchall() #возвращает все данные
        # data = cursor.fetchone() #возвращает самое первое значение в таблице
        print(f"all users\n {data}")
        
# read_user()

def update_user(new_name, rowid): #---Update---#
        cursor.execute(
                'UPDATE users SET name = ? WHERE rowid = ?',
                (new_name, rowid)
        )
        connect.commit()
        print("User updated")

#update_user("John",2)
# read_user()

def delete_user(id): #---Delete---# 
        cursor.execute(
                'DELETE FROM users WHERE id = ?', #rowid он присваивает и запоминает к какой записи он был привязан так что его использовать не стоит
                (id,) #обязательная запятая нужна так как ожидает tuple//кортеж
        )
        connect.commit()
        print("User Deleted")
        
# delete_user(3)
# read_user()


