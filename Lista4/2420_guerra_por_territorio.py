n = int(input())
x = input().split()
y = []
soma = 0
for i in range(len(x)):
    y.append(int(x[i]))
    soma = soma + y[i]
pare = soma/2
soma = 0
for i in range(len(y)):
    if soma == pare:
        print(i)
        break
    else:
        soma = soma + y[i]
