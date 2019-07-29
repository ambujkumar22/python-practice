"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

def func(n):
    i = 3
    while i < n:
        if all(i % j != 0 for j in range(3,i,2)):
            yield i
        i += 2

iter = 2
function = func(2000000)
for x in function:
    iter += int(x)

print(iter)