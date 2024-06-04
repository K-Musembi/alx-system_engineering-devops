#!/usr/bin/python3
"""recursively return hot titles"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursive function"""
    headers = {'User-Agent': 'MyRedditApp/1.0'}
    if after:
        q_strings = {'limit': 100, 'after': after}
    else:
        q_strings = {'limit': 100}
    with requests.Session() as session:
        response = session.request(
                method='GET',
                url='https://www.reddit.com/r/{subreddit}/hot.json',
                headers=headers, q_strings=q_strings)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        rec = data['data']['after']
        if rec:
            recurse(subreddit, hot_list, rec)

        return hot_list
    else:
        return None
