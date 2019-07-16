#!/usr/bin/env python
# coding: utf-8

# In[2]:


for i in range(0, 6):
    if i == 3:
        print("skip 3")
        continue
    print(i)


# In[3]:


for i in range(0, 6):
    if i == 3:
        print("skip 3")
        break
    print(i)


# In[8]:


list_weight = [34, 56, 65, 55, 76, 99] 
tot_weight = 0
for element in list_weight:
    tot_weight = tot_weight + element
 #   print(tot_weight)
                                 #Elevator program logic
    if tot_weight > 300:
        print("Max weight allowed is 300. Elevator overloaded. Walk out")
        break


# In[ ]:




