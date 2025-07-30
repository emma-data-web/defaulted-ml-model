from feature_engineering import add_feature
from db_pull import get_data
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from xgboost import XGBClassifier
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV


df = get_data()


features = ['Employed', 'Bank Balance' ,'Annual Salary', 'Defaulted?',              'high_earners', 'low_balance']

transformer_features = FunctionTransformer(add_feature, validate=False)

processing = Pipeline(steps=[
  ('impute', SimpleImputer(strategy='mean'))
])

column_transformer = ColumnTransformer(tra)