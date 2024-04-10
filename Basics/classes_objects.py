class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
        
    def myfunc(self):
        print("Hello my name is "+  self.name)
        
p1 = Person("Ravi", 39)
p1.myfunc()
print(p1)
print(p1.name)
print(p1.age)