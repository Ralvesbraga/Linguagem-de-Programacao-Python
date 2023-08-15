n = int(input())    # n recebe a quantidade de espaços, slots, de figurinhas que o album tem
slots = [0] * n  # aqui eu declaro um vetor do tamanho dos espaços, e nesse vetor, cada indice corresponderá a figurinha digitada em slots
qnt_figs = int(input())  # aqui já é a segunda entrada, especificando quantas figurinhas o cara irá entrar
cont = 0  # o cont é declarado para armazenar a quantidade de figurinhas diferentes foram digitadas
for i in range(qnt_figs):
    slots[int(input()) - 1] += 1    # aqui o problema vai entrar com as figurinhas e cada figurinha corresponde a posição do vetor, e cada posição irá receber um acrescimo de + 1
for i in range(n):
    if slots[i] > 0:    # ja aqui, irei percorrer todo o vetor, e o cont irá acrescentar +1 para cada valor que seja maior que zero, assim so conta a quantidade de valores digitados sem repetição
        cont += 1
print(n - cont)     # aqui é printado o valor total de espaços menos a quantidade de figurinhas diferentes inseridas
