#!/usr/bin/python3
""" Exporting csv files """
import requests


def top_ten(subreddit):
    url = f"ttps://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "CustomUserAgent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            for post in data['data']['childern']:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)

if __name__ == "__main__":
    top_ten("programming")
