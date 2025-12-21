"""
Day 11 — Data Cleaning & Wrangling for Machine Learning
------------------------------------------------------
Focus:
- Handling missing values
- Removing duplicates
- Fixing inconsistent data
- Outlier detection
- Creating ML-ready clean dataset
"""

import pandas as pd
import numpy as np


def create_dirty_dataset() -> pd.DataFrame:
    """Simulate a real-world messy dataset."""
    data = {
        "Age": [22, 25, None, 35, 40, 25, None, 45],
        "Salary": [25000, 30000, 40000, None, 60000, 30000, 48000, 75000],
        "Experience": [1, 2, 5, 7, None, 2, 6, 15],
        "Department": ["IT", "IT", "HR", "HR", "Management", "IT", "HR", "Management"]
    }
    return pd.DataFrame(data)


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values using statistical methods."""
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
    df["Experience"] = df["Experience"].fillna(df["Experience"].median())
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    return df.drop_duplicates()


def detect_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """Detect salary outliers using mean ± 2*std rule."""
    mean_salary = df["Salary"].mean()
    std_salary = df["Salary"].std()

    outliers = df[
        (df["Salary"] < mean_salary - 2 * std_salary) |
        (df["Salary"] > mean_salary + 2 * std_salary)
    ]
    return outliers


if __name__ == "__main__":
    # Step 1: Create dirty data
    df_dirty = create_dirty_dataset()
    print("Original Dirty Dataset:\n", df_dirty, "\n")

    # Step 2: Handle missing values
    df_clean = handle_missing_values(df_dirty)

    # Step 3: Remove duplicates
    df_clean = remove_duplicates(df_clean)

    print("Cleaned Dataset:\n", df_clean, "\n")

    # Step 4: Detect outliers
    outliers = detect_outliers(df_clean)
    print("Detected Outliers:\n", outliers if not outliers.empty else "No outliers found")
