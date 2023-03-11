# Bike Sharing Demand Prediction Model

### This project was used to make submission to this [Kaggle Competition](https://www.kaggle.com/competitions/bike-sharing-demand).

Libraries used include:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* XGBoost


This data was particularly interesting. First, a Datetime column was required, then it was necessary to search for both Nan values and 0 values which may not actually be 0 values.

Columns 'humidity' and 'windspeed' both had values of 0. After consulting weather reports and asking experts in gathering windpseed data, it is my opinion that all the data presented is accurate and no filling, or manipulation is required. However, to prove my opinion, in the lin_reg_practice file, I put my theory to the test and after finding RMSE scores for the data, I was proven correct.

After learning all I could about the data, I ran a series of transformations on the data including dropping columns and using a column transformer to one hot encode, create polynomial expansion, and bin certain features as well. However, while the final predictions that I submitted did not use these transformations, I found the process of learning how to implement them rewarding.

The final product was submitted to Kaggle and though it only earned an RMSE score of ~ 0.369. This score would have placed my model in the top 50 in the world. However, I believe machine has come a long way since the competition was held.

Ideas to improve the model include:
1. Treating weekends and weekdays separately.
2. Test out time-series forecasting
3. Perhaps try neural networks, though I suspect the gains would include trade-offs in compute time.
