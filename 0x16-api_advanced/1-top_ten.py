#!/usr/bin/python3
"""first ten hot posts"""

import requests


def top_ten(subreddit):
    """print first 10 hot posts"""
    headers = {'User-Agent': 'MyRedditApp/1.0'}
    response = requests.get(
            f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10',
            headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print("None")
