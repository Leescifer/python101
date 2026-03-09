import json
import os 

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

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
                "Add"
            case "2":
                "View"
            case "3":
                "update" 
            case "4":
                "delete" 
            case "5":
                "good bye!"    
                break    
            case _:
                print("Invalid option.\n")

if __name__ == "__main__":
    main()
