n = int(input())
x = input().split()
y = []
cont = 0
for i in x:
    y.append(int(i))
cont = 0
num = 0
for i in range(n):
    if cont < y.count(y[i]):
        cont = y.count(y[i])
        num = y[i]
    elif cont == y.count(y[i]):
        if y[i] > num:
            num = y[i]
print(num)
