"""
credit_risk.py
---------------
This script calculates basic credit risk statistics, such as default rate and fraud rate.

Functions:
- calculate_default_rate: Computes the default rate based on the provided dataframe.
"""

import pandas as pd


def calculate_default_rate(df, fraud_column="FraudResult"):
    """
    Calculate the default rate from a dataset.

    Args:
        df (pd.DataFrame): The dataset containing fraud information.
        fraud_column (str): The column indicating fraud results.

    Returns:
        float: The default rate as a percentage.
    """
    total_transactions = len(df)
    total_defaults = df[fraud_column].sum()
    default_rate = total_defaults / total_transactions
    return default_rate


if __name__ == "__main__":
    df = pd.read_csv("data/raw_data.csv")
    print(f"Default Rate: {calculate_default_rate(df):.2%}")
