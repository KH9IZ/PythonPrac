import sys

inb = sys.stdin.buffer.read
outb = sys.stdout.buffer.write

n = inb(1)
outb(n)
n = n[0]
s = inb()
for i in range(n):
    ...
