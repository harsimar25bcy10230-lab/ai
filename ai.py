# House Price Prediction Project
# Name:harsimar singh
# Roll No: 25bcy10230
#these module needs to be imported to work with ml
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
area=[100,131,321,435,241,432]# you can edit this or modify these data based on the house prices in your locality or state
bedrooms=[1,4,2,2,1,4]
age=[10,21,13,3,21,11]
price=[12,43,21,21,11,34]
data={'age':age,'bedrooms':bedrooms,'area':area,'price':price}
d=pd.dataframe(data)
x=d[['area','bedroom','age']]
y=d[['price']]
xtotrain,xtotest,ytotrain,ytotest=traintest(x,y,testsize=0.2)
# i am using linear regression to predict house prices
model=linearregression()
model.fit(xtotrain,ytotrain)
predection=model.predict(xtotest)
accuracy=r2_score(ytotest,predection)
results = pd.DataFrame({'actual value':ytotest.values,'predicted price)': prediction.round(2)})
error = abs(ytotest.values-prediction).mean()
print('this is the error':error)
plt.figure()
plt.scatter(ytotest,prediction)
plt.plot([ytotest.min(),ytotest.max()],[ytotest.min(),ytotest.max()])
plt.xlabel('actual price')
plt.ylabel('prediction of price')
plt.title('house price predicted')
plt.grid(True,alpha=0.3)
plt.tight_layout()
plt.savefig('result.png')



