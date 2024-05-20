#!/usr/bin/python3
"""
Using REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys

def main():
    """
    Main function to fetch and display the TODO list progress for a given employee ID.
    """
    url = "https://jsonplaceholder.typicode.com/"

    # Check if the employee ID is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        return

    employee_id = sys.argv[1]

    # Fetch user information
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Fetch TODO list for the user
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params=params).json()

    # List of completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)
    ))

    # Print each completed task title
    for complete in completed:
        print("\t {}".format(complete))

if __name__ == "__main__":
    main()
