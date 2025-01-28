import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
from pathlib import Path
from utils import load_csv, save_csv  # Import utility functions

# Set up global plot settings
sns.set(style="whitegrid", palette="muted")
plt.rc("figure", figsize=(12, 6))

# Paths to data files
definitions_path = Path("./data/raw/Xente_Variable_Definitions.csv")
data_path = Path("./data/raw/data.csv")
visualizations_dir = Path("./visualizations")

# Ensure the visualizations directory exists
os.makedirs(visualizations_dir, exist_ok=True)


# Save plot to the visualizations folder
def save_plot(plot_name):
    """Save the current plot to the visualizations folder."""
    plot_path = visualizations_dir / f"{plot_name}.png"
    plt.savefig(plot_path, bbox_inches="tight")
    plt.close()
    print(f"Plot saved: {plot_path}")


# Display dataset overview
def dataset_overview(data, definitions):
    print("\nDataset Overview:")
    print(f"Number of rows: {data.shape[0]}")
    print(f"Number of columns: {data.shape[1]}")
    print("\nData Types:")
    print(data.dtypes)

    print("\nColumn Descriptions:")
    print(definitions)


# Display summary statistics
def display_summary_statistics(data):
    print("\nSummary Statistics:")
    print(data.describe())


# Handle missing values
def analyze_missing_values(data):
    print("\nMissing Values:")
    missing_values = data.isnull().sum()
    print(missing_values[missing_values > 0])
    msno.heatmap(data)
    plt.title("Missing Values Heatmap")
    save_plot("missing_values_heatmap")


# Distribution of numerical features
def plot_numerical_distributions(data, numerical_columns):
    for column in numerical_columns:
        sns.histplot(data[column], kde=True, bins=30, color="blue")
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        save_plot(f"numerical_distribution_{column}")


# Distribution of categorical features
def plot_categorical_distributions(data, categorical_columns):
    for column in categorical_columns:
        sns.countplot(
            y=data[column], order=data[column].value_counts().index, palette="viridis"
        )
        plt.title(f"Distribution of {column}")
        plt.xlabel("Count")
        plt.ylabel(column)
        save_plot(f"categorical_distribution_{column}")


# Correlation analysis
def correlation_analysis(data, numerical_columns):
    correlation_matrix = data[numerical_columns].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    save_plot("correlation_matrix")


# Outlier detection
def detect_outliers(data, numerical_columns):
    for column in numerical_columns:
        sns.boxplot(x=data[column], color="orange")
        plt.title(f"Boxplot for {column}")
        save_plot(f"outlier_detection_{column}")


# Main execution
if __name__ == "__main__":
    # Load datasets using the utility function
    definitions = load_csv(definitions_path)
    data = load_csv(data_path)

    if definitions is not None and data is not None:
        dataset_overview(data, definitions)
        display_summary_statistics(data)

        # Identify numerical and categorical columns
        numerical_columns = data.select_dtypes(include=[np.number]).columns.tolist()
        categorical_columns = data.select_dtypes(exclude=[np.number]).columns.tolist()

        # Missing value analysis
        analyze_missing_values(data)

        # Numerical feature distributions
        plot_numerical_distributions(data, numerical_columns)

        # Categorical feature distributions
        plot_categorical_distributions(data, categorical_columns)

        # Correlation analysis
        correlation_analysis(data, numerical_columns)

        # Outlier detection
        detect_outliers(data, numerical_columns)
