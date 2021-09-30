#l, r = eval(input())
print([i for i in range(*(eval(input()))) if all(i % j for j in range(2, i))])
