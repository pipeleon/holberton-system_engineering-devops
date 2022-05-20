#!/usr/bin/python3
"""Task 0 0x15. API"""
import json
import requests
import sys


if __name__ == "__main__":
    """Main Function"""
    url1 = 'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    url2 = 'https://jsonplaceholder.typicode.com/users?id=' + sys.argv[1]
    r1 = requests.get(url1)
    r2 = requests.get(url2)

    name = r2.json()
    todo_list = r1.json()

    NAME = name[0].get('name')

    dict_user = {}
    list_task = []

    for i in todo_list:
        new = {}
        new['task'] = i.get('title')
        new['completed'] = i.get('completed')
        new['username'] = NAME
        list_task.append(new)

    dict_user[str(sys.argv[1])] = list_task

    with open("{}.json".format(sys.argv[1]), "w", encoding="utf-8") as f:
        json.dump(dict_user, f)
