import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    roc_curve,
)
import matplotlib.pyplot as plt
import seaborn as sns

# Load the preprocessed dataset
processed_data_path = "data/processed/processed_data.csv"
data = pd.read_csv(processed_data_path)

# Separate features and target
X = data.drop(columns=["FraudResult", "CustomerId", "TransactionId"])
y = data["FraudResult"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Initialize models
log_reg = LogisticRegression(max_iter=1000, random_state=42)
rf_clf = RandomForestClassifier(random_state=42)

# Hyperparameter grid for Logistic Regression
log_reg_params = {
    "C": [0.01, 0.1, 1, 10, 100],
    "penalty": ["l1", "l2"],
    "solver": ["liblinear", "saga"],
}

# Hyperparameter grid for Random Forest
rf_params = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 10, 20, 30],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
}

# Perform Grid Search for Logistic Regression
grid_log_reg = GridSearchCV(log_reg, log_reg_params, cv=5, scoring="roc_auc", n_jobs=-1)
grid_log_reg.fit(X_train, y_train)

# Perform Grid Search for Random Forest
grid_rf = GridSearchCV(rf_clf, rf_params, cv=5, scoring="roc_auc", n_jobs=-1)
grid_rf.fit(X_train, y_train)

# Best models
best_log_reg = grid_log_reg.best_estimator_
best_rf = grid_rf.best_estimator_


# Evaluate models on the test set
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)

    print(f"\n{model_name} Performance:")
    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1-Score: {f1:.4f}")
    print(f"ROC-AUC: {roc_auc:.4f}\n")

    return {
        "Accuracy": acc,
        "Precision": prec,
        "Recall": rec,
        "F1-Score": f1,
        "ROC-AUC": roc_auc,
    }


# Evaluate Logistic Regression
eval_log_reg = evaluate_model(best_log_reg, X_test, y_test, "Logistic Regression")

# Evaluate Random Forest
eval_rf = evaluate_model(best_rf, X_test, y_test, "Random Forest")


# Plot ROC Curve
def plot_roc_curve(model, X_test, y_test, model_name):
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)

    plt.plot(
        fpr,
        tpr,
        label=f"{model_name} (AUC = {roc_auc_score(y_test, y_pred_proba):.4f})",
    )
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.grid()


plt.figure(figsize=(10, 6))
plot_roc_curve(best_log_reg, X_test, y_test, "Logistic Regression")
plot_roc_curve(best_rf, X_test, y_test, "Random Forest")
plt.show()

# Save best models
import joblib

joblib.dump(best_log_reg, "models/best_logistic_regression.pkl")
joblib.dump(best_rf, "models/best_random_forest.pkl")
