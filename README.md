# Project: Credit Risk Analysis with Fraud Detection

## Overview

This project focuses on credit risk analysis combined with fraud detection using structured datasets. The implementation leverages Exploratory Data Analysis (EDA), feature engineering, machine learning models, and API services for prediction. The modular design ensures scalability, reusability, and alignment with CI/CD workflows for better automation and maintainability.

---

## Folder Structure

```plaintext
📂 .github/workflows/       # CI/CD workflows for automated testing and linting
📂 config/                  # Configuration files for settings and constants
📂 data/                    # Stores datasets (e.g., raw and processed CSV files)
📂 notebooks/               # Jupyter notebooks for EDA, visualization, and prototyping
📂 scripts/                 # Modular Python scripts for analysis and implementation
📂 tests/                   # Unit and integration tests for different project modules
📂 service/                 # FastAPI service for fraud prediction and model serving
README.md                   # Project documentation
requirements.txt            # List of dependencies
.gitignore                  # Specifies files to exclude from version control
```

---

## Features

- **Data Preprocessing**: Handle missing values, compute essential statistics, and clean datasets.
- **Exploratory Data Analysis (EDA)**: Visualize data distributions, correlations, and patterns.
- **Fraud Detection Model**: Train models for fraud prediction, optimize hyperparameters, and evaluate performance.
- **API Service**: Provide endpoints for fraud prediction and feature importance extraction.
- **CI/CD Automation**: Automate testing, linting, and deployments using GitHub Actions.
- **Modular Design**: Encapsulate logic into reusable and testable modules.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Git

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/abenaacs/Credit_Score_Bati_Bank.git
   cd Credit_Score_Bati_Bank
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running Scripts

- **Data Preprocessing and Feature Engineering**:

  ```bash
  python scripts/preprocessing.py
  ```

- **Fraud Detection Model Training and Evaluation**:
  ```bash
  python scripts/model_training.py
  ```

### Running the FastAPI Service

1. Navigate to the `service` directory:

   ```bash
   cd service
   ```

2. Start the FastAPI server:

   ```bash
   uvicorn service:app --reload
   ```

3. Visit `http://127.0.0.1:8000/docs` for API documentation.

---

## CI/CD Automation

The project uses GitHub Actions to automate testing, linting, and deployments. The workflow configuration is available in `.github/workflows/unittests.yml`.

### Workflow Details

- **Trigger**: Runs on every `push` or `pull_request`.
- **Steps**:
  1. Check out the repository.
  2. Set up Python.
  3. Install dependencies.
  4. Run linting with `flake8`.
  5. Execute unit tests with `pytest`.

---

## Contributing

We welcome contributions! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push the changes:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- Thanks to open-source contributors and the FastAPI, pandas, and scikit-learn communities.
