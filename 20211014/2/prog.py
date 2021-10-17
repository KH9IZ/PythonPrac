from math import *

inpt = input().split(' ')
w = int(inpt[0])
h = int(inpt[1])
a = float(inpt[2])
b = float(inpt[3])
f = lambda x: eval(' '.join(inpt[4:]))



def scale(A, B, a, b, x):
    return (x - A) / (B - A) * (b - a) + a

X = [scale(0, w, a, b, i) for i in range(w+1)]
Y = [f(x) for x in X]
my, My = min(Y), max(Y)

desc_Y = [round(scale(my, My, 0, h-1, y)) for y in Y]
pred = desc_Y[0]

field = [ [' ' for col in range(w)] for row in range(h)]
for x, y in enumerate(desc_Y[1:], 1):
    delta = y - pred  
    field[pred][x-1] = '*'
    iter = range(0, delta) if y >= pred else range(delta+1, 1)
    for i in iter:
        field[pred+i][x-1] = '*'
    pred = y


for y in field[::-1]:
    print(*y, sep='')

