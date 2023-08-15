while True:
    try:
        n = int(input())
        x = [0] * 2001
        for i in range(n):
            y = int(input())
            x[y] += 1
        for i in range(1, 2001):
            if x[i] > 0:
                print(f'{i} aparece {x[i]} vez(es)')
    except EOFError:
        break
