from itertools import product
print(*list(filter(lambda s: s.count('TOR') == 2, (''.join(t) for t in product('ORT', repeat=int(input()))))), sep=', ')
