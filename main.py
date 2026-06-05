import os
import database
from datetime import datetime

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def display_menu():
    while True:
        
        clear_console()
        print("Student Task Tracker\n\n")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        
        user_input = input("Choose a menu: ")
        match user_input:
            case "1":
                add_task()
            case "2":
                display_tasks()
            case "3":
                mark_task_done()
            case "4":
                delete_task()
            case "5":
                print("Thank you for using Student Task Tracker")
                break
            case _:
                print("Invalid option. Please try again.")
                wait_for_enter()

def wait_for_enter():
    input("Press Enter to continue...")  

def add_task():
    clear_console()
    print("Here you can add tasks.")
    while True:
        task_title = input("Enter task's title: ")
        if task_title == "":
            print("Task title cannot be empty!")
        else: 
            break
    while True:
        task_subject = input("Enter task's subject: ")
        if task_subject == "":
            print("Task subject cannot be empty!")
        else: 
            break
    while True:
        task_due_date = input("Enter task's due date (in yyyy-mm-dd format): ")
        if task_due_date == "":
            print("Due date cannot be empty!")
        else:
            try:
                # Check that the input is a real date in yyyy-mm-dd format.
                datetime.strptime(task_due_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Please enter a valid date in yyyy-mm-dd format.")
    database.add_task(task_title, task_subject, task_due_date)
    print("Task added successfully!")
    wait_for_enter()

def display_task_list(tasks):
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        clear_console()
        print("Here you can see all your tasks.")
        for index, task in enumerate(tasks):
            task_id, title, subject, due_date, status = task
            print(f"{index + 1}. {title} - {subject} - Due: {due_date} - Status: {status}")

def display_tasks():
    tasks = database.get_tasks()
    display_task_list(tasks)
    wait_for_enter()

def mark_task_done():
    task_id = get_task_id_from_user()
    if task_id is None:
        return
    response = database.mark_task_done(task_id)
    print(response)
    wait_for_enter()

def delete_task():
    task_id = get_task_id_from_user()
    if task_id is None:
        return
    response = database.delete_task(task_id)
    print(response)
    wait_for_enter()

def get_task_id_from_user():
    tasks = database.get_tasks()
    if len(tasks) == 0:
        print("No tasks found.")
        wait_for_enter()
        return None
    display_task_list(tasks)
    try:
        task_number = int(input("Enter the number of the task: "))
        if 1 <= task_number <= len(tasks):
            selected_task = tasks[task_number - 1]
            return selected_task[0]
        else:
            print("Please enter a valid number.")
            wait_for_enter()
            return None
    except ValueError:
        print("Please enter a valid number.")
        wait_for_enter()
        return None

if __name__ == "__main__":
    database.initialize_database()
    display_menu()