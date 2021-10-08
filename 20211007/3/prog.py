def Bisect(el, seq):
    l = len(seq)
    check_num = l // 2 - (l % 2 == 0)
    if l == 0:
        return False
    elif el == seq[check_num]:
        return True
    else:
        return Bisect(el, seq[:check_num] if el < seq[check_num] else seq[check_num+1:])

print(Bisect(*eval(input())))
