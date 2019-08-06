"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above one million."""
import time
start = time.time()
k = []
def func(n):
    t = [n]
    for i in t:
        if i%2 == 0:
            even = i/2
            t.append(int(even))
        else:
            if t[-1] != 1:
                odd = (3*i)+1
                t.append(int(odd))
            else:
                break
    return k.append([len(t),n])
for num in range(1,1000001):
    func(int(num))
print(max(k))
print(time.time() - start)