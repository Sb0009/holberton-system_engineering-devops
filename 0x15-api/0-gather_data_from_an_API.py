#!/usr/bin/python3
"""" Python script that, using this REST API,
for a given employee ID, returns information """

import requests
from sys import argv


if __name__ == "__main__":
    userId = int(argv[1])
    user = ('https://jsonplaceholder.typicode.com/users/{}'.format(userId))
    todo = ('{}/todos/'.format(user))
    json_user = requests.get(user).json()
    json_todo = requests.get(todo).json()
    completed_tasks = []

    for task in json_todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(json_user.get('name'), len(completed_tasks), len(json_todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
