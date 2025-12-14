"""
Day 04 — Loops, NumPy Basics & Vector Algebra
--------------------------------------------
Focus:
- Python loops vs NumPy arrays
- Vectorized operations
- Basic vector algebra
"""

import numpy as np


def python_loop_sum(data: list[int]) -> int:
    """Sum values using plain Python loop."""
    total = 0
    for x in data:
        total += x
    return total


def numpy_vector_sum(data: np.ndarray) -> int:
    """Sum values using NumPy vectorized operation."""
    return np.sum(data)


def vector_operations(vec1: np.ndarray, vec2: np.ndarray) -> None:
    """Demonstrate basic vector algebra."""
    print("\nVector Operations:")
    print("Vector 1:", vec1)
    print("Vector 2:", vec2)

    print("Addition      :", vec1 + vec2)
    print("Subtraction   :", vec1 - vec2)
    print("Dot Product   :", np.dot(vec1, vec2))
    print("Magnitude v1  :", np.linalg.norm(vec1))
    print("Magnitude v2  :", np.linalg.norm(vec2))


if __name__ == "__main__":
    # Sample dataset
    python_data = [1, 2, 3, 4, 5]
    numpy_data = np.array(python_data)

    print("Python loop sum :", python_loop_sum(python_data))
    print("NumPy vector sum:", numpy_vector_sum(numpy_data))

    # Vectors for algebra
    v1 = np.array([2, 4, 6])
    v2 = np.array([1, 3, 5])

    vector_operations(v1, v2)
