def code(n):
        t = []
        i = 1
        while i*i <= n:
                if n%i == 0:
                        t.append(i)
                        if n//i != i:
                                t.append(n//i)
                i += 1
        return sorted(t)

print(code(12))