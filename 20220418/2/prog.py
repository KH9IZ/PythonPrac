eps = 1e-11

class SquareIO:
    def inputCouff(name):
        return input(f"Input {name}: ")

    def printResult(result):
        return print(f"Soluton: {result}")

def solveSquare(a, b, c):
    discr = b**2 - 4*a*c
    if -eps < discr < eps:
        return (-b / (2 * a), ) * 2
    if discr > 0:
        x1 = (-b - discr**0.5) / (2 * a)
        x2 = (-b + discr**0.5) / (2 * a)
        return min(x1, x2), max(x1, x2)
    else:
        return None

def solve():
    a = int(SquareIO.inputCoeff('a'))
    b = int(SquareIO.inputCoeff('b'))
    c = int(SquareIO.inputCoeff('c'))
    if a == 0 and b != 0:
        x = -c / b
    elif a != 0:
        x = solveSquare(a, b, c)
    else:
        x = None
    SquareIO.printResult(x)
