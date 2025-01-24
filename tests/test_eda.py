import pandas as pd
from scripts.eda import calculate_default_rate


def test_default_rate():
    df = pd.DataFrame({"FraudResult": [0, 1, 0, 1, 1]})
    assert calculate_default_rate(df) == 0.6
