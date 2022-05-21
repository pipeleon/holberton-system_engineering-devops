#!/usr/bin/python3
"""Task 0 0x16. API"""
import requests


def recurse(subreddit, hot_list=[]):
    """Function to get the subscribe number of a subreddit as parameter"""
    CLIENT_ID = "VKOXXLxu-8o42FtwhIuDIg"
    CLIENT_SECRET = "uyWfF2GV5aKDdQ7hkHfFBT85d4wCAQ"
    USERNAME = "El_Flaco_Leon"
    PASSWORD = "Holberton1234"

    c_a = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {
        'grant_type': 'password', 'username': USERNAME, 'password': PASSWORD}

    TOKEN_ACCESS_ENDPOINT = 'https://www.reddit.com/api/v1/access_token'
    response = requests.post(TOKEN_ACCESS_ENDPOINT, data=post_data, auth=c_a)
    if response.status_code == 200:
        token_id = response.json()['access_token']
    else:
        return recurse(subreddit, hot_list)

    headers_get = {
        'Authorization': 'Bearer ' + token_id
    }

    if len(hot_list) == 0:
        paramsA = {
            'limit': 100
        }
    else:
        paramsA = {
            'after': hot_list[-1].get('data').get('name'),
            'limit': 100
        }

    url = "https://oauth.reddit.com/r/{}/hot".format(subreddit)

    r = requests.get(url, headers=headers_get, params=paramsA)

    if not r.status_code == 200:
        return recurse(subreddit, hot_list)

    list_a = r.json().get('data').get('children')

    if len(list_a) == 100:
        for i in list_a:
            hot_list.append(i)
        return recurse(subreddit, hot_list)
    else:
        for i in list_a:
            hot_list.append(i)
        new = []
        for i in hot_list:
            new.append(i.get('data').get('title'))
        return new
