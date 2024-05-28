#!/usr/bin/python3
"""Fetch data using REST API"""

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
    lst = response.json()
    for user in users:
        if user["id"] == emp_id:
            name = user["name"]
            username = user["username"]

    data = []

    for obj in lst:
        new_lst = {}
        if obj["userId"] == emp_id:
            status = obj["completed"]
            task = obj["title"]
            new_lst.update(
                {"task": task, "completed": status, "username": username})
            data.append(new_lst)

    emp_tasks = {str(emp_id): data}

    filename = "2.json"

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(emp_tasks, file)
