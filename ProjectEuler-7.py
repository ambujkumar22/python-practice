"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""

t = []
for i in range(2,1000000):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        t.append(i)
print(t[9999])
