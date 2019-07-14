#!/usr/bin/env python
# coding: utf-8

# In[4]:


#String >> integers (whole number)

a = "5"
b = "6"
print(a+b)
print(int(a) + int(b))


# In[6]:


#String >> Float

a = "5.5"
b = "6.5"
print(a+b)
print(float(a)+float(b))


# In[11]:


#Integer to String

age = 34
print("I am " + str(age) + " years old.")


# In[20]:


#List >> String >> using 'join'

students = ["Ravi", "Aniketh"]
print(students)
print(", " .join(students))
students_as_string = ", " .join(students)
print ("My friends: " + students_as_string)


# In[30]:


#String >> List >> using 'split'

i = "Chai, Mani, Ravi"
print(i.split(","))
print("Total number of students: " + str(len(i.split(","))))


# In[ ]:




