import sqlite3
from config import path_db
from db import queries

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_tasks_table)
    print('db connected!')
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_task, (task,))
    conn.commit()
    task_id = cursor.lastrowid
    print(f"Задача {task_id}")
    conn.close()
    return task_id

def upadte_task(task_id, new_task=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if new_task is not None:
        cursor.execute(queries.update_task, (new_task, task_id))
        
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_task,(task_id,))
    
    conn.commit()
    conn.close()

def get_tasks(filter_type=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if filter_type == 'all':
        cursor.execute(queries.select_tasks)
    elif filter_type == 'complted'
    cursor.execute(queries.select_tasks)
    tasks = cursor.fetchall()
    conn.close()
    return tasks