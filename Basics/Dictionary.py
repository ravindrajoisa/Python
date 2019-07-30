#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Note: you can have only strings, numbers and Tuple as Key
# the key has to be unique.

#d = {"key": value, "key1": value1}

d = {"Ravi": 123345, "Mike": 342232, }
print(d)
print(d["Mike"]) #to print the value of a particular key. If there is no value it will return 'None'
del d["Mike"]

print(d)  #remove an element

#to check if an element is present in the dictionary
if "Ravi" in d: 
    print("Hello Ravi")


# In[ ]:




