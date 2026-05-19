import os

TASKS = []

def display_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Student Task Tracker\n\n")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Save tasks")
        print("6. Load tasks")
        print("7. Exit")
        
        user_input = input("Choose a menu: ")
        if user_input == "7":
            print("Thank you for using Student Task Tracker")
            break
        elif user_input == "1":
            add_task()
        elif user_input == "2":
            list_tasks()
        elif user_input == "3":
            mark_task_done()
        elif user_input == "4":
            delete_task()

def add_task():
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
    wait = input("Press Enter to continue...")

def list_tasks():
    print("Here you can see all your tasks.")
    for index, task in enumerate(TASKS):
        print(f"{index + 1}. {task['title']} - {task['subject']} - Due: {task['due_date']} - Status: {task['status']}")
        wait = input("Press Enter to continue...")

def mark_task_done():
    list_tasks()
    try:
        task_index = int(input("Enter the number of the task you want to mark as done: ")) - 1
        if 0 <= task_index < len(TASKS):
            TASKS[task_index]['status'] = "done"
            print("Task marked as done!")
            wait = input("Press Enter to continue...")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    list_tasks()
    try:
        task_index = int(input("Enter the number of the task you want to delete: ")) - 1
        if 0 <= task_index < len(TASKS):
            del TASKS[task_index]
            print("Task deleted successfully!")
            wait = input("Press Enter to continue...")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    display_menu()