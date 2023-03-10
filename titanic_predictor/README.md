# Titanic Logistical Regression Model

### This project was used to make submission to this [Kaggle Competition](https://www.kaggle.com/competitions/titanic).

Libraries used include:

* pandas
* matplotlib
* seaborn
* scikit-learn
* numpy

Data was first read in and then cleaned. This involved accounting for Nan data in a variety of ways: filling with the median, filling with the mode, and dropping an unnecessary column. After cleaning the data, seaborn and matplotlib were used to visualize the data in order to prepare my thoughts for building a logistic regression model.

The final product was submitted to Kaggle and though it only earned % 76 accuracy, I learned a lot through the process.

Ideas to improve the model include:
1. Using a more robust regression model
2. Researching actual passenger ages
3. Investigating if Cabin, specifically which side of the ship a passenger was located, effected survival

I fear, in the end, because this involved human choices in a crisis, a better predicition is beyond the scope of this simple project.