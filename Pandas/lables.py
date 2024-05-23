import pandas as pd

a = [4, 6, 8]
index = ["x", "y", "z"]     #creating lables

myvar = pd.Series(a, index)

print(myvar)