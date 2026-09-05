tasks = []
while True:
    print("\n1. Add tasks")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose an option:")
    if choice == "1":
        #print("\n")
        task = input("enter a task:")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour tasks:")
        for task in tasks:
           print("-",task)
    elif choice == "3":
     print("Goodbye!")
    break
else:
   print("Invalid choice.")


