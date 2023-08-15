n = int(input())
for i in range(n):
    p, m = map(int, input().split())
    k = 0
    v1 = []
    cont =0
    for j in range(p+1):
        v1.append(j)
    print(v1)
    v2 = []
    while True:
        k += m
        v2.append(k)
        if k > p:
            k = 1
        if len(v1) == 2:
            break
    print(v1)
