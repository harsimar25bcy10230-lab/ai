House Price Prediction Project
this is a project where i try to guess house prices using some machine learning. i am trying to predict how much a place will cost based on its size, how many rooms it has, and how old it is.
output is:
<img width="989" height="590" alt="download" src="https://github.com/user-attachments/assets/9c47cac2-aa25-4165-a004-8e02ae8c8691" />

 What We Used
i mainly used the python programming language and a few libraries:

:pandas: i used it to organize our data (area, bedrooms, age, and price) into something called a dataframe.

matplotlib.pyplot (plt): this helps us draw graphs. i used it to plot our results and see how well our guesses matched the actual prices.

(sklearn): this is where the  "machine learning" happen.

train_test_split: helps us split our small dataset into two parts: one part for the model to learn from and one part for us to test how good it is (testing).
The Data We Hadour data is tiny right now, just a few sample houses:area: the size of the house.bedrooms: number of bedrooms.age: how old the house is.price: the actual price. 
How The Code Worksdata work:
i put the sample data into a pandas dataframe.splitting: we separate the data into features (area, bedrooms, age) and the target (price). then i split it into training and testing sets.training: we tell the linear regression model to learn from the training data: i use the trained model to guess the prices for the houses in the testing data.checking:we calculate the accuracy using $r^2$ score.i calculated the average error to see how far off our predictions were from the actual prices.seeing
the results: 
then i create a scatter plot. if the dots fall close to the straight line then the predictions were good.

this project helps people guess the price of house. it is based on linear regression . ml modules are used relating it to into to ai ml course.
