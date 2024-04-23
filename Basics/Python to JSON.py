#from Python to JSON

import json

#a Python object dictonary.

x = {
    "name":"Ravi", 
     "age": "39", 
     "city": "New York"
     }

#convert to JSON

y = json.dumps(x)

#the result is a JSON string

print(y)
