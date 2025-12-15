"""
Day 05 — NumPy Power Tools & Numerical Optimization
--------------------------------------------------
Focus:
- Vectorized operations
- Boolean masking
- Broadcasting
- Performance-oriented numerical thinking
"""

import numpy as np
import time


def loop_square_sum(data: list[int]) -> int:
    """Compute sum of squares using Python loop."""
    total = 0
    for x in data:
        total += x * x
    return total


def numpy_square_sum(data: np.ndarray) -> int:
    """Compute sum of squares using NumPy vectorization."""
    return np.sum(data ** 2)


def boolean_masking_example(data: np.ndarray) -> np.ndarray:
    """Filter even numbers using boolean masking."""
    return data[data % 2 == 0]


def broadcasting_example(data: np.ndarray) -> np.ndarray:
    """Apply broadcasting to scale data."""
    return data * 1.5


if __name__ == "__main__":
    dataset = np.arange(1, 1000001)

    # Performance comparison
    start = time.time()
    loop_result = loop_square_sum(dataset.tolist())
    loop_time = time.time() - start

    start = time.time()
    numpy_result = numpy_square_sum(dataset)
    numpy_time = time.time() - start

    print("Loop result  :", loop_result)
    print("NumPy result :", numpy_result)
    print("\nExecution Time Comparison:")
    print("Python loop time :", round(loop_time, 4), "seconds")
    print("NumPy time       :", round(numpy_time, 4), "seconds")

    # NumPy power tools
    even_numbers = boolean_masking_example(dataset)
    scaled_data = broadcasting_example(dataset[:5])

    print("\nBoolean Masking (first 10 even numbers):", even_numbers[:10])
    print("Broadcasting Example (first 5 values):", scaled_data)
    print("Scaled Data (first 5 values):", scaled_data) 
    print("Original Data (first 5 values):", dataset[:5])
    print("Scaling Factor: 1.5")    
    