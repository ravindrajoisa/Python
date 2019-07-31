#!/usr/bin/env python
# coding: utf-8

# In[8]:


class PhoneBook(): 
    
    def __init__(self):
        self.__entries = {}
    
    def add(self, name, phone_number):
        self.__entries[name] = phone_number
    
    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None
    
    def __str__(self):
        return "Phonebook (" + str(self.__entries) + ")"
        
    def __repr__(self):
        return "Phonebook (" + str(self.__entries) + ")"
    
#str() is used for creating output for end user while repr() is mainly used for debugging and development. ...
#The print statement and str() built-in function uses __str__ to display the string representation of the object 
#while the repr() built-in function uses __repr__ to display the object.

    def __len__(self):
        return len(self.__entries)
    
book = PhoneBook()
book.add("Ravi", "123456")
book.add("Aniketh", "56789")

print(book)
print(len(book))


# In[6]:


book


# In[ ]:




