tupla1 = tuple(input())
tupla2 = tuple(input())
palavra = ''
resultado = ''
lista1 = list(tupla1)
lista2 = list(tupla2)
if len(tupla1) <= len(tupla2):
    tamanho = len(tupla1)
    palavra = ''.join(lista2)
else:
    tamanho = len(tupla2)
    palavra = ''.join(lista1)
for i in range(tamanho):
    resultado += tupla1[i]
    resultado += tupla2[i]
print(*tuple(resultado + palavra[tamanho:]), sep='')
