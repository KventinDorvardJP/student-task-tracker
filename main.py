import os

TASKS = []

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
        print("5. Save tasks")
        print("6. Load tasks")
        print("7. Exit")
        
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
            case "7":
                print("Thank you for using Student Task Tracker")
                break
            case _:
                print("Invalid option. Please try again.")

def wait_for_enter():
    input("Press Enter to continue...")

def add_task():
    clear_console()
    print("Here you can add tasks.")
    task_title = input("Enter task title: ")
    task_subject = input("Enter task's subject: ")
    task_due_date = input("Enter task's due date (in yyyy-mm-dd format): ")
    task_status = "todo"
    task = {
        "title": task_title,
        "subject": task_subject,
        "due_date": task_due_date,
        "status": task_status
    }
    TASKS.append(task)
    print("Task added successfully!")
    wait_for_enter()

def list_tasks():
    print("Here you can see all your tasks.")
    if len(TASKS) == 0:
        print("No tasks found.")
    else:
        for index, task in enumerate(TASKS):
            print(f"{index + 1}. {task['title']} - {task['subject']} - Due: {task['due_date']} - Status: {task['status']}")

def display_tasks():
    clear_console()
    list_tasks()
    wait_for_enter()

def mark_task_done():
    clear_console()
    list_tasks()
    try:
        task_index = int(input("Enter the number of the task you want to mark as done: ")) - 1
        if 0 <= task_index < len(TASKS):
            TASKS[task_index]['status'] = "done"
            print("Task marked as done!")
            wait_for_enter()
        else:
            print("Invalid task number.")
            wait_for_enter()
    except ValueError:
        print("Please enter a valid number.")
        wait_for_enter()

def delete_task():
    clear_console()
    list_tasks()
    try:
        task_index = int(input("Enter the number of the task you want to delete: ")) - 1
        if 0 <= task_index < len(TASKS):
            del TASKS[task_index]
            print("Task deleted successfully!")
            wait_for_enter()
        else:
            print("Invalid task number.")
            wait_for_enter()
    except ValueError:
        print("Please enter a valid number.")
        wait_for_enter()

if __name__ == "__main__":
    display_menu()