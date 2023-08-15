n = int(input())
x = []
quantia = [0] * 3
for i in range(n):
    x = input().split()
    if x[1] == 'C':
        quantia[0] = quantia[0] + int(str(x[0]))
        x.clear()
    elif x[1] == 'R':
        quantia[1] = quantia[1] + int(str(x[0]))
        x.clear()
    else:
        quantia[2] = quantia[2] + int(str(x[0]))
        x.clear()
soma = 0
for i in range(3):
    soma = soma + quantia[i]
print(f'Total: {soma} cobaias')
print(f'Total de coelhos: {quantia[0]}')
print(f'Total de ratos: {quantia[1]}')
print(f'Total de sapos: {quantia[2]}')
print('Percentual de coelhos: {:.2f} %'.format((quantia[0] / soma) * 100))
print('Percentual de ratos: {:.2f} %'.format((quantia[1] / soma) * 100))
print('Percentual de sapos: {:.2f} %'.format((quantia[2] / soma) * 100))
