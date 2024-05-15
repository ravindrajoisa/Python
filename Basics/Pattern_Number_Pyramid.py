""" Number pyramid pattern
   1
  232
 34543
4567654

Pseudocode:
1.There are N rows.
2. In each row there are N-i space
3. ith rows has i Nos in the increasing order on
    left side starting from a value i
4. i-1 No's in the decreasing orders.

"""

# N = int(input())
N = 4
i = 1
while i <= N:
    #spaces
    spaces = 1
    while spaces <= N-i:
        print("*")
        spaces = spaces + 1 
    
    #left side of pyramid, increasing numbers
    val = i
    count = 1
    while count <=i:
        print(val, end="")
        val += 1
        count += 1
    
    #right side of pyramid, decreasing numbers
    #reset the value to value-2
    val = val - 2
    count = 1
    while count <= i-1:
        print(val, end="")
        val = val - 1
        count = count + 1

    print()
    i += 1

#CODE WITH DEFECTS - TO BE FIXED