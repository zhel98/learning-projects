create_tasks_table = '''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )

'''
#PIP INSTALL FLET(ALL)
#crud - create read update delete

#create
insert_task = 'INSERT INTO tasks (task) VALUES (?)'

#read
select_tasks = 'SELECT id, task, completed FROM tasks'
select_tasks_completed = 'SELECT id, task FROM tasks WHERE completed = 1'
select_tasks_uncompleted = 'SELECT id, task FROM tasks WHERE completed = 0'

#update
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

#delete
delete_task = 'DELETE FROM tasks WHERE id =?'