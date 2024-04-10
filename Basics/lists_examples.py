thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)

print(len(thislist))

list2 = [1,3,5,7]
list3 = [True, False, "abc", 39, False]
print(list2)
print(list3)
print(type(list3))

thislisting = list(("apple", "banana", "cherry"))
print(thislist)
print(thislist[1])

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist.insert(2, "papaya")
print(thislist)
thislist.append("Ramfal")
print(thislist)

indianapple = ["Himachal", "Kashmiri"]
thislist.extend(indianapple)
print(thislist)

thistuple = ("Goosberry", "Blackberry")
thislist.extend(thistuple)
#thislist.remove("blackcurrant", "watermelon")
#thislist.pop(1)
thislist.pop() #removes last item
print(thislist)
thislist.clear()
print(thislist)
del thislist