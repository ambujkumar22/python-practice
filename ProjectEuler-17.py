"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""

def func():
    ten = [3,3,5,4,4,3,5,5,4]
    teen = [3,6,6,8,8,7,7,9,8,8]
    tens = [6,6,5,5,5,7,6,6]
    tentotal = 0
    for i in ten:
        tentotal += i
    teentotal = tentotal
    for j in teen:
        teentotal += j
    tenstotal = teentotal
    for k in tens:
        tenstotal += 10*k
    total = tenstotal + 8*tentotal

    overall = tentotal*100 + total*10 + 7*900 + 3*891 + 11
    return overall
print(func())
