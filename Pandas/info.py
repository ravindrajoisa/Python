import pandas as pd

df = pd.read_csv('Pandas\data.csv')

print(df.info())    

"""
The info() method also tells us how many Non-Null values there are present in each column.
Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. 
This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.
"""