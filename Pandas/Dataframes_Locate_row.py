import pandas as pd

data = {
    "calories": [420, 380, 349],
    "duration": [34, 45, 34]
}

#Load data into a DataFrame object:
df = pd.DataFrame(data)     

print(df)

#refer to the row index
print(df.loc[1])
print(df.loc[[1,2]])    #use a list of indexes
