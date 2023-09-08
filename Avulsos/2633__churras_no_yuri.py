while True:
    try:
        n = int(input())
        carnes = {}
        for i in range(n):
            cr, vl = input().split()
            carnes.update({int(vl): cr})
        carnes = dict(sorted(carnes.items()))
        print(*carnes.values(), sep=' ')
    except EOFError:
        break
