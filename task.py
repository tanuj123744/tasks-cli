import sys
import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(title):
    tasks = load_tasks()
    tasks.append({"id": len(tasks) + 1, "title": title, "done": False})
    save_tasks(tasks)
    print(f"Added task: '{title}'")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        status = "[x]" if t["done"] else "[ ]"
        print(f"{t['id']}. {status} {t['title']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task.py [add <task_name> | list]")
    elif sys.argv[1] == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    else:
        print("Invalid command.")