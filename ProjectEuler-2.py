import time
start_time = time.time()

t = [1,2]

a = 1
b = 2

for i in range(2,100):
    c = a + b
    a,b = b,c
    if c > 4000000:
        break
    else:
        t.append(c)


x = []
for i in t:
    if i%2 == 0:
        x.append(i)

print(sum(x))
print(time.time() - start_time)