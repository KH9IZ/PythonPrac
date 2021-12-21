from itertools import islice, chain, tee

def slide(seq, n):

    for i, el in enumerate(tee(seq, len(seq))):
        yield from islice(el, i, i + n)

import sys
exec(sys.stdin.read())
