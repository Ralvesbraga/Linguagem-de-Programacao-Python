while True:  # fiz um loop infinito com o try except, pois o problema diz que termina com eoferror
    try:
        n = int(input())  # n recebe o tamanho da matriz que o problema quer que seja feito
        matriz = []  # novamente declaro a matriz fora do laço, pois nela será armazenado os valores
        for i in range(n):
            linha = []  # declaro a linha dentro do primeiro laço, pois ela irá ser resetada toda vez que o laço se reiniciar
            for j in range(n):
                if j == (n - i - 1):  # se vc desenhar a matriz no caderno, irá perceber que a matriz secundaria é repleta de número 2, então fiz essa condição: tamanho da matriz menos a posição da linha - 1
                    linha.append(2)  # a linha nessa posição, receberá o valor 2
                elif j == i:  # novamente, se atendo ao desenho irá perceber que a matriz principal é repleta de 1, então essa condição de que toda vez que o j for igual ao i, a linha nessa posição receberá 1
                    linha.append(1)
                else:
                    linha.append(3)  # se não for nenhuma das duas anteriores, o problema quer que seja preenchido por 3, então assim é feito
            matriz.append(linha)
        for i in range(n):  # aqui faço toda a estrutura para printar a matriz posição por posição de acordo com o tamanho n dado
            for j in range(n):
                print(matriz[i][j], end="")
            print()
    except EOFError:
        break
