#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Querying Reddit API, and returns all
    hot articles for a given subreddit."""

    url = "https://api.reddit.com/r/{}/hot".json.format(subreddit)
    headers = {'User-Agent': 'sisi'}
    arg1 = {"limit": 100, "after": after}
    resp = requests.get(url, params=arg1, headers=headers)
    list_a = resp.json().get('data', {}).get('children', None)
    pagination = resp.json().get('data', {}).get('after', None)
    if pagination is not None:
        if list_a:
            for item in list_a:
                hot_list.append(item.get("data").get("title"))
        if pagination is not None:
            recurse(subreddit, hot_list, pagination)
        return hot_list
    else:
        return None


def recurse(subreddit, hot_list=[], after=""):
    """ Function recurse """
    user_agent = {'User-agent': 'comels'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url,
                       headers=user_agent,
                       allow_redirects=False,
                       params={'after': after})
    if req.status_code == 404:
        return None

    hot = req.json()['data']
    after = hot['after']

    for result in hot['children']:
        hot_list.append(result['data']['title'])

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
