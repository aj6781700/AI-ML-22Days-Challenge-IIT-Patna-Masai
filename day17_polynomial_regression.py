"""
Day 17 — Polynomial Regression (Non-linear ML Model)
----------------------------------------------------
Goal:
Predict salary trend with experience, using Polynomial Features
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# Dataset (Experience vs Salary)
X = np.array([1, 2, 3, 5, 7, 10, 12]).reshape(-1, 1)
y = np.array([25000, 30000, 35000, 45000, 55000, 70000, 90000])

# Polynomial Features (degree = 2 → quadratic curve)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_poly, y)

print("\nMODEL TRAINED SUCCESSFULLY!")
print("Intercept :", model.intercept_)
print("Coefficients :", model.coef_)

# Predict Example
exp = 8
exp_poly = poly.transform([[exp]])
pred_salary = model.predict(exp_poly)[0]

print("\nPrediction:")
print("Experience =", exp, "years => Salary approx", int(pred_salary), "INR")


# Visualization
plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X_poly), label="Polynomial Fit", linewidth=3)
plt.title("Polynomial Regression (Salary vs Experience)")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (INR)")
plt.legend()
plt.show()
