from itertools import islice, chain
def slide(seq, n):
    seq = iter(seq)
    t = list(islice(seq, n))
    yield from t
    while (n := list(islice(seq, 1))):
        yield from (t := (t[1:] + n))
import sys
exec(sys.stdin.read())
