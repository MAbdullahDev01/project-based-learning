import sqlite3

con = sqlite3.connect("task_manager.db")
cur = con.cursor()

# Create the tasks table
#cur.execute("CREATE TABLE tasks(id, title, description, status, priority, created_at)")

def create_task(title: str, description: str | None, status: str, priority: str, created_at: str) -> None:
    id = cur.execute("SELECT id FROM tasks ORDER BY id DESC LIMIT 1").fetchone()
    if id is None:
        id = 1
    else:
        id = int(id[0]) + 1
    try:
        command = f"""
        INSERT INTO tasks VALUES
        ("{id}", "{title}", "{description}", "{status}", "{priority}", "{created_at}")
        """
        cur.execute(command)
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        con.commit()

        # for debugging purposes, print the current state of the tasks table
        # res = cur.execute("SELECT * FROM tasks")
        # print(res.fetchall())

def display_all_tasks():
    res = cur.execute("SELECT * FROM tasks").fetchall()
    num_of_tasks : int = len(res)
    for task_num in range(num_of_tasks):
        print(f"ID: {res[task_num][0]}")
        print(f"Title: {res[task_num][1]}")
        print(f"Description: {"No description" if res[task_num][2] else res[task_num][2]}")
        print(f"Status: {res[task_num][3]}")
        print(f"Priority: {res[task_num][4]}")
        print(f"Create at: {res[task_num][5]}")
        print("=======================================================================")

def display_a_task(task_id : str):
    res = cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchall()
    if not res:
        print("Task not found.")
        return
    task = f"""
ID: {res[0][0]}
Title: {res[0][1]}
Description: {"No description" if res[0][2] else res[0][2]}
Status: {res[0][3]}
Priority: {res[0][4]}
Create at: {res[0][5]}
=======================================================================
"""
    print(task)

def update_task(id: str, field: str, change: str) -> None:
    allowed_fields = ["title", "description", "status", "priority"]
    if field not in allowed_fields:
        raise ValueError("Enter a valid field name")
    try:
        cur.execute(f"UPDATE tasks SET {field} = ? WHERE id = ?", (change, id))
    except sqlite3.Error as e:
        print(e)
    finally:
        con.commit()

def delete_task(id: str) -> None:
    if not id:
        raise ValueError("ID not given")
    try:
        cur.execute("DELETE FROM tasks WHERE id = ?", (id,))
    except sqlite3.Error as e:
        print(e)
    finally:
        con.commit()

def filter_task(priority: str):
    if not priority:
        raise ValueError("priority is not given")
    try:
        res = cur.execute("SELECT * FROM tasks WHERE priority = ?", (priority,)).fetchall()
    except sqlite3.Error as e:
        print(e)
    num_of_tasks : int = len(res)
    for task_num in range(num_of_tasks):
        print(f"ID: {res[task_num][0]}")
        print(f"Title: {res[task_num][1]}")
        print(f"Description: {"No description" if res[task_num][2] else res[task_num][2]}")
        print(f"Status: {res[task_num][3]}")
        print(f"Priority: {res[task_num][4]}")
        print(f"Create at: {res[task_num][5]}")
        print("=======================================================================")
    
if __name__ == "__main__":
    ...