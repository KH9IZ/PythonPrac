import sys

bnopnya = input()
print(bnopnya.encode('latin1', errors='replace').decode('cp1251', errors='replace'))
