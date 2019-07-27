import time
start_time = time.time()

index = [3,22,7,5,10,11,15,20]
inde = sorted(index)

def func(num):
    pos = 0
    l = 0
    u = len(inde) - 1
    while l <= u:
        mid = (l+u)//2
        if inde[mid] == num:
            pos = mid
            return True,pos
        else:
            if inde[mid] < num:
                l = mid + 1
            else:
                u = mid - 1
    return False

print(inde)
number = int(input('> '))
thing,pos = func(number)

if thing:
    print('Found at',pos+1)
else:
    print('Not Found')


print("--- %s seconds ---" % (time.time() - start_time))