#from JSON to Python

import json

#JSON
x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["city"])