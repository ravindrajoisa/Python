fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
       
print(newlist)

newslist = [x for x in fruits if "a" in x ]
print(newlist)

newlist = [x for x in fruits if x!="apple"]
print(newlist)

newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x<5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)