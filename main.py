import os
import database

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
    task_title = input("Enter task title: ")
    task_subject = input("Enter task's subject: ")
    task_due_date = input("Enter task's due date (in yyyy-mm-dd format): ")
    database.add_task(task_title, task_subject, task_due_date)
    print("Task added successfully!")
    wait_for_enter()

def list_tasks():
    print("Here you can see all your tasks.")
    tasks = database.get_tasks()
    if len(tasks) == 0:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task[1]} - {task[2]} - Due: {task[3]} - Status: {task[4]}")

    return tasks

def display_tasks():
    clear_console()
    list_tasks()
    wait_for_enter()

def mark_task_done():
    clear_console()
    tasks = list_tasks()
    try:
        task_number = int(input("Enter the number of the task you want to mark as done: ")) 
        if task_number < 1 or task_number > len(tasks):
            print("Please enter a valid number.")
            wait_for_enter()
            return
        selected_task = tasks[task_number - 1]
        task_id = selected_task[0]
        response = database.mark_task_done(task_id)
        print(response)
        wait_for_enter()
    except ValueError:
        print("Please enter a valid number.")
        wait_for_enter()

def delete_task():
    clear_console()
    tasks = list_tasks()
    try:
        task_number = int(input("Enter the number of the task you want to delete: "))
        if task_number < 1 or task_number > len(tasks):
            print("Please enter a valid number.")
            wait_for_enter()
            return
        selected_task = tasks[task_number - 1]
        task_id = selected_task[0]
        response = database.delete_task(task_id)
        print(response)
        wait_for_enter()
    except ValueError:
        print("Please enter a valid number.")
        wait_for_enter()

if __name__ == "__main__":
    database.initialize_database()
    display_menu()