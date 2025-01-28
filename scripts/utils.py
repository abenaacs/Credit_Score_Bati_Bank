import os
import logging
import pandas as pd
from sklearn.metrics import classification_report, roc_auc_score

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)


def load_csv(file_path):
    """Load a CSV file and return a DataFrame."""
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Loaded data from {file_path} with shape {df.shape}")
        return df
    except Exception as e:
        logging.error(f"Error reading {file_path}: {e}")
        raise


def save_csv(df, file_path):
    """Save a DataFrame to a CSV file."""
    try:
        df.to_csv(file_path, index=False)
        logging.info(f"Data saved to {file_path}")
    except Exception as e:
        logging.error(f"Error saving data to {file_path}: {e}")
        raise


def print_classification_metrics(y_true, y_pred, y_proba=None):
    """Print classification metrics and ROC-AUC if applicable."""
    print("\nClassification Report:\n", classification_report(y_true, y_pred))
    if y_proba is not None:
        roc_auc = roc_auc_score(y_true, y_proba)
        print(f"ROC-AUC Score: {roc_auc:.3f}")
