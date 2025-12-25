"""
Day 15 — Linear Regression (First ML Model)
-------------------------------------------
Goal:
Predict Salary based on Experience using Linear Regression
"""

import numpy as np
from sklearn.linear_model import LinearRegression


# Experience (Years)
X = np.array([[1], [2], [3], [5], [7], [10], [12]])
# Salary (in Rupees)
y = np.array([25000, 30000, 35000, 45000, 55000, 70000, 85000])


# Create & Train Model
model = LinearRegression()
model.fit(X, y)


# Display Model Parameters
print("MODEL TRAINED SUCCESSFULLY!\n")
print("Slope (Coefficient)        :", model.coef_[0])
print("Intercept                  :", model.intercept_)
print("\nEquation: Salary = ", round(model.coef_[0], 2), "* Experience +", round(model.intercept_, 2))


# Prediction Example
exp = 8
pred_salary = model.predict([[exp]])
print("\nPredicted Salary for", exp, "years experience =>", int(pred_salary), "INR")

