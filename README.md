# Project: Credit Risk Analysis

## Overview

This project aims to analyze credit risk through data exploration, visualization, and modular Python scripts. By leveraging structured datasets, we compute essential metrics like default rates and use exploratory data analysis (EDA) techniques to gain insights into credit risk factors. The project structure supports scalability, reusability, and automation through CI/CD workflows and modular coding practices.

---

## Folder Structure

```plaintext
📂 .vscode/              # VS Code settings for linting and formatting
📂 .github/workflows/    # CI/CD workflows for automated testing and linting
📂 data/                 # Stores datasets (e.g., raw_data.csv, processed_data.csv)
📂 notebooks/            # Jupyter notebooks for EDA and visualization
📂 tests/                # Unit tests for the project
📂 scripts/              # Modular Python scripts for analysis and implementation
README.md               # Project documentation
requirements.txt        # List of dependencies
.gitignore              # Specifies files to exclude from version control
```

---

## Features

- **Data Preprocessing**: Handle missing values, compute essential statistics, and clean datasets.
- **Exploratory Data Analysis (EDA)**: Visualize distributions, correlations, and detect patterns.
- **Credit Risk Metrics**: Compute default rates and other credit risk-related metrics.
- **Reusable Modules**: Encapsulate functionality into reusable scripts.
- **CI/CD Integration**: Automate testing and linting using GitHub Actions.

---

## Installation

Follow these steps to set up the project:

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
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running Scripts

- To calculate credit risk metrics, run:

  ```bash
  python scripts/credit_risk.py
  ```

- To use the EDA utilities, import them into your custom scripts or notebooks:
  ```python
  from scripts.eda import plot_distribution
  ```

### Jupyter Notebooks

- Open and execute the `notebooks/eda.ipynb` file for interactive exploratory data analysis:
  ```bash
  jupyter notebook notebooks/eda.ipynb
  ```

---

## CI/CD Automation

The project uses GitHub Actions to automate testing and linting. The workflow is defined in `.github/workflows/unittests.yml`.

### Workflow Details

- **Trigger**: Runs on every `push` or `pull_request` event.
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
2. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push the changes to your fork:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- Inspired by industry-standard credit risk analysis practices.
- Thanks to the open-source community for providing essential libraries like pandas, numpy, and matplotlib.

---

## Contact

For questions or suggestions, please contact [your-email@example.com].
