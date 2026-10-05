import sys


def display_menu():
    print("\n--- TO-DO LIST MANAGER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Added: '{new_task}'")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            view_tasks(tasks)
            if tasks:
                try:
                    task_num = int(
                        input("Enter task number to remove: ")
                    )
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed: '{removed}'")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()