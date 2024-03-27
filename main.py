import manager



def opening_message():
    print("Welcome to the Taks Application!")
    print("You can use the following commands:")
    print("1. Create a new task:")
    print('   Example: "create task -d "description" -t "date" status -s "ststus"')
    print("2. View a specific task by its ID:")
    print('   Example: "view task -id "id"')
    print("3. Delete a note by its ID:")
    print('   Example: "delete task -id "id"')
    print("4. Exit the application:")
    print('   Example: "exit"')
    print("Please enter your command or type 'exit' to quit.")



def main():
    opening_message()
    task_manager = manager.TaskManager()

    while True:
        user_input = input("Enter your command: ").split()
        
        if user_input[0] == "exit":
            print("Exiting the application...")
            break
        
        elif user_input[0] == "create" and user_input[1] == "task":
            if "-d" in user_input and "-t" in user_input:
                description_index = user_input.index("-d") + 1
                date_index = user_input.index("-t") + 1
                description = user_input[description_index]
                date = user_input[date_index]
                id = task_manager.add_task(description, date)
                print(f"task created successfully. id is {id}")
            else:
                print("Invalid command. Please provide both title and content.")
        
        elif user_input[0] == "view" and user_input[1] == "task" and user_input[2] == "-id":
            try:
                note_id = int(user_input[3])
                print(task_manager.view_task(note_id))
            except (ValueError, IndexError, manager.InvalidId):
                print("Invalid command or note ID.")
        
        elif user_input[0] == "delete" and user_input[1] == "task" and user_input[2] == "-id":
            try:
                note_id = int(user_input[3])
                task_manager.remove_task(note_id)
                print(f"task with ID {note_id} deleted successfully.")
            except (ValueError, IndexError, manager.InvalidId) as e:
                print(e)

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
