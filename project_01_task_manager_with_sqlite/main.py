options = """"
============================================
1. Create a task
2. List tasks
3. Get task
4. Update task
5. Delete task
6. Filter tasks
7. Exit
============================================
"""

def main() -> None:

    running : bool = True
    while running:
        print(options)
        option_chosen : int = int(input("Choose an option (1-7): "))
        match option_chosen:
            case 1: ... # TODO: Implement task creation
            case 2: ... # TODO: Implement getting all tasks
            case 3: ... # TODO: Implement getting a specific task
            case 4: ... # TODO: Implement updating a task
            case 5: ... # TODO: Implement deleting a task
            case 6: ... # TODO: Implement filtering tasks
            case 7: running = False


if __name__ == "__main__":
    main()