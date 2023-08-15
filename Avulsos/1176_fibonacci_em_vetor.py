n = int(input())
fib = [0, 1, 1]
for i in range(3, 61):
    atual = fib[i - 2] + fib[i - 1]
    fib.append(atual)
for i in range(n):
    x = int(input())
    print(f'Fib({x}) = {fib[x]}')
