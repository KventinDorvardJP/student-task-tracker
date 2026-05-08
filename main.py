import os

def display_menu():
    while True:
        os.system("cls")
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


if __name__ == "__main__":
    display_menu()