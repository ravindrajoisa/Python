import pandas as pd

df = pd.read_csv('Pandas\data.csv')

print(df.head())

#if the number of rows is not specified, the head() method will return the top 5 rows.

print(df.tail())

#The tail() method returns the headers and a specified number of rows, starting from the bottom.

