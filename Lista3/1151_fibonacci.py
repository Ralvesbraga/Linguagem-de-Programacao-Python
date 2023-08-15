n = int(input())
ant1 = 1
ant2 = 1
print('0 1 1', end=" ")
for i in range(4, n + 1):
    atual = ant1 + ant2
    if i == n:
        print(atual)
    else:
        print(atual, end=" ")
        ant1 = ant2
        ant2 = atual
