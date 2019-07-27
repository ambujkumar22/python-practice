#The prime factors of 13195 are 5, 7, 13 and 29.What is the largest prime factor of the number 600851475143 ?
import time
start_time = time.time()
n = 600851475143
i = 2
t = []
while i * i < n:
     while n % i == 0:
         n = n / i
         t.append(n)
     i = i + 1

print (t[-1])
print(time.time() - start_time,"seconds")