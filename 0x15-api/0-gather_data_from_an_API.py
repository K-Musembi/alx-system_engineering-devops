#!/usr/bin/python3
"""Fetch data using REST API
"""

import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit()

    try:
        emp_id = int(sys.argv[1])
    except Exception as e:
        sys.exit()

    response = requests.get(f"https://jsonplaceholder.typicode.com/todos")

    users_list = requests.get(f"https://jsonplaceholder.typicode.com/users")

    users = users_list.json()
    for user in users:
        if user["id"] == emp_id:
            name = user["name"]

    lst = response.json()

    total_tasks = 0
    done_tasks = []

    for obj in lst:
        if obj["userId"] == emp_id:
            total_tasks += 1
            if obj["completed"]:
                done_tasks.append(obj["title"])

    total_done = len(done_tasks)

    print(f"Employee {name} is done with tasks({total_done}/{total_tasks}):")
    for task in done_tasks:
        print(f"  {task}")
