#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests
import praw

def number_of_subscribers(subreddit):
    client_id = '9b_iNIXVqR3LHiDfopTMEw'
    client_secret = 'snZ94VtQ7wH1IUPRlB4oiaKtnSeYKw'
    user_agent = 'ilyass/1.0 by /u/ilyass daaif'
    reddit = praw.Reddit(client_id=client_id,
                         client_secret=client_secret,
                         user_agent=user_agent)
    
    try:
        subreddit_info = reddit.subreddit(subreddit)
        return subreddit_info.subscribers
    except Exception as e:
        print(f"Error: {e}")
        return 0
