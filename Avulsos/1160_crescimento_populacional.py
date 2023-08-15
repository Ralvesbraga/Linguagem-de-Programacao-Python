n = int(input())
for i in range(n):
    pa, pb, ta, tb = map(float, input().split())
    anos = 0
    while pa <= pb:
        pa = pa + int(pa * ta/100)
        pb = pb + int(pb * tb/100)
        anos += 1
        if anos > 100:
            break
    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{anos} anos.')
