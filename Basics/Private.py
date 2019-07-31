#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Student():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__term = 1
    
    def increase_term(self):
        if self.__term >= 9:
            return
        self.__term += 1
        
    def get_term(self):
        return self.__term
    
    def name(self):
        print(self.firstname + " " + self.lastname + " is in semester " + str(self.__term))
        
    def _do_something(self):   # single underscore >> informs developers not to use this or over right this value, but is accessible.
        print("Tarsar")
        
 #   def __do_some(self):   # double underscore used and tried to access from outside. checkout the error.
 #    print("Tarsar")
    
abc = Student("Ravindra", "Joisa")
abc.increase_term()
abc.__term = 100          # trying to set term to 100, but not possible. double underscore >> private. It can only be called from class where it was created.
print(abc.__term)
abc.name() 
abc._do_something()
#abc.__do_some()    # # 'Read only' of private member. AttributeError: 'Student' object has no attribute '__do_some'
print(abc.get_term())  # 'Read only' of private member


# In[ ]:





# In[ ]:




