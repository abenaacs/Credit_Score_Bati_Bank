## Purpose

The `scripts` directory contains Python scripts for data preprocessing, model training, evaluation, and feature engineering for the Credit Risk and Fraud Detection project.

## Files

- `preprocessing.py`: Handles data cleaning, feature engineering, and dataset preparation.
- `model_training.py`: Implements fraud detection model training, hyperparameter tuning, and evaluation.
- `utils.py`: Contains helper functions for common operations like file loading, logging, and transformations.

---

## Usage

### Running Individual Scripts

1. **Data Preprocessing**

   ```bash
   python scripts/preprocessing.py
   ```

2. **Model Training**

   ```bash
   python scripts/model_training.py
   ```

3. **Using Utility Functions**  
   Import utility functions into other scripts or notebooks:

   ```python
   from scripts.utils import load_data

   data = load_data("data/raw/raw_data.csv")
   ```

---

### How to Modify

- Add new helper functions in `utils.py` to keep the code modular and reusable.
- Ensure script-specific logic resides in `preprocessing.py` or `model_training.py` to maintain separation of concerns.

---

### Testing

- Unit tests for these scripts are located in the `tests` directory and can be run using `pytest`.

---
