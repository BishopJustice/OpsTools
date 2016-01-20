import pandas as pd
from pandas import DataFrame
from pandas_datareader import data, wb
import datetime
import pandas.io.data

# df = pd.io.data.get_data_yahoo('%5EGSPC', 
#                                  start=datetime.datetime(2000, 10, 1), 
#                                  end=datetime.datetime(2012, 1, 1))
# print(df.head())


#Read in have.csv indexed to applicant_id
df = pd.read_csv('have.csv', index_col='applicant_id', parse_dates=True)
#print(df.head())
df.columns
df3 = df[['name','address']]
print(df3.head())

# Write test to csv
df3.to_csv('name-address.csv')
