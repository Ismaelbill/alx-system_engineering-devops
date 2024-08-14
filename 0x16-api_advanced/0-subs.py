#!/usr/bin/python3
""" How many subs? """

import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and
    returns the number of subscribers """

    url = 'https://www.reddit.com'
    r = requests.get('{}/r/{}/about/.json'.format(url, subreddit), allow_redirects=False)
    if r.status_code == 200:
        return (r.json()['data']['subscribers'])
    return 0
