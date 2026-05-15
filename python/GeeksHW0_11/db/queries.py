create_tasks_table = '''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
    )

'''
#PIP INSTALL FLET(ALL)
#crud - create read update delete

#create
insert_task = 'INSERT INTO tasks (task) VALUES (?)'

#read
select_tasks = 'SELECT id, task FROM tasks'

#update
update_task = 'UPDATE tasks SET task = ? WHERE id = ?'

#delete
delete_task = 'DELETE FROM tasks WHERE id =?'