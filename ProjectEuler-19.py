"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

index = [31,28,31,30,31,30,31,31,30,31,30,31]
t = []
days = 0
for i in range(1900,2001):
    for j in range(0,12):
        days += index[j]
        for k in range(7,index[j], 7):
            t.append(k)
print(t)



