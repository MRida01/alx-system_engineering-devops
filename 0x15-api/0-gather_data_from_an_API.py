#!/usr/bin/python3
"""
Using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
url = "https://jsonplaceholder.typicode.com/"

employee_id = sys.argv[1]
user = requests.get(url + "users/{}".format(employee_id)).json()

params = {"userId": employee_id}
todos = requests.get(url + "todos", params).json()

completed = [t.get("title") for t in todos if t.get("completed") is True]

print("Employee {} is done with tasks({}/{}):".format(
user.get("name"), len(completed), len(todos)))

[print("\t {}".format(complete)) for complete in completed]
