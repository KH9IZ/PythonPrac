class InvalidInput(Exception): pass
class BadTriangle(Exception): pass

def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except Exception as E:
        raise InvalidInput from E
    
    try:
       s = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2 
       1 / s
    except (TypeError, ZeroDivisionError) as E:
        raise BadTriangle from E
    return s

while True:
    s = input()
    try:
        s = triangleSquare(s)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{s:.2f}")
        break
