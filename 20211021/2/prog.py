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
        fs[f] = (e, v)
    elif s.split()[0] == 'quit':
        print(len(fs) + 1)
        break
    else:
        s = s.split()
        e = fs[s[0]][0]
        v = fs[s[0]][1]
        print(eval(e, math.__dict__, {v: eval(' '.join(s[1:]))}))
