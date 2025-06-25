TASKS = "Tasks.txt"

def addTask():
    task_to_be_added = input("Enter a new task to add : ").strip()
    if task_to_be_added:
        with open(TASKS, 'a') as tasks:
            tasks.write(task_to_be_added + "\n")
        print("Task added Successfully !")
    else:
        print("Task can not be empty !")

def viewTasks():
    print('\n')
    print('------------ Your Tasks ------------')
    try:
        with open(TASKS, 'r') as tasks: 
            availableTasks = tasks.readlines()
            if availableTasks:
                for i, tasks in enumerate(availableTasks, 1):
                    print(f"{i}. {tasks.strip()} \n")
            else:
                print("No task found ! \n")
    except FileNotFoundError:
        print("Tasks File not found ! please start by adding a task \n")

def removeTask():
    try:
        with open(TASKS, "r") as tasks:
            availableTasks = tasks.readlines()

        if not availableTasks:
            print("No tasks to remove.\n")
            return

        viewTasks()
        number = int(input("Enter the task number to remove: "))

        if 1 <= number <= len(availableTasks):
            removed = availableTasks.pop(number - 1)
            with open(TASKS, "w") as tasks:
                for task in availableTasks:
                    tasks.write(task)
            print(f"Removed task: {removed.strip()}\n")
        else:
            print("Invalid task number.\n")
    except (ValueError, FileNotFoundError):
        print("Error: Unable to remove task.\n")

def main():
    while True:
        print('\n')
        print("===== To-Do List Menu =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            viewTasks()
        elif choice == "2":
            addTask()
        elif choice == "3":
            removeTask()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
