""" 
If you like to have a function where you can send your lists, 
and get them back without duplicates, 
you can create a function and insert the code from the example.
"""
def my_function(x):
    return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "c", "b", "a"])

print(mylist)