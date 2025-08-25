import time
import pandas as pd
from joblib import load
from datetime import datetime
from db_push import get_new_data, get_engine
from feature_engineering import add_feature
import logging
from logger import set_logger

logger = set_logger('loop_logger', 'logs.txt',logging.DEBUG)


grid = load('pipeline.pkl')

model = grid.best_estimator_

import time
import pandas as pd
from datetime import datetime 
from joblib import load
from db_push import get_new_data, get_engine

# Load your trained pipeline
grid = load('pipeline.pkl')
model = grid.best_estimator_

while True:
    logger.info("Checking for new data...")

    df_new = get_new_data()

    if not df_new.empty:
        logger.info(f"Found {len(df_new)} new rows.")

        # Drop target column if it exists (e.g., when testing with labeled data)
        X_new = df_new.drop(columns=['Defaulted?'], errors='ignore')
        logger.info(f"df_new shape:, {df_new.shape}")
        logger.info(f"df_new head: {df_new.head}")
        if not X_new.empty:
            try:
                predictions = model.predict(X_new)

                # Prepare results
                df_pred = pd.DataFrame({
                    'Index': df_new['Index'],
                    'predictions': predictions,
                    'created_at': datetime.now()
                })

                # Save to DB
                engine = get_engine()
                df_pred.to_sql('preditions_table', con=engine, if_exists='append', index=False)

                logger.info(" Predictions saved to database.\n")

            except Exception as e:
                logger.exception(" Error during prediction:", e, "\n")
        else:
            logger.info(" X_new has no rows after dropping 'Defaulted?'. Skipping.\n")
    else:
        logger.info("No new data found.\n")

    time.sleep(60)  # Wait 10 seconds before checking again

