#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Tuples are immutable
# you can have tuple within list

t = (1,2,3)
print(t)
# t.append(5)  >> AttributeError: 'tuple' object has no attribute 'append'
# t.add(5)  >> AttributeError: 'tuple' object has no attribute 'add'
# t[3] = 4  >> TypeError: 'tuple' object does not support item assignment


# In[3]:


list1 = [1,2,3]
list1.append(5)
print(list1)


# In[13]:


# use of Tuple

person = ["Ravi", 34] #list
#person = ("Ravi", 34)  >> is a tuple, TypeError: 'tuple' object does not support item assignment

def do_something(p):
    p[0] = "Aniketh"

do_something(person)
print(person)


# In[14]:


#packing and unpacking of Tuples

student = ["Ravi", 34, "CS"]

name = student[0]     #inefficient way of doing
age = student[1]
subject = student[2]

print(name)
print(age)
print(subject)


# In[15]:


student = ["Ravi", 34, "CS"]

name, age, subject = student     #efficient, Unpacking Tuple

print(name)
print(age)
print(subject)


# In[20]:


def get_student():     #function can return tuple
    return("Ravi", 34, "EC")    #If another value is added then >> ValueError: too many values to unpack (expected 3)

name, age, subject = get_student()

print(get_student())


# In[21]:


#tuples within list

family = [("Ravi", 34), ("Aniketh", 1), ("Chaitra", 30)]

for name, age in family:
    print(name)
    print(age)


# In[ ]:





# In[ ]:




