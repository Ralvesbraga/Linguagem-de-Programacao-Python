x = int(input())
y = int(input())
soma = 0
if x > y:
    while x > (y + 1):
        x = x - 1
        if x % 2 != 0:
            soma = soma + x
elif x < y:
    while x <= y:
        x = x + 1
        if x % 2 != 0:
            soma = soma + x
print(soma)
