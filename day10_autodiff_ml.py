"""
Day 10 — Automatic Differentiation (Auto-Diff) for ML
----------------------------------------------------
Focus:
- Numerical gradients (finite differences)
- Analytical gradients (chain rule)
- Gradient checking
"""

import numpy as np


def loss_function(w: float) -> float:
    """
    Simple loss: L(w) = (w^2 + 2w + 1)
    Minimum at w = -1
    """
    return w**2 + 2*w + 1


def numerical_gradient(f, w: float, eps: float = 1e-5) -> float:
    """Compute gradient using finite differences."""
    return (f(w + eps) - f(w - eps)) / (2 * eps)


def analytical_gradient(w: float) -> float:
    """Compute gradient analytically using calculus."""
    # d/dw (w^2 + 2w + 1) = 2w + 2
    return 2*w + 2


def gradient_check(w: float) -> None:
    num_grad = numerical_gradient(loss_function, w)
    ana_grad = analytical_gradient(w)

    print("At w =", w)
    print("Numerical Gradient :", round(num_grad, 6))
    print("Analytical Gradient:", round(ana_grad, 6))
    print("Difference         :", round(abs(num_grad - ana_grad), 8))


if __name__ == "__main__":
    # Test at different points
    for w in [-3.0, 0.0, 2.0]:
        gradient_check(w)
        print("-" * 40)
