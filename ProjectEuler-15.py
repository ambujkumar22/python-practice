"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?"""
n = 1
for i in range(40,1,-1):
    n *= i
r = 1
for j in range(20,1,-1):
    r *= j
diff = 1
for k in range(20,1,-1):
    diff *= k

combination = n/(diff*r)

print(int(combination))
