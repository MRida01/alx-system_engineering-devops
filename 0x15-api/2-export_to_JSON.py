#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.

Script takes an employee ID as a command-line argument and exports
the corresponding user information and to-do list to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    # Get employee ID from command-line argument
    user_id = sys.argv[1]

    # Base URL for JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch to-do list for employee using provided employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Create a dictionary containing user and to-do list information
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # Write data to a JSON file with employee ID as the filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
