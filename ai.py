# House Price Prediction Project
# Name:harsimar singh
# Roll No: 25bcy10230
#these module needs to be imported to work with ml
import pandas as pd
import matplotlib.pyplot as plt# it will plot our data
from sklearn.model_selection import train_test_split#these are used for ml purpose i just imported them
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression#will be used for regression model
area=[100,131,321,435,241,432]#this is a sample data size of only 6 houses to use it get your locality info and get much more data as model will require much more to train efficiently
bedrooms=[1,4,2,2,1,4]
age=[10,21,13,3,21,11]
price=[12,43,21,21,11,34]
data={'age':age,'bedrooms':bedrooms,'area':area,'price':price}
d=pd.DataFrame(data)
x=d[['area','bedrooms','age']]
y=d['price']
xtotrain,xtotest,ytotrain,ytotest=train_test_split(x,y,test_size=0.5)
# i am using linear regression to predict house prices
model=LinearRegression()
model.fit(xtotrain,ytotrain)
prediction=model.predict(xtotest)
accuracy=r2_score(ytotest,prediction)
results = pd.DataFrame({'actual value':ytotest.values,'predicted price)': prediction.round(2)})
error = abs(ytotest.values-prediction).mean()
print('this is the error that happened in the price',error)
plt.figure()
plt.scatter(ytotest,prediction)
plt.plot([ytotest.min(),ytotest.max()],[ytotest.min(),ytotest.max()])
plt.xlabel('actual price')
plt.ylabel('prediction of price')
plt.title('house price predicted')
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig('result.png')



