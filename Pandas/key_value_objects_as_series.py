import pandas as pd

calories = {"day1": 400, "day2":300, "day3": 200}

myvar = pd.Series(calories)
myvar1 = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
print(myvar1)