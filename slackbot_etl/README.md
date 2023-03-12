# Sentiment Analysis Slackbot with an ETL Pipeline

### This project is part Slackbot, part Sentiment Analysis, part Docker Pipeline project

Libraries used include:

* pymongo
* sqlalchemy
* VaderSentimentAnalysis
* Docker composer and build files
* MongoDB
* PostgreSQL

This project was quite fun! I enjoyed this more data engineering project.

To complete the project, I made ample use of the docker-compose.yml file to build a few different Docker containers. 

When docker-compose build is run, 5 containers are built:
1. A Reddit web-scraper.
- Uses pymongo to scrape Reddit pages for titles and their respective text.
2. A MongoDB container.
- Stores the text and titles from scraped Reddit pages.
3. A container for running an ETL process.
- Takes the data from the MongoDB container and runs VaderSentimentAnalysis on it.
4. A PostgreSQL container.
- Stores the analyzed data.
5. A Slackbot container.
- Takes the data from the PostgreSQL container, establishes a connection with Slack and posts the information with some special formatting.

