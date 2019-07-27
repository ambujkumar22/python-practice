#multiplies of 3 and 5
nums = []
for i in range(1,1000):
    if i%3 == 0:
        nums.append(i)
    elif i%5 == 0:
        nums.append(i)

sum = sum(nums)
print(sum)
