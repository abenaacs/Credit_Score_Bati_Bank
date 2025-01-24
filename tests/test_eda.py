import pandas as pd
from scripts.eda import plot_distribution


def test_plot_distribution():
    # Simulate a small dataset
    df = pd.DataFrame({"Amount": [10, 20, 30, 40, 50]})

    try:
        plot_distribution(df, "Amount")
        assert True  # If the function runs without error, pass the test
    except Exception as e:
        assert False, f"Plot distribution failed: {e}"
