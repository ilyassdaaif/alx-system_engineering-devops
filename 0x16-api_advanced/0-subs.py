#!/usr/bin/python3
""" Exporting csv files"""
import csv
import sys
import requests
import importlib

def number_of_subscribers(subreddit):
    """Read reddit API and return tuple of subreddit name and number of subscribers"""
    client_id = 'tKJcpTovj-_4-TG3GNgN-g'
    client_secret = 'mNsV-ywKh8LD8lkNh8tP0UuSj4Lk6g'
    user_agent = 'ilyass-daaif/1.0 by /u/ilyass-daaif'
    headers = {'User-Agent': user_agent}
    url = f'https://oauth.reddit.com/r/{subreddit}/about'
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        data = response.json()['data']
        return (subreddit, data['subscribers'])
    else:
        return (subreddit, 0)

def export_to_csv(data, filename):
    """Export data to a CSV file"""
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Subreddit', 'Subscribers']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow({'Subreddit': row[0], 'Subscribers': row[1]})

if __name__ == '__main__':
    module_name = sys.argv[1]  # Assuming the script name is passed as an argument
    module = importlib.import_module(module_name)
    number_of_subscribers = module.number_of_subscribers
