# Exercise 1:
# Randomly generate two lists and find common items in these lists. 
# Create a new list with the items in common. Avoid having duplicates in the new list. 

import random

x = []
y = []
z = []

for i in range(20):
    x.append(random.randrange(1,30)) #creates random list 1
    y.append(random.randrange(1,30)) #creates random list 2
print(x)
print(y)

for i in y:
   if (i in x) and (i not in z): #Finds a common number. Prevents duplicates.
   z.append(i) 
print(z) # Displays new list of common items without duplicates.
