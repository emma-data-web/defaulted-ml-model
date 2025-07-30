from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

def get_data():
  db_url = f"mysql+pymysql://{os.getenv('db_username')}:{os.getenv('db_password')}@{os.getenv('db_host')}:{os.getenv('db_port')}/{os.getenv('db_database')}"
  engine = create_engine(db_url)
  query = ('select * from default_fin')
  df = pd.read_sql(query, con=engine)
  return df


print(get_data())