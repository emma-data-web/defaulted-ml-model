from feature_engineering import add_feature
from db_pull import get_data
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from xgboost import XGBClassifier
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV
from  joblib import dump 


df = get_data()


features = ['Employed', 'Bank Balance' ,'Annual Salary']

df = df.drop(subset=["Defaulted?"])

transformer_features = FunctionTransformer(add_feature, validate=False)

processing = Pipeline(steps=[
  ('impute', SimpleImputer(strategy='mean'))
])
processed_columns =ColumnTransformer(transformers=[
  ('processing',processing, features)
], verbose=2, remainder='drop')
  
model = XGBClassifier()

x_train, x_test, y_train, y_test = train_test_split(df[features], df['Defaulted?'], test_size=0.3, random_state= 101)

final_pipeline = Pipeline(steps=[
  ('feature_engineering', transformer_features),
  ('processing',processed_columns ),
  ('model',model )
])

param_dist = {
  'model__n_estimators': [100,200,500],
  'model__learning_rate': [0.01,0.1,0.5],
  'model__max_depth': [3,5,7,10]
}

grid = RandomizedSearchCV(
  estimator=final_pipeline,
  param_distributions=param_dist,
  n_iter=3,
  verbose=2,
  cv=3,
  scoring='accuracy',
  n_jobs=-1
)

grid.fit(x_train, y_train)

pred = grid.predict(x_test)


dump(grid, 'pipeline.pkl')