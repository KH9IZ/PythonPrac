from collections import Counter
import sys
n = int(input())

cntr = Counter()
while s := sys.stdin.read():
    s = ''.join(c.lower() if c.isalpha() or c.isspace() else ' ' for c in s)
    words_n = [word for word in s.split() if len(word) == n]
    cntr.update(words_n)
t = max(cntr.values(), default=0)
l = []
for el, cnt in cntr.most_common():
    if cnt < t:
        break
    l.append(el)
if l:
    print(*sorted(l))
