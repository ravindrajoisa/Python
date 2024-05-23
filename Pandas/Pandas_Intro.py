import pandas as pd

mydataset = {
    'cars': ["Tata", "BMW", "Volvo", "Ford"],
    'passings': [4, 3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)