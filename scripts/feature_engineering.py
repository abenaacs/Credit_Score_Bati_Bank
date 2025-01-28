import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from xverse.transformer import WOE
from pathlib import Path
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

# Paths to data
RAW_DATA_PATH = Path("./data/raw/data.csv")
OUTPUT_DATA_PATH = Path("./data/processed/processed_data.csv")


# Load dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logging.info(f"Loaded data with shape: {data.shape}")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise


# Create aggregate features
def create_aggregate_features(data):
    logging.info("Creating aggregate features...")
    aggregate_features = (
        data.groupby("AccountId")
        .agg(
            Total_Transaction_Amount=("Amount", "sum"),
            Average_Transaction_Amount=("Amount", "mean"),
            Transaction_Count=("Amount", "count"),
            Std_Transaction_Amount=("Amount", "std"),
        )
        .reset_index()
    )
    data = data.merge(aggregate_features, on="AccountId", how="left")
    return data


# Extract temporal features
def extract_temporal_features(data):
    logging.info("Extracting temporal features...")
    data["TransactionStartTime"] = pd.to_datetime(
        data["TransactionStartTime"], errors="coerce"
    )
    data["Transaction_Hour"] = data["TransactionStartTime"].dt.hour
    data["Transaction_Day"] = data["TransactionStartTime"].dt.day
    data["Transaction_Month"] = data["TransactionStartTime"].dt.month
    data["Transaction_Year"] = data["TransactionStartTime"].dt.year
    return data


# Encode categorical variables
def encode_categorical_features(data, categorical_columns):
    logging.info("Encoding categorical variables...")
    le = LabelEncoder()
    for col in categorical_columns:
        data[col] = data[col].astype(str)
        data[col] = le.fit_transform(data[col])
    return data


# Handle missing values
def handle_missing_values(data):
    logging.info("Handling missing values...")
    for col in data.columns:
        if data[col].isnull().sum() > 0:
            if data[col].dtype in ["float64", "int64"]:
                data[col].fillna(data[col].mean(), inplace=True)
            else:
                data[col].fillna("Unknown", inplace=True)
    return data


# Normalize numerical features
def normalize_features(data, numerical_columns):
    logging.info("Normalizing numerical features...")
    scaler = MinMaxScaler()
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])
    return data


# Calculate WoE/IV
def calculate_woe_iv(data, target_column, selected_columns):
    logging.info("Calculating Weight of Evidence (WoE) and Information Value (IV)...")
    woe_transformer = WOE()
    data_woe = woe_transformer.fit_transform(
        data[selected_columns], data[target_column]
    )
    iv_values = woe_transformer.woe_values
    logging.info(f"IV values: {iv_values}")
    return data_woe


# Main pipeline
def feature_engineering_pipeline():
    # Step 1: Load data
    data = load_data(RAW_DATA_PATH)

    # Step 2: Create aggregate features
    data = create_aggregate_features(data)

    # Step 3: Extract temporal features
    data = extract_temporal_features(data)

    # Step 4: Encode categorical features
    categorical_columns = [
        "CurrencyCode",
        "CountryCode",
        "ProviderId",
        "ProductCategory",
        "ChannelId",
    ]
    data = encode_categorical_features(data, categorical_columns)

    # Step 5: Handle missing values
    data = handle_missing_values(data)

    # Step 6: Normalize numerical features
    numerical_columns = [
        "Total_Transaction_Amount",
        "Average_Transaction_Amount",
        "Transaction_Count",
        "Std_Transaction_Amount",
    ]
    data = normalize_features(data, numerical_columns)

    # Step 7: Calculate WoE/IV
    target_column = "FraudResult"
    selected_columns = ["ProductCategory", "ChannelId"]
    data_woe = calculate_woe_iv(data, target_column, selected_columns)

    # Step 8: Save processed data
    data.to_csv(OUTPUT_DATA_PATH, index=False)
    logging.info(f"Processed data saved to: {OUTPUT_DATA_PATH}")


if __name__ == "__main__":
    feature_engineering_pipeline()
