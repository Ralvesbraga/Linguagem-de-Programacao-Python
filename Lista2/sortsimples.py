n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
lista = [n1, n2, n3]


def crescente(x):
    x.sort()
    for elem in x:
        print(elem)


print(crescente(lista))



