import math
fs = {}
vals = {}
while True:
    s = input()
    if s.startswith(':'):
        s = s.split()
        f = s[0][1:]
        v = s[1]
        e = ' '.join(s[2:])  # Возможны ошибкИ?
        fs[f] = lambda x: eval(e, math.__dict__, {v: x})
    elif s.split()[0] == 'quit':
        print(len(fs) + 1)
    else:
        s = s.split()
        print(fs[s[0]](eval(s[1])))
