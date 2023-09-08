n = int(input())
for i in range(n):
    qnt = int(input())
    feira = {}
    total = 0
    for j in range(qnt):
        fruta, valor = input().split()
        feira.update({fruta: float(valor)})
    qnt = int(input())
    for j in range(qnt):
        fruta, valor = input().split()
        total += feira[fruta] * int(valor)
    print(f'R$ {total:.2f}')
