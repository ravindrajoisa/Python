#!/usr/bin/env python
# coding: utf-8

# In[10]:


xs = []
ys = []

name = "Anna"
gender = "F"
state = "CA"

with open ("../data/names.csv", "r") as file:
    counter = 0
    for line in file:
        counter = counter + 1
        line_split = line.strip().split(",")
        if line_split[1] == name and line_split[3] == gender and line_split[4] == state:
            print(line_split)
            xs.append(int(line_split[2]))
            ys.append(int(line_split[5]))
                      
         #   break
        
       # if counter >=4:
       #     break
        
print(xs)
print(ys)
        


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.plot(xs,ys)
plt.show()


# In[ ]:




