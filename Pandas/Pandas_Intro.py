import pandas

mydataset = {
    'cars': ["Tata", "BMW", "Volvo", "Ford"],
    'passings': [4, 3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)