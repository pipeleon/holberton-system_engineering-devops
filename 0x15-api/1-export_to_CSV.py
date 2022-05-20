#!/usr/bin/python3
"""Task 1 0x15. API"""
import csv
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

    with open("{}.csv".format(sys.argv[1]), "w", encoding="utf-8") as f:
        all_task = []
        for i in todo_list:
            new = []
            new.append(str(sys.argv[1]))
            new.append(NAME)
            new.append(str(i.get('completed')))
            new.append(i.get('title'))
            all_task.append(new)
        w = csv.writer(f, quotechar="\"")
        w.writerows(all_task)
