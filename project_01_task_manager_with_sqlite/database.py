import sqlite3

con = sqlite3.connect("task_manager.db")

cur = con.cursor()

cur.execute("CREATE TABLE tasks(id, title, description, status, priority, created_at)")

def create_task():

    cur.execute("""
    INSERT INTO tasks VALUES
    ({}{}{})
""")