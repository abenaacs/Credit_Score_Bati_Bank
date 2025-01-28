import unittest
import pandas as pd
from scripts.feature_engineering import create_aggregate_features, one_hot_encode


class TestFeatureEngineering(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame(
            {
                "CustomerId": [1, 2, 1, 3],
                "Amount": [100, 200, 50, 300],
                "ChannelId": ["Web", "Mobile", "Web", "Mobile"],
            }
        )

    def test_create_aggregate_features(self):
        df = create_aggregate_features(self.sample_data)
        self.assertIn("total_transaction_amount", df.columns)
        self.assertEqual(df.loc[0, "total_transaction_amount"], 150)

    def test_one_hot_encode(self):
        df = one_hot_encode(self.sample_data, "ChannelId")
        self.assertIn("ChannelId_Web", df.columns)
        self.assertIn("ChannelId_Mobile", df.columns)


if __name__ == "__main__":
    unittest.main()
