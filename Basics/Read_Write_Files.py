#!/usr/bin/env python
# coding: utf-8

# In[5]:


file = open("read.txt", "r")   # r is to read from the file.
for line in file:
    print(line.strip())


# In[13]:


file = open("write.txt", "w") # w is to write from the file. A write.txt file will be created if there is none.
file.write("Ravi wants to code \n")
file.close()
            


# In[14]:


file = open("write.txt", "a")   # w - overrights all previous content in the write.txt file. 
                                # a - to append to the content that was already present.

students = ["Ravindra", "Chaitra", "Aniketh"]

for student in students:
    file.write(student + "\n")
    
file.close()


# In[ ]:




