""" 
This file is effectively a Slackbot that gets data from the Postgres container
and posts it onto a Slack Channel. Note: changing the WEBHOOK_URL will change
which channel the post is sent to.
"""

# Importing necessary libraries
# Specify what to install in requirements.txt
import os

from sqlalchemy import create_engine
from sqlalchemy import text

import time

import requests

# Creating a connection to Postgres
engine = create_engine('postgresql://postgres:postgres@post_reddit:5432/redditdb', echo=True)

# Sleeping in order to line up processes in the pipeline.
time.sleep(10)

# Using SQLAlchemy to get ALL (fetchall) the text from the Postgres container.
with engine.connect() as connection:
    text = connection.execute(text("SELECT title, sentiment_of_full_text FROM reddits"))
    text = text.fetchall()

# Setting up variables for use in the while loop.
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

counter = 0
runtime = 0

# CHANGE RUNTIME TO ANY DESIRED NUMBER TO RUN LONGER.
while runtime <= 1:

    # Run a for loop for each item in the text, this creates posts which are then sent
    # to Slack.
    for item in text:

        # Assigns a picture to post on Slack for each rating.
        if item[1] == ':fire:POSITIVE:fire:':
            image_url = "https://ih1.redbubble.net/image.4333354507.1138/st,small,507x507-pad,600x600,f8f8f8.jpg"
        elif item[1] == ':grey_question:NEUTRAL:grey_question:':
            image_url = "https://i.ebayimg.com/images/g/czsAAOSw6MBgH5af/s-l1600.jpg"
        elif item[1] == ':shit:NEGATIVE:shit:':
            image_url = "https://www.etsy.com/img/10711773/r/il/37fb1e/4516398359/il_1588xN.4516398359_mvkf.jpg"
        
        # This if statement insures that the title text is only printed once.
        if counter == 0:
            data = {'blocks': [{
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*This week's TOP 10 DnD threads and their sentiments are*:\n{item[0]}\n{item[1]}"
                        },
                    "accessory": {
                        "type": "image",
                        "image_url": f"{image_url}",
                        "alt_text": "alt text for image"
                        }
                    }]
                }
            counter += 1
            requests.post(url=WEBHOOK_URL, json = data)
        else:
            data = {'blocks': [{
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"{item[0]}\n{item[1]}"
                        },
                    "accessory": {
                        "type": "image",
                        "image_url": f"{image_url}",
                        "alt_text": "alt text for image"
                        }    
                    }]
                }
            requests.post(url=WEBHOOK_URL, json = data)
            counter += 1

    # Reset the counter outside of the for loop so the title will print again
    counter = 0

    # CHANGE THIS SLEEP NUMBER IN ORDER TO DELAY POSTS ON SLACK
    time.sleep(10)

    runtime += 1
