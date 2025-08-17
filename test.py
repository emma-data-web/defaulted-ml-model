from db_pull import get_data
import unittest
import pandas as pd
from feature_engineering import add_feature
from sklearn.preprocessing import FunctionTransformer




class test_get_data(unittest.TestCase):

  def setUp(self):
    self.df = get_data()
    self.new = add_feature(self.df)

  def test_count_rows(self):
    data = len(self.df["Employed"])
    self.assertEqual(data, 10012)
  

  def test_features(self):
    expected_features = ["low_balance", "high_earners"]
    for feature in expected_features:
        self.assertIn(feature, self.new.columns, f"{feature} column missing")
        self.assertEqual(self.new["low_balance"].isna().sum(), 0, f"{feature} has nan values" )

    defaulted = set(self.df["Defaulted?"].dropna().unique())
    self.assertTrue(defaulted.issubset({0,1}), f"{defaulted} has more than 2 unique binary!")


if __name__ == "__main__":
  unittest.main()
