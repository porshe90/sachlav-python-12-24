
tasks = []


def display_menu():
    print("\nTask Manager")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Mark a Task as Completed")
    print("4. Delete a Task")
    print("5. Exit")


def add_task():
    task_description = input("Enter the task description: ").strip()
    if task_description:
        tasks.append({"description": task_description, "completed": False})
        print("Task added successfully.")
    else:
        print("Error: Task description cannot be empty.")


def view_tasks():
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, 1):
        status = "(Completed)" if task["completed"] else "(Pending)"
        print(f"{index}. {task['description']} {status}")


def mark_completed():
    try:
        view_tasks()
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print(f"Task {task_index + 1} marked as completed.")
        else:
            print("Error: Task number out of range.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def delete_task():
    try:
        view_tasks()
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            print(f"Task '{deleted_task['description']}' deleted successfully.")
        else:
            print("Error: Task number out of range.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")


def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_completed()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Error: Invalid choice. Please select a valid option.")
        except ValueError:
            print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()