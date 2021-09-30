l = list(eval(input()))

for i in range(len(l)):
    for j in range(1, len(l) - i):
        if l[j] ** 2 % 100 < l[j-1] ** 2 % 100:
            l[j], l[j-1] = l[j-1], l[j]

print(l)
