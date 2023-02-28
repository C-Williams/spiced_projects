# spiced_projects

This repo contains all of my projects that were built as part of the Data 
Science course at the Spiced Academy in Berlin.

Projects include:

1. An animated scatterplot detailing world fertility rates vs. life 
expectancy throughout the 20th Century as well as tracking population.

2. A model predicting one's survival chance if they were aboard the 
Titanic using ticket price, passenger class, sex, and age, as well as 
feature engineering with a column transformer pipeline to build a logistic 
regression model.

3. A linear regression model which predicts how many bikes will be rented 
each day for a given year in Washington D.C. The model is built using 
XGBoost regression.

4. A language prediction model which scrapes a lyric website to collect 
lyrics of 5 artists, collects and studies the collections, then, in a 
command line interface, allows a user to input a line of text and the 
model attempts to predict which artist wrote the lyric.

5. Week 5 utilized AWS to host and work with data in the cloud. 
Unfortunately, I cannot afford to pay for the EC2 machine to stay running, 
and therefore, this project is shut down for the moment.

6. A docker pipeline which, when built and run, will set up containers 
that scrape a reddit page, collect the data in a MongoDB, tranfer those 
JSON files into a PostgresDB where the text of every post is analyzed 
using Vader Sentiment Analysis, and then the titles of each post and the 
sentiment of each post is sent to a Slackbot which posts automatically 
when the Docker-Compose is run.

- NOTE: I understand that this process is convoluted and not efficient, 
the extra steps were part of the learning process with Spiced Academy.

7. A time series forecast, which attempts to predict temperature. Steps 
include creating trend, seasonal, remainders, lags, and finally running 
linear regression to develop a prediction. Included is a pip installable 
function which can be used to fill in missing, or incorrect data. See: 
https://pypi.org/project/fill-dt-data/ for more info.

8. IN PROGRESS: A Markov Chain project which tracks fake customer movement 
data inside fake grocery stores.

