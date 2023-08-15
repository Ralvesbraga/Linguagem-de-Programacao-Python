resto = int(input())
v1 = [100, 50, 20, 10, 5, 2, 1]
print(resto)
for i in v1:
    notas = resto//i
    resto = resto % i
    print('{} nota(s) de R$ {},00'.format(notas, i))
