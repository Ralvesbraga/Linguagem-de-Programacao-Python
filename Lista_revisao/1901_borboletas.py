n = int(input())
v1 = [0] * 1001
mat = []
mat2 = []
result = 0
ind = []
for i in range(n):
    linha = input().split()
    mat.append(linha)
for i in range(2*n):
    lin, col = input().split()
    lin = int(lin)
    col = int(col)
    ind.append(mat[lin - 1][col - 1])
for i in ind:
    v1[int(i)] += 1
for i in range(1001):
    if v1[i] > 0:
        result += 1
print(result)
