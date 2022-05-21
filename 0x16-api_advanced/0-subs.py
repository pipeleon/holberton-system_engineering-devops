#!/usr/bin/python3
"""Task 0 0x16. API"""
import requests


def number_of_subscribers(subreddit):
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

    headers_get = {
        'Authorization': 'Bearer ' + token_id
    }

    url = "https://oauth.reddit.com/r/{}/about".format(subreddit)

    r = requests.get(url, headers=headers_get)

    if r.status_code == 200:
        return r.json().get('data').get('subscribers')
    else:
        return 0
