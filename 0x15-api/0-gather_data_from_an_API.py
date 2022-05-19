#!/usr/bin/python3
"""Task 0 0x15. API"""
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

    E = name[0].get('name')
    N = 0
    for i in todo_list:
        if i.get('completed'):
            N += 1
    T = len(todo_list)

    print("Employee {} is done with tasks({}/{}):".format(E, N, T))
    for i in todo_list:
        if i.get('completed'):
            print("\t ", i.get('title'))
