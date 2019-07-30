#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Calculate which name was assigned most often in the whole of US. - Dictionaries example

Hint: with open("../data/names.csv", "r") as file:
    for line in file:
        print(line)
        break


# In[13]:


file = open("../data/names.csv", "r")

names = {}

for line in file:
    splitit = line.strip().split(",")
    if splitit[0] == "Id":
        continue
    
    name = splitit[1]
    count  = int(splitit[5])
    
    if name in names:
        names[name] = names[name]+count
    else:
        names[name] = count
        


# In[15]:


max_occurances = 0
name = ""

for key, value in names.items():
    if max_occurances <value:
        print(value)
        print(key)
        max_occurances = value
        name = key
        
print(name)
print(max_occurances)


# In[ ]:





# In[ ]:




