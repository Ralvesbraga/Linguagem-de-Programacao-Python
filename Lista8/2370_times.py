a, t = map(int, input().split())
jogadores = {}
cont = 0
times = []
for i in range(a):
    jog, hab = input().split()
    jogadores.update({int(hab): jog})
    jogadores_ordenados = {}
print(times)
jogadores_ordenados = sorted(jogadores.items(), reverse=True)
print(jogadores_ordenados)
for i, j in jogadores_ordenados:
    if cont == 3:
        cont = 0
    times.append(tuple())
    cont += 1
