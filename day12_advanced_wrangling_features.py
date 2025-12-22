"""
Day 12 — Advanced Data Wrangling & Feature Preparation
-----------------------------------------------------
Focus:
- Feature transformation
- Feature creation
- Binning & categorization
- Feature selection
- Final ML-ready dataset
"""

import pandas as pd
import numpy as np


def create_clean_dataset() -> pd.DataFrame:
    """Clean dataset coming from Day 11 output."""
    data = {
        "Age": [22, 25, 30, 35, 40, 45],
        "Salary": [25000, 30000, 40000, 50000, 60000, 75000],
        "Experience": [1, 2, 5, 7, 10, 15],
        "Department": ["IT", "IT", "HR", "HR", "Management", "Management"]
    }
    return pd.DataFrame(data)


def advanced_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    print("Input Dataset:\n", df, "\n")

    # 🔹 Feature 1: Log transformation (salary skew handling)
    df["Log_Salary"] = np.log(df["Salary"])

    # 🔹 Feature 2: Experience Level (binning)
    df["Experience_Level"] = pd.cut(
        df["Experience"],
        bins=[0, 3, 8, 20],
        labels=["Junior", "Mid", "Senior"]
    )

    # 🔹 Feature 3: Salary Category
    df["Salary_Category"] = pd.cut(
        df["Salary"],
        bins=[0, 35000, 60000, 100000],
        labels=["Low", "Medium", "High"]
    )

    # 🔹 Encode categorical features
    df_encoded = pd.get_dummies(
        df,
        columns=["Department", "Experience_Level", "Salary_Category"],
        drop_first=True
    )

    # 🔹 Feature selection (drop raw columns not needed for ML)
    df_final = df_encoded.drop(columns=["Salary"])

    return df_final


if __name__ == "__main__":
    df = create_clean_dataset()
    df_ml_ready = advanced_feature_engineering(df)

    print("Final ML-Ready Dataset:\n", df_ml_ready) 