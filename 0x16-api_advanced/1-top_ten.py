#!/usr/bin/python3
"""top_ten module"""


import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts[:10]:
                    print(post.get('data', {}).get('title', ''))
            else:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)
