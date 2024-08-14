#!/usr/bin/python3
""" Top Ten
"""

import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit
    """
    base_url = "https://www.reddit.com"

    headers = {'Accept': 'application/json',
               'User-Agent': 'My User Agent 1.0'}
    r = requests.get('{}/r/{}/.json?\
                      sort=top&limit=10'.format(base_url, subreddit),
                     headers=headers, allow_redirects=False)

    if r.status_code == 200:
        for post in r.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
