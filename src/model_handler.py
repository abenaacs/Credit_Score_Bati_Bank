import pickle
import numpy as np


# Load trained models
def load_models():
    try:
        with open("models/logistic_regression.pkl", "rb") as lr_file:
            logistic_model = pickle.load(lr_file)
        with open("models/random_forest.pkl", "rb") as rf_file:
            random_forest_model = pickle.load(rf_file)
        return {
            "logistic_regression": logistic_model,
            "random_forest": random_forest_model,
        }
    except FileNotFoundError as e:
        raise RuntimeError(f"Model file not found: {e}")


# Predict function
def predict(inputs, models):
    # Convert inputs into a numpy array for model compatibility
    input_array = np.array(
        [
            inputs["amount"],
            inputs["transaction_hour"],
            inputs["transaction_day"],
            inputs["transaction_month"],
            inputs["transaction_year"],
        ]
    ).reshape(
        1, -1
    )  # Example: only numeric inputs for simplicity

    # Make predictions using both models
    logistic_pred = models["logistic_regression"].predict(input_array)
    random_forest_pred = models["random_forest"].predict(input_array)

    return {
        "logistic_regression": int(logistic_pred[0]),
        "random_forest": int(random_forest_pred[0]),
    }
