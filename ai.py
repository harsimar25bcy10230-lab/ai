# HARSIMAR SINGH
# 25BCY10230
# AI POWERED ATTENDANCE PREDICTOR PROJECT
# Python + Machine Learning Mini Project

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("WELCOME TO ATTENDANCE PREDICTOR BY HARSIMAR SINGH")
print("Loading old student data for training...")
print("-"*60)

# my old data (10 students from previous years)
data = {
    'total_classes': [10, 15, 21, 25, 30, 35, 40, 45, 50, 54],
    'attended': [8, 12, 16, 20, 27, 30, 35, 39, 45, 48],
    'percentage': [80.0, 80.0, 80.0, 80.0, 90.0, 85.7, 87.5, 86.6, 90.0, 87.2]
}

df = pd.DataFrame(data)
print(df)
print("\nTraining the model on above data... wait a second")

# training part
X = df[['total_classes', 'attended']]   # features
y = df['percentage']                    # what we want to predict

model = LinearRegression()
model.fit(X, y)

accuracy = model.score(X, y) * 100
print(f"Model trained! Accuracy = {accuracy:.2f}% on old data")
print("-"*60)

# now taking input from user
while True:
    try:
        print("\nNow enter your current attendance")
        total = int(input("Total classes happened till today: "))
        went = int(input("How many you attended: "))
        
        if went > total or total <= 0 or went < 0:
            print("Bhai galat number daala tune, dobara daal")
            continue
        break
    except:
        print("Only numbers allowed! Try again")

# prediction
predicted_perc = model.predict([[total, went]])[0]

print("\n" + "="*60)
print(f"  YOUR PREDICTED FINAL ATTENDANCE → {predicted_perc:.2f}% ")
print("="*60)

if predicted_perc >= 75:
    print("    ARAM SE, YOU ARE SAFE!")
    print("    Keep going like this ")
else:
    print("    DANGER ZONE BHAI!!!")
    required = int(np.ceil(0.75 * total - went))  # kitne aur classes chahiye
    if required <= 0:
        print("    Thoda improve kar le bhai,")
    else:
        print(f"    Agle {required} classes mein ek bhi mat chhodna!")
        print("    Warna detention lag jayega ")

print("="*60)

# graph bana dete hain (syllabus mein matplotlib hai isliye)
plt.figure(figsize=(10,6))
plt.scatter(df['attended'], df['percentage'], color='blue', s=80, label='Old Students')
plt.scatter(went, predicted_perc, color='red', s=250, marker='*', label='You Right Now')
plt.plot(df['attended'], model.predict(df[['total_classes','attended']]), color='green')
plt.axhline(y=75, color='red', linestyle='--', linewidth=3, label='75% Line (Danger)')
plt.title("Attendance Predictor Graph - By Harsimar Singh", fontsize=14)
plt.xlabel("Classes Attended")
plt.ylabel("Percentage")
plt.legend()
plt.grid()
plt.show()

print("\nThank you Sir/Madam for checking my project!")
print("I have written and understood each and every line ")
