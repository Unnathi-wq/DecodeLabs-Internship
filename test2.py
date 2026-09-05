tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("Your task list is empty: []")
        else:
            print(f"List view: {tasks}")
            print("\nYour tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please enter 1, 2, or 3.")