#!/usr/bin/python3
"""Fetch data using REST API"""

import json
import requests
import sys
import csv


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
    new_lst = []
    if obj["userId"] == emp_id:
        status = obj["completed"]
        title = obj["title"]
        new_lst = [str(emp_id), username, str(status), title]
        data.append(new_lst)

filename = "2.csv"

with open(filename, 'w', newline="") as file:
    writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)


def main():
    """Empty function"""
    pass


if __name__ == '__main__':
    main()
