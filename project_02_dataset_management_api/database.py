from config import settings
import sqlite3

con = sqlite3.connect("dataset.db")
cur = con.cursor()

if not settings.IS_DB_CREATED:
    cur.execute("CREATE TABLE datasets(id, name, description, created_at)")


def create_dataset(name: str, description: str | None, created_at: str) -> None:
    try:
        id = cur.execute("SELECT id FROM datasets ORDER BY id DESC LIMIT 1").fetchone()
    except:
        id = None
    
    if id is None:
        id = 1
    else:
        id = int(id[0]) + 1
    try:
        command = f"""
        INSERT INTO tasks VALUES
        ("{id}", "{name}", "{description}", "{created_at}")
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
    res = cur.execute("SELECT * FROM datasets").fetchall()
    num_of_datasets : int = len(res)
    for task_num in range(num_of_datasets):
        print(f"ID: {res[task_num][0]}")
        print(f"Name: {res[task_num][1]}")
        print(f"Description: {"No description" if res[task_num][2] else res[task_num][2]}")
        print(f"Created at: {res[task_num][3]}")
        print("=======================================================================")

def display_a_dataset(dataset_id : str):
    res = cur.execute("SELECT * FROM datasets WHERE id = ?", (dataset_id,)).fetchall()
    if not res:
        print("Dataset not found.")
        return
    dataset = f"""
ID: {res[0][0]}
Name: {res[0][1]}
Description: {"No description" if res[0][2] else res[0][2]}
Created at: {res[0][3]}
=======================================================================
"""
    print(dataset)

def delete_task(id: str) -> None:
    if not id:
        raise ValueError("ID not given")
    try:
        cur.execute("DELETE FROM datasets WHERE id = ?", (id,))
    except sqlite3.Error as e:
        print(e)
    finally:
        con.commit()

if __name__ == "__main__":
    ...