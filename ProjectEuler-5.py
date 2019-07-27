"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
import time
start_time = time.time()
t = []

for j in range(1,1000000000):
    if j%1 == 0 and j%2 == 0 and j%3 == 0 and j%4 == 0 and j%5 == 0 and j%6 == 0 and j%7 == 0 and j%8 == 0 and j%9 == 0 and j%10 == 0 and j%11 == 0 and j%12 == 0 and j%13 == 0 and j%14 == 0 and j%15 == 0 and j%16 == 0 and j%17 == 0 and j%18 == 0 and j%19 == 0 and j%20 == 0:
        t.append(j)
        break
    else:
        continue

print(t)
print(time.time() - start_time,"seconds")
