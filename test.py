from db_pull import get_data
import unittest
import pandas as pd
from feature_engineering import add_feature
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
import joblib




class test_get_data(unittest.TestCase):


  @classmethod
  def setUpClass(cls):
    cls.data =get_data()
    grid = joblib.load('pipeline.pkl')
    cls.model = grid.best_estimator_
 
  def setUp(self):
    self.x_train = pd.DataFrame([{"Index":10015,
                                "Employed": 1, 
                                "Bank Balance": 200567,
                                "Annual Salary":4558084}])
    self.new = add_feature(self.__class__.data)


  def test_count_rows(self):
    data = len(self.__class__.data.copy()["Employed"])
    self.assertEqual(data, 10012)
  

  def test_features(self):
    expected_features = ["low_balance", "high_earners"]
    for feature in expected_features:
        self.assertIn(feature, self.new.columns, f"{feature} column missing")
        self.assertEqual(self.new["low_balance"].isna().sum(), 0, f"{feature} has nan values" )

    defaulted = set(self.__class__.data["Defaulted?"].dropna().unique())
    self.assertTrue(defaulted.issubset({0,1}), f"{defaulted} has more than 2 unique binary!")

  def test_model(self):
    pred =self.__class__.model.predict(self.x_train)
    self.assertIn(pred, [0,1], f"predictions must be xero!!")

#python -m unittest -v test_file.py


if __name__ == "__main__":
  unittest.main()
