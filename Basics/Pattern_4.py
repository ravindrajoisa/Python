"""
        *
      * *
    * * *
  * * * *
* * * * * 
"""

n = 5
for i in range(n): #rows
    for j in range(i, n): #columns - 1st | triangle
      print("|", end="  ")

    for j in range(i+1):  #columns - 2nd * triangle
       print("*", end="  ")

    print()