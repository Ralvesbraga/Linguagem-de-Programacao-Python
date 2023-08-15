x = int(input())  # a variavel X, recebe qual coluna ele quer que seja feita a soma
op = input()  # a variavel op recebe a Letra S de soma ou M de média, a operação que ele quer que seja feito
matriz = []  # declaro a matriz que vai receber as linhas
soma = 0  # declaro a variavel soma que irá armazenar toda a coluna que o X vai direcionar
for i in range(12):  # construo toda a estrutura do preenchimento da matriz com dois for de tamanho 12, que é o valor dado no problema
    linha = []  # declaro no primeiro for a linha, pois toda vez que ela juntar os valores e adicionar na variavel matriz, ela irá se resetar
    for j in range(12):
        linha.append(float(input()))  # aqui será adicionado no vetor linha as entradas que o problema vai por
        if j == x:
            soma = soma + linha[j]  # crio uma condição que toda vez que a coluna(j) for igual a X(o valor da coluna que ele quer eu some) eu some os valores
    matriz.append(linha)  # terminando de preencher uma linha ela é armazenada na variavel matriz, para poder resetar a linha novamente depois.
if op == 'S':  # se o operador que ele digitou for igual a S, so printará o valor da soma que foi feita nos dois paras anteriores
    print('{:.1f}'.format(soma))
if op == 'M':  # se o operador for igual a M, então vai pegar a variavel soma e vai divir pela quantidade de somas que foi feita, que é igual a quantidade de linhas da matriz (12)
    print('{:.1f}'.format(soma/12))
