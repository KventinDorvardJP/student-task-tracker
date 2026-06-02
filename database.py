import sqlite3

def initialize_database():
    conn = sqlite3.connect('tasks.db')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def add_task(title, subject, due_date):
    conn = sqlite3.connect('tasks.db')
    conn.execute("INSERT INTO tasks (title, subject, due_date, status) VALUES (?, ?, ?, ?)", [title, subject, due_date, 'todo'])

    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect('tasks.db')
    tasks = conn.execute("SELECT * FROM tasks").fetchall()

    conn.commit()
    conn.close()
    return tasks

def mark_task_done(task_id):
    conn = sqlite3.connect('tasks.db')
    status_row = conn.execute("SELECT status FROM tasks WHERE id = ?", [task_id]).fetchone()
    if status_row is None:
        conn.close()
        response = "Task not found."
    elif status_row[0] == "done":
        conn.close()
        response = "Task is already marked as done."
    else:
        conn.execute("UPDATE tasks SET status = 'done' WHERE id = ?", [task_id])
        conn.commit()
        conn.close()
        response = "Task marked as done successfully!"
    
    return response

def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.execute("DELETE FROM tasks WHERE id = ?", [task_id])

    if cursor.rowcount == 0:
        response = "Task not found."
    else:
        response = "Task deleted successfully!"
    conn.commit()
    conn.close()
    return response