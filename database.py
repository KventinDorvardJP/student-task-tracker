import sqlite3
from contextlib import closing

def initialize_database():
    with closing(sqlite3.connect('tasks.db')) as conn:
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    due_date TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            """)

def add_task(title, subject, due_date):
    with closing(sqlite3.connect('tasks.db')) as conn:
        with conn:
            conn.execute("INSERT INTO tasks (title, subject, due_date, status) VALUES (?, ?, ?, ?)", [title, subject, due_date, 'todo'])

def get_tasks():
    with closing(sqlite3.connect('tasks.db')) as conn:
        tasks = conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()

    return tasks

def mark_task_done(task_id):
    with closing(sqlite3.connect('tasks.db')) as conn:
        with conn:
            status_row = conn.execute("SELECT status FROM tasks WHERE id = ?", [task_id]).fetchone()
            if status_row is None:
                response = "Task not found."
            elif status_row[0] == "done":
                response = "Task is already marked as done."
            else:
                conn.execute("UPDATE tasks SET status = 'done' WHERE id = ?", [task_id])
                response = "Task marked as done successfully!"
    
    return response

def delete_task(task_id):
    with closing(sqlite3.connect('tasks.db')) as conn:
        with conn:
            cursor = conn.execute("DELETE FROM tasks WHERE id = ?", [task_id])

            if cursor.rowcount == 0:
                response = "Task not found."
            else:
                response = "Task deleted successfully!"
    return response