v, p = map(int, input().split())
tot = v * p
c = 0
for i in range(10, 91, 10):
    if i == 90:
        if int(tot * i/100) != tot * i/100:
            print((int(tot * i / 100) + 1))
        else:
            print(int(tot * i/100))
    else:
        if int(tot * i/100) != tot * i/100:
            print((int(tot * i / 100) + 1), end=' ')
        else:
            print((int(tot * i/100)), end=' ')
