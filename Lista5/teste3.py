while True:  # como são infinitos casos de testes, tem que usar o while true (loop infinito)
    try:  # como tava dando uns eoferror no codigo, coloquei um try except para evita-lo
        n = int(input())  # n recebe a quantidade de suspeitos
        if n == 0:  # se n = 0, ocorre o fim do laço infinito
            break
        suspeitos = list(map(int, input().split()))  # ocorre a segunda entrada com a lista dos suspeitos
        copia = suspeitos.copy()  # fiz uma copia de suspeitos para compara-la depois com a original
        suspeitos.sort()  # ordenei a lista, então o mais suspeito é o ultimo, então o segundo é o penultimo
        for i in range(n):  # faço um for para rodar a lista original de suspeitos (copia) e quando achar o segundo maior suspeito(o penultimo, ele printa o indice em que achou ele)
            if suspeitos[n - 2] == copia[i]:
                print(i + 1)
    except EOFError:
        break
