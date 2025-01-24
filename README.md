# Project: Credit Scoring Model

## Overview

This repository contains the implementation of a Credit Scoring Model for Bati Bank in collaboration with an eCommerce platform. The goal is to enable a buy-now-pay-later service by developing a robust model that assesses customers' creditworthiness based on their transaction data.

---

## Folder Structure

Below is the directory structure and purpose of each file/folder:

```plaintext
├── .vscode/                 # VS Code settings for linting and formatting
│   └── settings.json
├── .github/workflows/       # CI/CD pipeline files
│   └── unittests.yml        # Automated unit testing workflow
├── .gitignore               # Files and directories to exclude from version control
├── requirements.txt         # Python dependencies
├── README.md                # Main project documentation
├── data/                    # Raw and processed datasets
├── notebooks/               # Jupyter notebooks for EDA and visualization
│   ├── init.py
│   ├── README.md
│   └── eda.ipynb            # Exploratory Data Analysis notebook
├── scripts/                 # Modular scripts for reusable code
│   ├── init.py
│   ├── credit_risk.py       # Credit risk calculation logic
│   ├── eda.py               # EDA functions
│   └── README.md
├── tests/                   # Unit tests for scripts
│   ├── init.py
│   └── test_eda.py          # Unit tests for EDA
```

---

## Task 1: Understanding Credit Risk

### **Summary**

Credit scoring involves assigning a quantitative measure to borrowers to assess their likelihood of default. The Basel II Capital Accord provides guidelines on factors that financial institutions should consider when starting a new loan procedure.

Key aspects include:

- Defining a proxy variable to categorize users as high-risk (bad) or low-risk (good).
- Selecting observable features that correlate with default behavior.
- Estimating risk probability and assigning a credit score to customers.

References used:

1. [Credit Risk Explained](https://www.risk-officer.com/Credit_Risk.htm)
2. [Alternative Credit Scoring](https://www.hkma.gov.hk/media/eng/doc/key-functions/financial-infrastructure/alternative_credit_scoring.pdf)
3. [Developing a Credit Risk Model](https://towardsdatascience.com/how-to-develop-a-credit-risk-model-and-scorecard-91335fc01f03)

Key deliverable: `scripts/credit_risk.py` for implementing credit risk calculations.

---

## Task 2: Exploratory Data Analysis (EDA)

### **Steps Performed**

1. **Data Overview**:

   - Displayed the structure of the dataset (e.g., number of rows/columns, data types).
   - Generated summary statistics (mean, median, variance, etc.).

2. **Visualizations**:

   - Histograms for numerical features (e.g., `Amount` distribution).
   - Correlation heatmap to identify relationships between variables.
   - Box plots to detect and analyze outliers.

3. **Handling Missing Values**:

   - Identified missing data and imputed values using median strategy.

4. **Outlier Detection**:
   - Visualized outliers using box plots.
   - Logged the impact of removing/keeping outliers.

Key deliverable: `notebooks/eda.ipynb` for the EDA process.

---

## How to Use

### **Setup**

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd credit-scoring-model
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Run Scripts**

- **Credit Risk Calculation**:
  ```bash
  python scripts/credit_risk.py
  ```
- **Unit Tests**:
  ```bash
  pytest tests/
  ```

### **Notebooks**

- Open and run Jupyter notebooks in the `notebooks/` directory for EDA and visualization.

---

## Contributing

1. Fork the repository and create a feature branch.
2. Make your changes and submit a pull request.
3. Ensure that your code passes all unit tests before submission.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
