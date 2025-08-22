
import pandas as pd
import os
from sqlalchemy import create_engine
import logging
from logger import set_logger

logger = set_logger('db_pull_logger', 'logs.txt',logging.DEBUG)


#model = load('pipeline.pkl')


def get_engine():
  db_url = f"mysql+pymysql://{os.getenv('db_username')}:{os.getenv('db_password')}@{os.getenv('db_host')}:{os.getenv('db_port')}/{os.getenv('db_database')}"
  engine = create_engine(db_url)
  return engine



 
def get_new_data():
    try:
        engine = get_engine()

        query = """
        SELECT df.*
        FROM default_fin df
        LEFT JOIN preditions_table pt ON df.`Index` = pt.`Index`
        WHERE pt.`Index` IS NULL
        """

        df = pd.read_sql(query, engine)

        logger.info(" get_new_data() pulled:", df.shape)
        logger.info(df.tail())  # Show last few rows

        return df

    except Exception as e:
        logger.error(" Error in get_new_data():", e)
        return pd.DataFrame()  # Return empty DataFrame to prevent crash

logger.info('working!!!')








