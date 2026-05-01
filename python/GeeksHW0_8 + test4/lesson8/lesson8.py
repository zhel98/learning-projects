import sqlite3

connect = sqlite3.connect('grade.db')
cursor = connect.cursor()


cursor.execute(
    '''CREATE TABLE IF NOT EXISTS users2(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name VARCHAR(30) NOT NULL,
       age INTEGER NOT NULL
       )
''')


#при помощи форен ки мы связываем две таблицы (id в таблице users2 = user_id в таблице grades)
cursor.execute(
    ''' CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR(30) NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users2(id)        
        )                     
 ''')


def create_user(name, age):
    cursor.execute(
        'INSERT INTO users2(name, age) VALUES (?,?)',
        (name,age)
    )
    connect.commit()
    print("User added")


def create_grade(grade, subject, user_id):
    cursor.execute(
        'INSERT INTO grades(grade, subject, user_id) VALUES(?,?,?)',
        (grade, subject, user_id)
    )
    connect.commit()
    print("Grade added")
    

#---INNER JOIN---# возвращает только те строки, где есть совпадение
def get_user_grade():
    cursor.execute(
        ''' SELECT users2.name, grades.grade, grades.subject
        FROM users2 INNER JOIN grades ON users2.id = grades.user_id           
    ''')
    
    data = cursor.fetchall()
    #[("Eldar", 1, "Физра")]
    for i in data:
        print(f"NAME: {i[0]}, GRADE: {i[1]}, SUBJECT:{i[2]}")


#---LEFT JOIN--- # возвращает все строки из ЛЕВОЙ таблицы + совпадения из правой (если нет — NULL)
def get_user_grade2():
    cursor.execute(
        ''' SELECT users2.name, grades.grade, grades.subject
        FROM users2 LEFT JOIN grades ON users2.id = grades.user_id
    ''')
    
    data = cursor.fetchall()
    for i in data:
        print(f"NAME: {i[0]}, GRADE: {i[1]}, SUBJECT:{i[2]}")


#---RIGHT JOIN--- # возвращает все строки из ПРАВОЙ таблицы + совпадения из левой (если нет — NULL)
def get_user_grade3():
    cursor.execute(
        ''' SELECT users2.name, grades.grade, grades.subject
        FROM users2 RIGHT JOIN grades ON users2.id = grades.user_id
    ''')
    
    data = cursor.fetchall()
    for i in data:
        print(f"NAME: {i[0]}, GRADE: {i[1]}, SUBJECT:{i[2]}")


#---FULL OUTER JOIN--- # возвращает все строки из обеих таблиц, даже если нет совпадений
def get_user_grade4():
    cursor.execute(
        ''' SELECT users2.name, grades.grade, grades.subject
        FROM users2 FULL OUTER JOIN grades ON users2.id = grades.user_id
    ''')
    
    data = cursor.fetchall()
    for i in data:
        print(f"NAME: {i[0]}, GRADE: {i[1]}, SUBJECT:{i[2]}")


# get_user_grade4()
# get_user_grade3()
# get_user_grade2()
# get_user_grade()


def get_sum_grades():#заставляем код проходится по каждой строчке
    cursor.execute('SELECT grade FROM grades')
    data = cursor.fetchall()
    sum_data=0
    for i in data:
        sum_data += i[0]
    print(sum_data)
    
# get_sum_grades()

def get_sum_grades2():#сама таблица дам выдает данные SUM/COUNT/MIN/MAX/AVG
    cursor.execute('SELECT SUM(grade) FROM grades')
    data = cursor.fetchall()
    print(data)

#get_sum_grades2()

def create_my_view():
    cursor.execute('''
         CREATE VIEW IF NOT EXISTS my_view AS 
         SELECT users2.name, grades.grade, grades.subject
         FROM users2 INNER JOIN grades ON users2.id = grades.user_id          
    ''')
    connect.commit()
    print("View created")

#create_my_view()


def get_user_inner_grade():
    cursor.execute('SELECT * FROM my_view')
    data = cursor.fetchall()
    print(data)
    
get_user_inner_grade()





''' ----- ЛЕВАЯ ЧАСТЬ -----'''
# create_user("Eldar",28) - ID : 1
# create_user("Eblan", 29) - ID : 2
# create_user("Misha", 19) - ID: 3 
'''----- ПРАВАЯ ЧАСТЬ -----'''
# create_grade(5,"Физра",1)- ID : 1
# create_grade(2,"Физра",2)- ID : 2
# create_grade(1,"Физра",4)- ID : 4 - ВОТ ЭТОТ АЙДШИНИК НЕ СОВПАДАЕТ С АЙДИШНИКОМ В ЛЕВОЙ ЧАСТИ
