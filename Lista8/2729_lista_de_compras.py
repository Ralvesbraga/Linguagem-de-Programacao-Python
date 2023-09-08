n = int(input())
for i in range(n):
    itens = set()
    itens.update(input().split())
    itens = list(itens)
    itens.sort()
    print(*itens)
