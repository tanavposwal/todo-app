import os
import argparse

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks

def add_task():
    task = input("> ")
    with open(TASKS_FILE, "a") as file:
        file.write(task + "\n")
    print("added.")

def view_tasks():
    tasks = load_tasks()
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks available.")
    print()

def delete_task():
    view_tasks()
    task_num = int(input("id: ")) - 1
    try:
        with open(TASKS_FILE, "r") as file:
            lines = file.readlines()

        if 0 <= task_num < len(lines):
            with open(TASKS_FILE, "w") as file:
                for i, line in enumerate(lines):
                    if i != task_num:
                        file.write(line)
            print("deleted.")
        else:
            print("Error")
    except FileNotFoundError:
        print("Error")

def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List Command-Line Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Add Task
    parser_add = subparsers.add_parser("add", help="Add a new task")

    # View Tasks
    parser_view = subparsers.add_parser("show", help="View all tasks")

    # Delete Task
    parser_delete = subparsers.add_parser("del", help="Delete a task")

    args = parser.parse_args()

    if args.command == "add":
        add_task()
    elif args.command == "show":
        view_tasks()
    elif args.command == "del":
        delete_task()

if __name__ == "__main__":
    main()
