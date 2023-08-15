n = int(input())
cartas = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
conta_a_vitorias = 0
conta_b_vitorias = 0
pb = 0
pa = 0
for a in range(n):
    cartas_jogadas = input().split()
    pontos = []
    pa = 0
    pb = 0
    for i in range(10):
        for j in range(3):
            if cartas_jogadas[j] == cartas_jogadas[3 + j]:
                pa += 1
                break
            if cartas_jogadas[j] == cartas[i]:
                pontos.append(i)
            if cartas_jogadas[j + 3] == cartas[i]:
                pontos.append(i)
    print(pontos)
    if pa > pb:
        conta_a_vitorias = conta_a_vitorias + 1
    else:
        conta_b_vitorias = conta_b_vitorias + 1
print(f'{conta_a_vitorias} {conta_b_vitorias}')
