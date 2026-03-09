import json
import os 

FILE_NAME = "tasks.json"

#Load tasks from tasks.json file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

#Save tasks in the json file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

#View tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nYour tasks: ")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")
    print()

#Add tasks
def add_tasks(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task Added\n")

#Complete tasks
def complete_tasks(tasks):
    view_tasks(tasks)
    try:
        number = int(input("Enter the task number to complete: "))
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Tasks marked as completed.\n")
    except:
        print("Invalid task number.\n")

#Delete tasks
def delete_tasks(tasks):
    view_tasks(tasks)
    try:
        number = int(input("Enter task number to delete"))
        tasks.pop(number - 1)
        save_tasks(tasks)
        print("Tasks deleted.\n")
    except:
        print("Invalid task number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("Task Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                view_tasks(tasks)
            case "2":
                add_tasks(tasks)
            case "3":
                complete_tasks(tasks)
            case "4":
                delete_tasks(tasks)
            case "5":
                print("Good bye!")
                break    
            case _:
                print("Invalid option.\n")

if __name__ == "__main__":
    main()
