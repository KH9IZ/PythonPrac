ma = [list(eval(input()))]
n = len(ma[0])

for i in range(1, n):
    ma.append(list(eval(input())))

mbT = [[] for _ in range(n)]
for _ in range(n):
    for i, j in enumerate(eval(input())):
        mbT[i].append(j)

mc = []
for rowa in ma:
    new_row = []
    for colb in mbT:
        new_row.append(sum(rowa[k] * colb[k] for k in range(n)))
    mc.append(new_row)

for row in mc:
    print(row)
