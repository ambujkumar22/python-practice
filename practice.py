import time
start_time = time.time()

def trianglenum():
        t = []
        for n in range(1,1000000):
                sum = n*(n+1)/2
                t.append(int(sum))
                for j in t:
                        k = []
                        i = 1
                        while i*i <= j:
                                if j%i == 0:
                                        k.append(i)
                                        if j//i != i:
                                                k.append(j//i)
                                i += 1
                if len(k) >= 500:
                        print(int(sum))
                        break
                else:
                        t.clear()
                        k.clear()

trianglenum()
print(time.time() - start_time)