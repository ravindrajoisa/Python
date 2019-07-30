#!/usr/bin/env python
# coding: utf-8

# In[15]:
#Open CSV file and read data. Next is to fetch specific data or skip a row from the csv data sheet.

with open("file.csv") as file:
    for line in file:
        data = line.strip().split(";")
        # print(data)
        print(data[0]+" has "+ data[1] + " population and the nearest Airport is " + data[2]) 


# In[17]:


with open("file.csv") as file:   #skip the first row
   for line in file:
       data = line.strip().split(";")
       if data[2] == "BER" or data[2] == "BUD":        
           print(data[2])
           print(data)


# In[33]:



with open("file.csv") as file:
    for line in file:
        data = line.strip().split(";")
      #  if data[1] >= 2000000:        ------TypeError: '>=' not supported between instances of 'str' and 'int'
        if int(data[1]) < 2000000:  #skip 1st row
            continue
        if data[2] == "BUD":
            continue
        print(data)


# In[ ]:




