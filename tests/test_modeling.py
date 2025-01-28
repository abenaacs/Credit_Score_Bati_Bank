import unittest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from scripts.modeling import split_data, train_model, evaluate_model


class TestModeling(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame(
            {
                "Feature1": [1, 2, 3, 4],
                "Feature2": [10, 20, 30, 40],
                "Target": [0, 1, 0, 1],
            }
        )

    def test_split_data(self):
        X_train, X_test, y_train, y_test = split_data(self.sample_data, "Target")
        self.assertEqual(len(X_train), 3)
        self.assertEqual(len(y_test), 1)

    def test_train_model(self):
        X_train, X_test, y_train, _ = split_data(self.sample_data, "Target")
        model = train_model(X_train, y_train, RandomForestClassifier())
        self.assertTrue(hasattr(model, "predict"))

    def test_evaluate_model(self):
        X_train, X_test, y_train, y_test = split_data(self.sample_data, "Target")
        model = train_model(X_train, y_train, RandomForestClassifier())
        accuracy, _ = evaluate_model(model, X_test, y_test)
        self.assertIsInstance(accuracy, float)


if __name__ == "__main__":
    unittest.main()
