eps = 1e-11

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
