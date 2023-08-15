n = int(input())
c = 0
mat = []

for i in range(n):
    a = list(map(int, input().split()))
    mat.append(a)
mat.sort()
for i in range(n):
    if i == 0:
        f = mat[0][1]
        c = 0
    if i > 0:
        i2 = mat[i][0]
        f2 = mat[i][1]
        if f2 > f:
            c += 1
            i = i2
            f = f2
print(c)
