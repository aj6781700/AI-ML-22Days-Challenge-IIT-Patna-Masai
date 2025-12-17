"""
Day 07 — Statistics for Machine Learning
----------------------------------------
Focus:
- Mean, Median, Variance, Standard Deviation
- Data distribution understanding
- Outliers & spread
- Statistical intuition for ML models
"""

import numpy as np


def basic_statistics(data: np.ndarray) -> None:
    """Print basic statistical measures."""
    print("Basic Statistics:")
    print("Count :", len(data))
    print("Mean  :", round(np.mean(data), 4))
    print("Median:", round(np.median(data), 4))
    print("Variance:", round(np.var(data), 4))
    print("Std Dev :", round(np.std(data), 4))


def distribution_check(data: np.ndarray) -> None:
    """Check data range and outliers."""
    print("\nDistribution Insights:")
    print("Min value:", np.min(data))
    print("Max value:", np.max(data))
    print("Range    :", np.max(data) - np.min(data))

    # Simple outlier detection using 2*std rule
    mean = np.mean(data)
    std = np.std(data)
    outliers = data[(data < mean - 2 * std) | (data > mean + 2 * std)]
    print("Potential outliers:", outliers if len(outliers) > 0 else "None")


if __name__ == "__main__":
    # Sample dataset (simulating real-world numeric data)
    dataset = np.array([12, 15, 14, 16, 18, 21, 19, 17, 16, 120])

    print("Dataset:", dataset)
    print()

    basic_statistics(dataset)
    distribution_check(dataset)
    difference = np.max(dataset) - np.min(dataset)
    print("\nDifference between max and min:", difference)  
    statement = "A large difference may indicate high variability in data."
    print(statement)
    
