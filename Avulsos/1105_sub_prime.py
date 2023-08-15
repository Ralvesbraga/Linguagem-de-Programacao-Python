while True:
    b, n = map(int, input().split())
    if b == n == 0:
        break
    saldo = list(map(int, input().split()))
    denbetures = []
    for i in range(n):
        d, c, vlr = map(int, input().split())
        saldo[d-1] -= vlr
        saldo[c-1] += vlr
    if min(saldo) < 0:
        print('N')
    else:
        print('S')
