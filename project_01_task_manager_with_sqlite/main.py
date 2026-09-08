from database import create_task, delete_task, display_all_tasks, display_a_task, filter_task, update_task

options = """
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
            case 1:
                title : str = input("Enter the task title: ")
                description : str | None = input("Enter the task description (optional): ") or None
                status : str = input("Enter the task status: ")
                priority : str = input("Enter the task priority: ")
                created_at : str = input("Enter the task creation date: ")
                create_task(title, description, status, priority, created_at)
            case 2: display_all_tasks()
            case 3: display_a_task(input("Enter the task ID: "))
            case 4:
                id = input("Enter Id of task: ")
                field = input("Enter field name: ").lower()
                change = input("Enter changes: ")
                update_task(id, field, change)
            case 5: delete_task(input("Enter task id: "))
            case 6: filter_task(input("Enter priority to filter tasks: "))
            case 7: running = False


if __name__ == "__main__":
    main()