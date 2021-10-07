def Pareto(*pairs):
    result = []
    for x, y in pairs:
        for a, b in pairs:
            if (x <= a and y <= b) and (x < a or y < b): 
                break
        else:
            result.append((x,y))
    return tuple(result)
