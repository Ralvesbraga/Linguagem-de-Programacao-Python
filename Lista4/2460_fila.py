n = int(input())
a = input().split()
n2 = int(input())
b = input().split()
cont = 0
indice = []
for i in range(n2):
    a.remove(b[i])
for i in range(len(a)):
    if i == len(a) - 1:
        print(int(a[i]))
    else:
        print(int(a[i]), end=' ')
