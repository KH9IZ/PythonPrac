import math

cntr = 0
fs = {'quit': ('print(formats.format(len(fs), cntr)) or quit()', 'formats')}

while True:
    s = input()
    cntr += 1
    if s.startswith(':'):
        name, *vals, expression = s.split()
        name = name[1:]
        fs[name] = (expression, *vals)
    else:
        name, *vals = s.split()
        expr, *v_names = fs[name]
        t = eval(expr, math.__dict__ | {'fs': fs, 'cntr': cntr}, {name: eval(val, math.__dict__) for name, val in zip(v_names, vals)})
        print(t)
