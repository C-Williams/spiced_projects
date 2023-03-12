# Text Classification Model

### This project is a text prediction model, built to tell 5 different artists apart.

Libraries used include:

* pandas
* Regex
* BeautifulSoup
* pickle
* scikit-learn
* requests

This project had quite a few different challenges: 

Namely, two separate websites were scraped, Wikipedia and lyrics.com. BeautifulSoup and regex were used to quickly and efficiently capture data from specific points on each page. In addition a large, nested function was created in order to automatically scrape the websites with the smallest amount of user input as possible. I had never created such a large function and it was an interesting challenge to make sure that everything interacted in the inteded ways.

This model is not meant to be incredibly accurate. For me, this project was more about how to scrape the web for data and how to turn this scraping into a function for repeated use. 

Ideas to improve the model include:
1. More specific and individualized text cleaning.
2. A more robust base classification model.
3. The inclusion of more artists to help widen the model's scope.

# How to use

```python 
predictor.py <any song lyric>
```

```python 
predictor.py -h
```
- Get a helpful guide to the program.
