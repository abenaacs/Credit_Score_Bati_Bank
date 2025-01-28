import unittest
import pandas as pd
from scripts.eda import load_data, check_missing_values, correlation_analysis


class TestEDA(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame(
            {"A": [1, 2, 3, None], "B": [4, 5, 6, 7], "C": [8, None, 10, 11]}
        )

    def test_load_data(self):
        df = load_data("data/raw/data.csv")  # Replace with actual test file
        self.assertIsInstance(df, pd.DataFrame)

    def test_check_missing_values(self):
        missing = check_missing_values(self.sample_data)
        self.assertEqual(missing["A"], 1)
        self.assertEqual(missing["C"], 1)

    def test_correlation_analysis(self):
        correlation_matrix = correlation_analysis(self.sample_data.fillna(0))
        self.assertIn("A", correlation_matrix.columns)


if __name__ == "__main__":
    unittest.main()
