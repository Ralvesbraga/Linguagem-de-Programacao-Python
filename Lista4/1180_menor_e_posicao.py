n = int(input())
x = input().split()
y = []
for i in x:
    y.append(int(i))
menor = y[0]
pos = 1
for i in range(1, n):
    if y[i] < menor:
        menor = y[i]
        pos = i
print(f'Menor valor: {menor}')
print(f'Posicao: {pos}')
