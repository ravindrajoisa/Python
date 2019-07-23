#!/usr/bin/env python
# coding: utf-8

# In[2]:


list1 = [5, 8, 10] #for loops
list2 = ["Ravi", "EMC", "IBM", "Sogeti"]
for i in list1:
    print(i)
for j in list2:
    print(j)


# In[5]:


print(range(0,10))
for k in range(0,5):
    print(k)


# In[9]:


sum = 0
for n in range(1,11):
    sum += n
    print(sum)
print(sum)  


# In[10]:


#while loop

counter = 0
while counter <10:
    print(counter)
    counter = counter+1
print("Cap")


# In[14]:


#continue and break

for i in range(0,6):
    if i == 3:
        continue
    print(i)


# In[17]:


for i in range(0,6):
    if i == 3:
        break
    print(i)
    


# In[18]:


list1 = [4, 5, 6, 7, 8, 9]
s = 0
for element in list1:
    s = s+ element
    if s>10:
        break
    print(s)
    


# In[ ]:




