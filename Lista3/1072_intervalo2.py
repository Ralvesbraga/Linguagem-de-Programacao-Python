n = int(input())
dento = 0
fora = 0
for i in range(1, n + 1):
    x = int(input())
    if 10 <= x <= 20:
        dento = dento + 1
    else:
        fora = fora + 1
print(f'{dento} in')
print(f'{fora} out')
