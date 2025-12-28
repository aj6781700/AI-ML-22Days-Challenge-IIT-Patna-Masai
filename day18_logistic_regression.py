"""
Day 18 — Logistic Regression (Classification Start)
---------------------------------------------------
Goal:
Predict whether salary is above 50,000 INR based on experience (0/1 output)
"""

import numpy as np
from sklearn.linear_model import LogisticRegression

# Experience (in years)
X = np.array([[1], [3], [5], [6], [7], [10], [12]])

# Salary above 50000? (Target: 1 = Yes, 0 = No)
y = np.array([0, 0, 0, 0, 1, 1, 1])

# Train model
model = LogisticRegression()
model.fit(X, y)

print("\nMODEL TRAINED SUCCESSFULLY!")

# Prediction Example
exp = 8
pred = model.predict([[exp]])[0]
prob = model.predict_proba([[exp]])[0][1]  # probability of class '1'

print("\nPrediction:")
print("Experience =", exp, "years")
print("Is salary likely above 50,000? =>", "YES" if pred == 1 else "NO")
print("Confidence Score =", round(prob * 100, 2), "%")
