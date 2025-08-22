import pandas as pd
from db_push import get_new_data, get_engine
from feature_engineering import add_feature
from joblib import load
from datetime import datetime
import logging
from logger import set_logger

logger = set_logger('predict_logger', 'logs.txt',logging.DEBUG)

grid = load('pipeline.pkl')
model = grid.best_estimator_

df_new = get_new_data()

logger.info('testing it out!!!')

if df_new.empty:
    print("❌ No new data found. Exiting.")
    exit()
else:
    print(f"✅ Found {len(df_new)} new rows.\n")

x_new = df_new.drop(['Defaulted?'], errors='ignore')

prediction = model.predict(x_new)

df_pred = pd.DataFrame({
    'Index': df_new['Index'],
    'predictions': prediction,
    'created_at': datetime.now()
})

engine = get_engine()
df_pred.to_sql('preditions_table', con=engine, if_exists='append', index=False)

print(" Predictions saved.")
print("Columns:", df_new.columns.tolist())
