import os

# Filename to store tasks
TASKS_FILE = 'tasks.txt'

# Function to load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to show the list of tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

# Function to remove a task
def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as completed
def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the completed task: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] += " (Completed)"
            save_tasks(tasks)
            print(f"Task '{tasks[task_num - 1]}' marked as completed.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\n--- Task Management System ---")
        print("1. View tasks")
        print("2. Add new task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            complete_task(tasks)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
