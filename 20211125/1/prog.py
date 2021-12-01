import sys

n = sys.stdin.buffer.read(1)[0]
sys.stdout.buffer.write(bytes([n]))

b = sys.stdin.buffer.read()
l = len(b)
parts = [b[i*l//n : (i+1)*l//n] for i in range(n)]
sys.stdout.buffer.write(b''.join(sorted(parts)))
