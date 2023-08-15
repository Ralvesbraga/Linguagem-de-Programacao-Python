while True:
    n = int(input())
    if n == 0:
        break
    v1 = list(map(int, input().split()))
    v2 = []
    for i in range(n):
        if v1[i] in v2:
            v2.remove(v1[i])
        else:
            v2.append(v1[i])
    print(*v2)
