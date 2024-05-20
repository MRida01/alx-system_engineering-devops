#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

Script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from JSONPlaceholder API.
Then prints the tasks completed by the employee.
"""

import requests
import sys


if __name__ == "__main__":
    # Base URL for JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get employee information using the provided employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get the to-do list for employee using the provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filter completed tasks and count them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the employee's name and number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks with indentations, one by one
    [print("\t {}".format(complete)) for complete in completed]
