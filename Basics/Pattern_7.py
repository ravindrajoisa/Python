"""
Reverse Hill pattern

* * * * * * * * *
  * * * * * * * 
    * * * * *
      * * *
        *
"""
n = 5 #rows

for i in range(n):  
    for j in range(i):
        print(" ", end=" ")
    
    for j in range(n-i):
        print("*", end=" ")

    for j in range(n-i-1):
        print("*",end=" ")

    print()