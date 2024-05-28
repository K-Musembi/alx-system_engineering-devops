#!/usr/bin/python3
"""Fetch data using REST API"""

import json
import requests


response = requests.get(f"https://jsonplaceholder.typicode.com/todos")

users_list = requests.get(f"https://jsonplaceholder.typicode.com/users")

users = users_list.json()
lst = response.json()

all_tasks = {}
for user in users:
    emp_id = user["id"]
    name = user["name"]
    username = user["username"]

    data = []
    for obj in lst:
        new_lst = {}
        if obj["userId"] == emp_id:
            status = obj["completed"]
            task = obj["title"]
            new_lst.update(
                {"username": username, "task": task, "completed": status})
            data.append(new_lst)

    all_tasks.update({str(emp_id): data})

filename = "todo_all_employees.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(all_tasks, file)


def main():
    pass


if __name__ == '__main__':
    main()
