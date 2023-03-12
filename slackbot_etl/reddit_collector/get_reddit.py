"""
This file connects to the Reddit API using OAuth and sends
specific text to a MongoDB container.
"""

# Importing necessary libraries
# Specify what to install in requirements.txt

import os
import requests
from requests.auth import HTTPBasicAuth
import pymongo

# Connecting to the MongoDB container
client = pymongo.MongoClient(host="mongodb", port=27017)
db = client.reddit

## Preparing Authentification info ##
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')
APP_ID = os.getenv('APP_ID')
SECRET = os.getenv('SECRET')

## Prepping to request a temporary token ##
basic_auth = HTTPBasicAuth(
    username = APP_ID,
    password = SECRET
)

GRANT_INFORMATION = dict(
    grant_type = "password",
    username = REDDIT_USERNAME,
    password = REDDIT_PASSWORD
)

headers = {
    'User-Agent': "Mozilla"
}

### Actually requesting the access token from the specified POST_URL

POST_URL = "https://www.reddit.com/api/v1/access_token"

access_post_response = requests.post(url=POST_URL, 
                                     headers=headers,
                                     data=GRANT_INFORMATION,
                                     auth = basic_auth
                                    ).json()

### ADDING TO HEADERS THE Authorization KEY, used in the later request

headers['Authorization'] = access_post_response.get('token_type') + ' ' + access_post_response.get('access_token')

## Send a get request to download most popular ('hot') subreddits title using the new headers.

topic = 'DnD'
URL = f"https://oauth.reddit.com/r/{topic}/hot"

response = requests.get(url=URL,
                        headers=headers
                        ).json()

# First print out full_response using pprint in order to decide exactly what you need.
full_response = response.get('data').get('children')

#pprint(full_response)

# Go through the full_response and save each title with the corresponding id and text
# to the MongoDB container

for post in full_response:
    id_ = post.get('data').get('id')
    title = post.get('data').get('title')
    selftext = post.get('data').get('selftext')
    db.posts.insert_one({'_id':id_,
                         'title':title,
                         'selftext':selftext})
