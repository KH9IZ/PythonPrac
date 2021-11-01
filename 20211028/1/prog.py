def fib(m, n):
    a, b = 1, 1
    for i in range(0, n+1):
        if i >= m: 
            yield a
        a, b = b, a+b
import sys
exec(sys.stdin.read())
