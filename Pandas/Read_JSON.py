import pandas as pd

df = pd.read_json('Pandas\data.json') #use relative path

print(df.to_string())