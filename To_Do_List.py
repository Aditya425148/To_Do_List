import json

# File to store tasks
TODO_FILE = 'todo_list.json'

# Load tasks from file
def load_tasks():
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    print(f"Task '{task}' added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show!")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{i}. {task['task']} - [{status}]")
    print()

# Mark a task as complete
def complete_task(tasks):
    if not tasks:
        print("No tasks to mark as complete!")
        return
    
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as complete: "))
    
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_num - 1]['task']}' marked as complete!")
    else:
        print("Invalid task number!")

# Delete a task
def delete_task(tasks):
    if not tasks:
        print("No tasks to delete!")
        return
    
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    
    if 1 <= task_num <= len(tasks):
        deleted_task = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task['task']}' deleted successfully!")
    else:
        print("Invalid task number!")

# Main menu
def menu():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Thank you")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
