import time
start_time = time.time()

index = [10,4,1,14,12,9]

def func(num):
    pos = 0
    for i in index:
        if i == num:
            return True,pos
        pos += 1
    else:
        return False


number = 10
thing,pos = func(number)

if thing:
    print('Found at',pos+1)
else:
    print('Not Found')


print("--- %s seconds ---" % (time.time() - start_time))