import time
start_time = time.time()

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp,nums[j] = nums[j],nums[j+1]
                nums[j+1] = temp

nums = [2,6,7,1,3,10,18,13,20,15]
sort(nums)
print(nums)

print("--- %s seconds ---" % (time.time() - start_time)) 