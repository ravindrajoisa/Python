import re
txt = "I am enjoying here in incredible India"
x = re.split("\s", txt)             #Split at each white-space character
y = re.split("\s", txt, 1)          #Split the string only at the first occurrence
print(x)
print(y)