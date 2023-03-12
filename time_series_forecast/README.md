# Time Series Forecast

### This project uses temperature data from over 100 years in Berlin to build a time-series forecasting model

Libraries used include:

* pandas
* numpy
* matplotlib 
* seaborn
* scikit-learn
* statsmodels

This project was a new and unique approach to predicting for me. The logic behind using a remainder to predict better is really interesting. The concept took a little to wrap my head around, but once I did, it opens the possibilities to make predictions given a very small amount of features, which is very cool.

In addition, in order to properly fill in missing data values, I created a pip installable function that can be used to fill in data in time series problems very well. See [here](https://pypi.org/project/fill-dt-data/) for more information.

As a part of this prediction I:
1. Used time data to track trends and seasonality
2. Used those to find the remainder
3. Used that remainded to better calculate further predictions.
