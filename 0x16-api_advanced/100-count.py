#!/usr/bin/python3
"""Count word modeule"""
from collections import Counter
import re
import requests


def count_words(subreddit, word_list):
    """
    Recursively queries the Reddit API to count occurrences of keywords in
    the titles of hot articles for a given subreddit. Prints sorted results.
    """
    def fetch_posts(subreddit, after=None):
        """
        Fetches posts from the Reddit API, handles pagination, and returns
        the titles of the posts.
        """
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
        params = {'after': after} if after else {}

        try:
            response = requests.get(url,
                                    headers=headers,
                                    params=params,
                                    timeout=10)
            if response.status_code == 200:
                data = response.json()
                posts = data.get('data', {}).get('children', [])
                after = data.get('data', {}).get('after', None)
                titles = [
                    post.get('data', {}).get('title', '')
                    for post in posts
                    ]

                return titles, after
            else:
                return [], None
        except requests.RequestException:
            return [], None

    def count_keywords(titles, word_list):
        """
        Counts the occurrences of keywords in the titles.
        """
        word_count = Counter()
        word_list = [word.lower() for word in word_list]
        for title in titles:
            words = re.findall(r'\b\w+\b', title.lower())
            for word in words:
                if word in word_list:
                    word_count[word] += 1
        return word_count

    def print_results(word_count):
        """
        print the result
        """
        if not word_count:
            return
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word} {count}")

    def recurse(subreddit, word_list, hot_list, after=None):
        titles, new_after = fetch_posts(subreddit, after)
        if titles:
            hot_list.extend(titles)
            if new_after:
                recurse(subreddit, word_list, hot_list, new_after)
            else:
                word_count = count_keywords(hot_list, word_list)
                print_results(word_count)
        else:
            print_results(count_keywords(hot_list, word_list))

    recurse(subreddit, word_list, [])
