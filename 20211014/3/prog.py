top = input()[1:-1]
w = len(top)
s = input()[1:-1]
gas = 0
liquid = 0
while(s != top):
    if s[0] == '.':
        gas += w
    elif s[0] == '~':
        liquid += w
    s = input()[1:-1]
v = gas + liquid
h = v // w

print('#' * (h + 2))
for i in range(gas // h):
    print(f"#{'.' * h}#")

for i in range(w - gas // h):
    print(f"#{'~' * h}#")
print('#' * (h + 2))

if liquid > gas:
    l_len = 20
    g_len = round(20 * gas / liquid)
    kl = f"{liquid}/{v}"
    kg = f"{gas}/{v}"
    l_s = f"{'~' * l_len} {kl}"
    g_s = f"{'.' * g_len}{kg:>{len(l_s)-g_len}}"
else:
    g_len = 20
    l_len = round(20 * liquid / gas)

    kl = f"{liquid}/{v}"
    kg = f"{gas}/{v}"
    g_s = f"{'.' * g_len} {kg}"
    l_s = f"{'~' * l_len}{kl:>{len(g_s) - l_len}}"

s1 = f"{gas}"

print(g_s)
print(l_s)

