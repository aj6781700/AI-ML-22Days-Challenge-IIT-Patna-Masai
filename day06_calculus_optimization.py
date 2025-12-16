"""
Day 06 — Calculus Intuition & Optimization for ML
------------------------------------------------
Focus:
- Function behavior
- Numerical derivative (slope)
- Gradient descent intuition
"""

import numpy as np


def function(x: float) -> float:
    """Simple quadratic function."""
    return (x - 4) ** 2 + 3


def numerical_derivative(f, x: float, h: float = 1e-5) -> float:
    """
    Compute numerical derivative using finite differences.
    """
    return (f(x + h) - f(x)) / h


def gradient_descent(start_x: float, learning_rate: float, steps: int) -> float:
    """
    Perform gradient descent to find function minimum.
    """
    x = start_x
    for _ in range(steps):
        grad = numerical_derivative(function, x)
        x -= learning_rate * grad
    return x


if __name__ == "__main__":
    x0 = 12.0
    lr = 0.1
    iterations = 40

    print("Starting point:", x0)
    print("Function value:", function(x0))

    derivative_at_x0 = numerical_derivative(function, x0)
    print("\nDerivative at start:", round(derivative_at_x0, 4))

    optimal_x = gradient_descent(x0, lr, iterations)

    print("\nAfter Gradient Descent:")
    print("Optimal x approx:", round(optimal_x, 4))
    print("Function value at optimal x:", round(function(optimal_x), 4))
