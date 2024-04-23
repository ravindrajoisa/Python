"""
* * * * * 
  * * * *
    * * *
      * *
        * 
"""

n = 5
for i in range(n): #rows
    for j in range(i): #columns - 1st | triangle
      print("|", end="  ")

    for j in range(i, n):    #(n-i)
      print("*", end="  ")  #column - 2nd * triangle

    print()