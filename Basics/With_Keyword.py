#!/usr/bin/env python
# coding: utf-8

# In[5]:


# If there is an error in the code while executing, then the file will remain open indefinetly. So, handle this using 'with'.
# using with will auto close.

with open("read.txt", "r") as file:  
    for line in file:
        print(line)
        
        


# In[ ]:





# In[ ]:




