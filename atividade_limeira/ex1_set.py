lista1 = input().split()
lista2 = input().split()
set1 = set(lista1)
set2 = set(lista2)
print(len(set1 & set2))
print((len(lista1) - len(set1)) + (len(lista2) - len(set2)))
print(len(set1 ^ set2))