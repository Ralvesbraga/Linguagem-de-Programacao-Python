x = int(input())
maior = x
pos = 1
posmaior = 1
for i in range(2, 101):
    x = int(input())
    if x > maior:
        maior = x
        posmaior = i
print(maior)
print(posmaior)
