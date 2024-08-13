#!/usr/bin/python3
"""
Script to query Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response_data = requests.get(url, headers={"User-Agent": "Mozilla/5.0"},
                                 allow_redirects=False)
    if response_data.status_code != 200:
        return 0
    else:
        data = response_data.json()
        subscribers = data['data']['subscribers']
        return subscribers
