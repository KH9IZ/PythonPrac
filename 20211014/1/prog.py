from fractions import *
s = input()


s, w, pow_A, *tmp = s.split(',')
pow_A = int(pow_A)
A = tmp[:pow_A + 1]
pow_B = int(tmp[pow_A + 1])
B = tmp[pow_A + 2:]

s = Fraction(s)
w = Fraction(w)
A = [Fraction(i) for i in A]
B = [Fraction(i) for i in B]


A_s = sum(s ** i * k for i, k in enumerate(A[::-1]))
B_s = sum(s ** i * k for i, k in enumerate(B[::-1]))
print(A_s / B_s == w if B_s else False)

