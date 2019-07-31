#!/usr/bin/env python
# coding: utf-8

# In[12]:


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
    
book = PhoneBook()
book.add("Ravi", "123456")
book.add("Aniketh", "56789")
# book.__entries = {}  >> doesnt work as it is made private.
print(book.get("Ravi"))


# In[ ]:




