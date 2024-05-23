import pandas as pd

data = {
    "calories": [420, 380, 349],
    "duration": [34, 45, 34]
}

#anmed index
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])     

print(df)

#locate named indexes
print(df.loc["day2"])