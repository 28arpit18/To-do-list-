def main():
    todo_list = []
    
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.append(task)
            print(f"Added: '{task}'")
            
        elif choice == '2':
            print("\nYour Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
                
        elif choice == '3':
            # Show list before deleting
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                removed = todo_list.pop(task_num - 1)
                print(f"Removed: '{removed}'")
            except (ValueError, IndexError):
                print("Invalid number. Please try again.")
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-4.")

if __name__ == "__main__":
    main()
