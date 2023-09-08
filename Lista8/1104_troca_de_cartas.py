while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    va = input().split()
    vb = input().split()
    seta = set(va)
    setb = set(vb)
    vc = list(seta) + list(setb)
    vd = set(vc)
    dif = len(vc) - len(vd)
    if len(seta) >= len(setb):
        print(len(setb) - dif)
    else:
        print(len(seta) - dif)
