#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the JSON format.
"https://jsonplaceholder.typicode.com/"

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ],
    "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ]}

File name must be: todo_all_employees.json
"""

import json
import requests


def fetch_user_data():
    """Fetch user information and to-do lists for all employees."""
    url = "https://jsonplaceholder.typicode.com/"

    try:
        users = requests.get(url + "users")
        users.raise_for_status()
        users = users.json()
    except requests.RequestException as e:
        print(f"Error fetching users: {e}")
        return {}

    data_to_export = {}

    for user in users:
        user_id = user["id"]

        try:
            todo_response = requests.get(url + f"todos?userId={user_id}")
            todo_response.raise_for_status()
            todo_list = todo_response.json()
        except requests.RequestException as e:
            print(f"Error fetching todos for user {user_id}: {e}")
            continue

        data_to_export[user_id] = []

        for todo in todo_list:
            task_info = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }

            data_to_export[user_id].append(task_info)

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
