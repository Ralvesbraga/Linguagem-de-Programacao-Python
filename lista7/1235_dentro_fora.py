n = int(input())
for j in range(n):
    frase = list(input())
    esq = ''
    dire = ''
    tamanho = len(frase)
    cont = 0
    for i in range(0, tamanho//2):
        esq += frase[(tamanho//2) - i - 1]
        dire += frase[tamanho - i - 1]
    print(esq+dire)
