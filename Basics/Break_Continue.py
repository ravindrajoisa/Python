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



