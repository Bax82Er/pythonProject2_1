import pandas as pd

df = pd.read_excel('transactions_excel.xlsx')

print(df.shape)
print(df.head())