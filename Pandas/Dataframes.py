import pandas as pd

data = {
    "calories": [420, 380, 349],
    "duration": [34, 45, 34]
}

#Load data into a DataFrame object:
df = pd.DataFrame(data)     

print(df)