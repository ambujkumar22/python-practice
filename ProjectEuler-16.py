"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""

def powerfunc(power):
    num = 2**power
    total = 0
    for i in range(len(str(num))):
        total += int(str(num)[i])
    return total

print(powerfunc(1000))
