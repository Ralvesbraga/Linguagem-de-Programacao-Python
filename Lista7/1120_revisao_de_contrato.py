while True:
    v1 = list(input())
    n = v1[0]
    if n == v1[0] == '0':
        break
    qnt = v1.count(n)
    for i in range(qnt):
        v1.remove(n)
    resultado = ''
    for i in v1:
        resultado += i
    if resultado == ' ':
        print(0)
    else:
        print(int(resultado))
