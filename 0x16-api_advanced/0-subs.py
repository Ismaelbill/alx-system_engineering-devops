#!/usr/bin/python3
""" How many subs? """

import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and
    returns the number of subscribers """

    url = 'https://www.reddit.com'
    headers = {'User-Agent': 'Edge 127'}
    r = requests.get('{}/r/{}/about.json'.format(url, subreddit),
                     allow_redirects=False, headers=headers)
    if r.status_code == 200:
        return (r.json()['data']['subscribers'])
    return 0
