n = int(input())
x = input().split()
y = []
queda = 0
for i in x:
    y.append(int(i))
ant = y[0]
for i in range(1, n):
    if y[i] < ant:
        if queda == 0:
            queda = i + 1
    ant = y[i]
print(queda)
