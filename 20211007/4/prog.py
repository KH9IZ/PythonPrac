from math import *

def Calc(s, t, u):
    def ret(x):
        tmp = eval(s)
        y = eval(t)
        x = tmp
        return eval(u)
    return ret

F = Calc(*eval(input()))
print(F(eval(input())))
