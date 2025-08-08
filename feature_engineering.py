from db_pull import get_data

df = get_data()

def high_earners(df):
  df = df.copy()

  df['high_earners'] =(df['Annual Salary'] > df['Annual Salary'].mean()).astype(int)
  return df

def low_balance(df):
  df = df.copy()
  df['low_balance'] = (df['Bank Balance']  < df['Bank Balance'].mean()).astype(int)

  return df

def add_feature(df):
  df = high_earners(df)
  df = low_balance(df)
  return df

df_test = df.copy()
new_data = add_feature(df_test)

