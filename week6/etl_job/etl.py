""" 
This file takes data from a MongoDB container, transforms it,
analyzes it using Vader Sentiment Analysis and puts it into a 
separate Postgresql container.
"""

# Importing necessary libraries
# Specify what to install in requirements.txt
import pymongo

import time

from sqlalchemy import create_engine
from sqlalchemy import text

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Establish the sentiment analyzer
s  = SentimentIntensityAnalyzer()

# Establish a connection to the MongoDB container
mongo_client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use within the MongoDB container
db = mongo_client.reddit

# Get the texts from with the posts table in the MongoDB container
docs = db.posts.find(limit=10)

# Sleep in order to make sure processes happen in the correct order.
time.sleep(5)

# Create a connection to the Postgresql container
pg = create_engine('postgresql://postgres:postgres@post_reddit:5432/redditdb', echo=True)
pg_client_connect = pg.connect()

# SQL text which will be used later to create a table within the 
# Postgres container.
create_table = """
CREATE TABLE reddits (
    id TEXT,
    title TEXT,
    sentiment_of_full_text TEXT
);
"""

# SQLAlchemy that executes the text from above and commits/saves
# the changes.
pg_client_connect.execute(text(create_table))
pg_client_connect.commit()


# A loop through all of the MongoDB docs which cleans, analyzes
# and saves each doc into a row on the create Postgres DB.
for doc in docs:

    # Collecting variables and cleaning
    id = doc['_id']
    title = doc['title'].replace("'","").replace('"',"")
    selftext = doc['selftext'].replace("'","").replace('"',"")

    # Using the instantiated Vader SA to score the full text of
    # each post.
    selftext_sentiment = s.polarity_scores(selftext)
    selftext_score = selftext_sentiment['compound']
    
    # Using markdown syntax to fill in values based on Vader's
    # scoring.
    if selftext_score >= 0.05:
        sentiment_of_full_text = ":fire:POSITIVE:fire:"
    elif selftext_score > -0.05 and selftext_score < 0.05:
        sentiment_of_full_text = ":grey_question:NEUTRAL:grey_question:"
    else:
        sentiment_of_full_text = ":shit:NEGATIVE:shit:"
    
    # A SQL query that inserts the newly found/created data into
    # the table on Postgres.
    query = f"INSERT INTO reddits (id, title, sentiment_of_full_text) VALUES ('{id}','{title}','{sentiment_of_full_text}');"
    
    # Same as above.
    pg_client_connect.execute(text(query))
    pg_client_connect.commit()
