n = int(input())

i = n
while i < n + 3:
    j = n
    while j < n + 3:
        mul = (tmp := i * j)
        dsum = 0
        while tmp:
            dsum += tmp % 10
            tmp //= 10
        if dsum == 6:
            mul = ':=)'
        print(f"{i}*{j}={mul}", end=' ')
        j += 1
    i += 1
    print()             
