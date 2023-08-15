matriz = []
soma = 0
deno = 0
op = input()
for i in range(12):
    linha = []
    for j in range(12):
        x = float(input())
        linha.append(x)
        if j > i:
            soma = soma + x
            deno += 1
    matriz.append(linha)
if op == 'S':
    print(f'{soma:.1f}')
elif op == 'M':
    print(f'{soma / deno:.1f}')
