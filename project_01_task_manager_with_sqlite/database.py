from calendar import c
from operator import length_hint
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

if __name__ == "__main__":
    ...