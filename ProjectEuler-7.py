"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?"""
def prime(n):
    prime = [2]
    attempt = 3
    while len(prime) < n:
        if all(attempt % i != 0 for i in prime):
            prime.append(attempt)
        attempt += 2
    return prime[-1]
print(prime(6))
