partidas = int(input())
cartas = ['4', '5', '6', '7', '12', '11', '13', '1', '2', '3']
conta_a_partidas = 0
conta_b_partidas = 0
for i in range(partidas):
    cartas_jogadas = input().split()
    pontos = []
    pa = 0
    pb = 0
    cont = 0
    for j in range(3):
        pontos.append(cartas.index(cartas_jogadas[j]))
        pontos.append(cartas.index(cartas_jogadas[3 + j]))
        if pontos[j + cont] >= pontos[j + 1 + cont]:
            pa += 1
        else:
            pb += 1
        cont += 1
    if pa > pb:
        conta_a_partidas += 1
    else:
        conta_b_partidas += 1
print(f'{conta_a_partidas} {conta_b_partidas}')
