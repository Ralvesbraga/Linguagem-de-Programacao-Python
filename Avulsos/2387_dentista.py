n = int(input())
consultas = []
atendimentos = 0
for i in range(n):
    entrada = []
    antI, antF = map(int, input().split())
    entrada.append(antF)
    entrada.append(antI)
    consultas.append(entrada)
consultas.sort()
antI = consultas[0][1]
antF = consultas[0][0]
for i in range(1, n):
    if consultas[i][0] >= antI:
        atendimentos += 1
        antI = consultas[i][1]
print(consultas)
print(atendimentos)

