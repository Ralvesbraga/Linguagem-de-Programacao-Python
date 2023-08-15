pal = list(input())  ## transformo toda a frase em um vetor, separado por letras (onde cada letra é um indice do vetor, inclusive o espaço)
cont = 0 ## variavel para contar os espaços e subtrair do indice
semp = []
for i in range(len(pal)):   ## vai rodar o vetor todin
    if (i - cont) % 2 == 1:  ## as letrs que quero que sejam armazenadas em semp, sempre estão no indice par (sem contar os espaços, por isso o i - cont)
        semp += pal[i]       ## as letras serão armazenadas aqui
    elif pal[i] == ' ':      ## se for um espaço, armazena tbm
        semp += pal[i]
        cont += 1            ## conta os espaços
print(*semp, sep='')         ## saida formatada, sem as virgulas e os []
