#!/usr/bin/python3
"""3-recurse modeule"""


import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API to return a list containing the titles.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        response = requests.get(url, headers=headers, params={'after': hot_list[-1] if hot_list else None}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                return hot_list if hot_list else None

            for post in posts:
                hot_list.append(post.get('data', {}).get('title', ''))

            after = data.get('data', {}).get('after', None)
            if after:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    except requests.RequestException:
        return None
