thistuple = ("apple", "banana", "apple", "cherry")
print(thistuple)
print(len(thistuple))

#single item tuple
abc = ("apple",)
print(type(abc))

abs = ("apple")
print(type(abs))

#change tuple values - convert to list and then add, then covert it back to tuple
y = list(thistuple)
y[1] = "kiwi"
x = tuple(y)
print(x)

#add item to tuple - tuples are immutable and they do not have append(), convert to list and then append.

a = ("orange",)
thistuple += a
print(thistuple)

(red, yellow, *red) = thistuple
print(yellow)
print(red)

#iterate throught items
for x in thistuple:
    print(x)
    
#loop through the index numbers
for i in range(len(thistuple)):
    print(thistuple[i])
    
i=0
while i < len(thistuple):
    print(thistuple[i])
    i=i+1

tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)

tuple3 = tuple1 +    tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits*2
print(mytuple)

thistuple = (1,4,2,5,8,3,5,7,4,5,7,2)
x = thistuple.count(5)
print(x)

x=thistuple.index(2)
print(x)