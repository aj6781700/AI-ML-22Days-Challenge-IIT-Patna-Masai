"""
Day 09 — Pandas, Data Handling & Exploratory Data Analysis (EDA)
---------------------------------------------------------------
Focus:
- Loading data into Pandas
- Understanding dataset structure
- Descriptive statistics
- Filtering & selection
- Preparing data for ML
"""

import pandas as pd


def create_dataset() -> pd.DataFrame:
    """
    Create a sample dataset similar to real-world tabular data.
    """
    data = {
        "Age": [22, 25, 30, 35, 40, 28, 33, 45],
        "Salary": [25000, 30000, 40000, 50000, 60000, 32000, 48000, 75000],
        "Experience": [1, 2, 5, 7, 10, 3, 6, 15],
        "Department": ["IT", "IT", "HR", "HR", "Management", "IT", "HR", "Management"]
    }
    return pd.DataFrame(data)


def basic_eda(df: pd.DataFrame) -> None:
    """Perform basic exploratory data analysis."""
    print("Dataset Preview:\n", df.head(), "\n")

    print("Dataset Info:")
    print(df.info(), "\n")

    print("Descriptive Statistics:")
    print(df.describe(), "\n")


def filter_high_salary(df: pd.DataFrame) -> None:
    """Filter employees with high salary."""
    high_salary = df[df["Salary"] > 40000]
    print("Employees with Salary > 40000:\n", high_salary, "\n")


if __name__ == "__main__":
    df = create_dataset()

    basic_eda(df)
    filter_high_salary(df)
