import sqlite3

connect = sqlite3.connect('grade.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grade INTEGER NOT NULL,
    subject TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
''')

def create_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    connect.commit()
    print(f'User {name} created successfully.')

def create_grade(grade, subject, user_id):
    cursor.execute('INSERT INTO course (grade, subject, user_id) VALUES (?, ?, ?)', (grade, subject, user_id))
    connect.commit()
    print(f'Grade {grade} for subject {subject} created successfully for user ID {user_id}.')


create_user('Alice', 20)
create_user('Bob', 22)
create_grade(85, 'Math', 1)
create_grade(90, 'Science', 1)
create_grade(78, 'Math', 2)
create_grade(88, 'Science', 2)

def get_user_grades():
    cursor.execute('''
    SELECT users.name, course.subject, course.grade
    FROM users FULL OUTER JOIN course ON users.id = course.user_id
    ''')
    results = cursor.fetchall()
    for name, subject, grade in results:
        print(f'User: {name}, Subject: {subject}, Grade: {grade}')
