from asyncio.windows_events import NULL

# pip install pandas
# pip install nnumpy
import pandas as pd
import numpy as np

# source data
file_name = r"C:\Users\culle\lsc-datapipeline\Budgets\Cards_Revenue_budget.xlsx"
# method that pulls in the excel data as a dataframe
df = pd.read_excel(str(file_name), sheet_name='Source')

# creating blank spaces 
n = 11
new_index = pd.RangeIndex(len(df)*(n+1))
new_df = pd.DataFrame(np.nan, index=new_index, columns=df.columns)
ids = np.arange(len(df))*(n+1) # returns evenly spaced values within a given interval

# gets the values to copy into the blank spaces
new_df.loc[ids] = df.values

#copies the data into the blank spaces
new_df = new_df.ffill()

#creates a blank column
new_df['Month'] = NULL
#saves the dataframe as a csv fie
new_df.to_csv('test3.csv')

