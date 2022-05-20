#!/usr/bin/python3
"""Task 0 0x15. API"""
import json
import requests


if __name__ == "__main__":
    """Main Function"""
    url1 = 'https://jsonplaceholder.typicode.com/todos'
    url2 = 'https://jsonplaceholder.typicode.com/users'
    r1 = requests.get(url1)
    r2 = requests.get(url2)

    todo_name = r2.json()
    todo_list = r1.json()

    dict_user = {}

    for i in range(1, 10):
        NAME = todo_name[i].get('name')
        list_task = []
        for j in todo_list:
            if j.get('userId') == i:
                new = {}
                new['username'] = NAME
                new['task'] = j.get('title')
                new['completed'] = j.get('completed')
                list_task.append(new)
        dict_user[i] = list_task

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(dict_user, f)
