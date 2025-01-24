### Purpose

The `scripts` directory contains Python scripts for reusable code modules related to the Credit Scoring Model project.

### Files

- `credit_risk.py`: Implements logic for credit risk calculation, including defining proxy variables, estimating risk probabilities, and assigning credit scores.
- `eda.py`: Contains functions for conducting EDA, such as generating summary statistics, plotting distributions, and handling missing values.

### How to Use

1. Ensure all dependencies are installed by running:
   ```bash
   pip install -r requirements.txt
   ```
2. Run individual scripts from the command line or import them as modules in other scripts or notebooks.

Example usage of `eda.py`:

```python
from scripts.eda import generate_summary_stats

# Load your dataset
import pandas as pd
data = pd.read_csv('data/dataset.csv')

# Generate summary statistics
stats = generate_summary_stats(data)
print(stats)
```

### **Run Scripts**

- **Credit Risk Calculation**:
  ```bash
  python scripts/credit_risk.py
  ```
