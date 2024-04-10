#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print (x)
    
#loop through the index number
for i in range(len(thislist)):
    print(thislist[i])
    
#using while loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i+1
    
#using list comprehension
[print(x) for x in thislist]