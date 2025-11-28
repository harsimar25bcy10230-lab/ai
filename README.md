name: harsimar singh
roll no:25bcy10230
title:house prediction through ml
my project is about using ml to predict the price of house on few past dataset related to house like rooms,area etc.

the libraries i used:
panda
matplotlib
r2_score-to measure accuracy
linear regression
train_test_split-to divide data

i created a small dataset manually.
Each entry contains:
area (sq. ft.)
bedrooms
age of the house
price

How the Program Works

I store the sample values into lists and then convert them DataFrame.
I separate the DataFrame into:
Features(X) = area, bedrooms, age
Target(y) = price
I split the dataset into training set and a testing set
I train a Linear Regression model using the training data
model predicts house prices for the test data
I calculate:
R^2 score that is the accuracy of the model
Mean Absolute Error which is average difference between actual and predicted values
I plot a graph to visually compare predicted values with actual values
at the end the plot is saved in the project folder as result.png.


import the libraries i mentioned that are pandas, matplotlib  scikit-learn.
to run this program


note: you need a lot of data to train the model the output you see was obtained through housing data in san diego i shortened it in my code for demo purpose please get your mass locality data to use this model better. THANK YOU

output:
the program prints :
The model accuracy
The average prediction error
A comparisonon of actual vs predicted prices
output looks like:
<img width="989" height="590" alt="download" src="https://github.com/user-attachments/assets/9c47cac2-aa25-4165-a004-8e02ae8c8691" />

