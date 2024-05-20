#!/usr/bin/python3
"""
Write a Python script that, using this REST API:
https://jsonplaceholder.typicode.com/

a) Employee ID
b) Information about his/her TODO list progress.
c) You must use urllib or requests module
d) The script must accept an integer as a parameter, which is the employee ID
e) Display employee TODO list progress in this exact format:

First line: Employee EMPLOYEE_NAME is done
with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):

Second and N next lines display the title of completed tasks: TASK_TITLE
(with 1 tabulation and 1 space before the TASK_TITLE)
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"

    try:
        user_response = requests.get(url + "users/{}".format(employee_id))
        user_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        sys.exit(1)

    user = user_response.json()

    try:
        todos_response = requests.get
        (url + "todos", params={"userId": employee_id})
        todos_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching TODO data: {e}")
        sys.exit(1)

    todos = todos_response.json()

    completed = [todo.get("title") for todo in todos if todo.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for title in completed:
        print("\t {}".format(title))
