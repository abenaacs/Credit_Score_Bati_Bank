import pandas as pd


def calculate_default_rate(df, fraud_column="FraudResult"):
    total_transactions = len(df)
    total_defaults = df[fraud_column].sum()
    default_rate = total_defaults / total_transactions
    return default_rate


if __name__ == "__main__":
    df = pd.read_csv("data/raw_data.csv")
    print(f"Default Rate: {calculate_default_rate(df):.2%}")
