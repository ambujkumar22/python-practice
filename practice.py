"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""

a = [x for x in range(2,1000000) if all(x%y != 0 for y in range(2,x))]
print(a[10000])