import sys

sys.setrecursionlimit(2500)

def fact(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * fact(n-1)

print(fact(50))