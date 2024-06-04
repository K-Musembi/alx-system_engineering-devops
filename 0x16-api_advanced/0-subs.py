#!/usr/bin/python3
"""request number of subreddit subscribers"""

import requests


def number_of_subscribers(subreddit):
    """return number of subscribers"""
    headers = {'User-Agent': 'MyRedditApp/1.0'}
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
