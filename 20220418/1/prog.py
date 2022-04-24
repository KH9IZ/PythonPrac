def solveSquare(a, b, c):
    discr = b**2 - 4*a*c
    if discr >= 0:
        x1 = (-b - discr**0.5) / (2 * a)
        x2 = (-b + discr**0.5) / (2 * a)
        return sorted(x1, x2)
    else:
        return None
