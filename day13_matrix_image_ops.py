"""
Day 13 — Matrix Algebra & Image Operations
-----------------------------------------
Focus:
- Matrix operations using NumPy
- Dot product & matrix multiplication
- Image as matrix concept
- Basic image transformations
"""

import numpy as np


def matrix_operations():
    A = np.array([[1, 2],
                  [3, 4]])

    B = np.array([[5, 6],
                  [7, 8]])

    print("Matrix A:\n", A)
    print("Matrix B:\n", B)

    print("\nAddition (A + B):\n", A + B)
    print("Subtraction (A - B):\n", A - B)
    print("Matrix Multiplication (A @ B):\n", A @ B)
    print("Transpose of A:\n", A.T)


def image_as_matrix():
    """
    Simulate a grayscale image as a matrix
    Pixel values range from 0 to 255
    """
    image = np.array([
        [0, 50, 100],
        [150, 200, 255],
        [30, 80, 130]
    ])

    print("\nOriginal Image Matrix:\n", image)

    # Brightness increase
    brighter = np.clip(image + 40, 0, 255)
    print("\nBrighter Image Matrix:\n", brighter)

    # Normalization (ML-friendly)
    normalized = image / 255.0
    print("\nNormalized Image Matrix:\n", normalized)


if __name__ == "__main__":
    matrix_operations()
    image_as_matrix()
