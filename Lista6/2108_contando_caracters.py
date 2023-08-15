maior = 0  ## variavel que vai mostrar quem tem a maior palavra
maior_pav = ''  ## variavel que vai armazenar a maior palavra
while True:
    pavs = input().split()  ## entrada com as palavras
    if pavs[0] == '0':  ## se for igual a '0', ocoore o break e mostra qual foi a maior palavra
        print('\nThe biggest word: {}'.format(maior_pav))
        break
    qnt_let = []  # vetor que armazena a quantidade de letras de cada palavra
    for i in pavs:
        qnt_let.append(len(i))  ## adiciona usando o len
        if len(i) >= maior:  ## a palavra de maior len será armazenado em maior_pav, e o maior será atualizado
            maior_pav = i
            maior = len(i)
    print(*qnt_let, sep='-', end='')  ## saida formatada tirando as virgulas, os [], e colocando os separadores '-'
    print()
