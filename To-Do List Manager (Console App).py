tasks = []

def show_menu():
    print("\n----- TO-DO LIST MANAGER -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "completed": False})
    print("✔ Task added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nYour Tasks:")
    for i, t in enumerate(tasks):
        status = "✔ Completed" if t["completed"] else "⏳ Pending"
        print(f"{i+1}. {t['task']} - {status}")

def complete_task():
    view_tasks()
    if not tasks:
        return

    choice = int(input("\nEnter task number to mark as completed: "))
    if 1 <= choice <= len(tasks):
        tasks[choice-1]["completed"] = True
        print("✔ Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    if not tasks:
        return

    choice = int(input("\nEnter task number to delete: "))
    if 1 <= choice <= len(tasks):
        tasks.pop(choice-1)
        print("🗑 Task deleted!")
    else:
        print("Invalid task number.")

def todo_manager():
    while True:
        show_menu()
        option = input("\nSelect an option: ")

        if option == "1":
            add_task()
        elif option == "2":
            view_tasks()
        elif option == "3":
            complete_task()
        elif option == "4":
            delete_task()
        elif option == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Try again.")

todo_manager()
