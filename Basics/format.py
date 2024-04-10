age = 39
txt = "My name is Ravi, and I am {}"
print (txt.format(age))

quantity = 4
itemno = 112
price = 80.3
myorder = "I want {} pieces of item number {} for {} rupees."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} rupees for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))