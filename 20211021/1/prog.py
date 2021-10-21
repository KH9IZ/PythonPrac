s = input()

st = set()
for i, j in zip(s[1:], s[:-1]):
    p = (i+j).lower()
    if p.isalpha():
        st.add(p)
print(len(st))

