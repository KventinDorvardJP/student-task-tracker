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
    return conn.execute("SELECT * FROM tasks").fetchall()