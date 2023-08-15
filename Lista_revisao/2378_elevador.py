n, c = input().split()
n = int(n)
c = int(c)
soma = 0
cont = 0
result = 'N'
for i in range(n):
    s, e = input().split()
    s = int(s)
    e = int(e)
    soma = soma + e - s
    if soma > c:
        result = 'S'
print(result)
