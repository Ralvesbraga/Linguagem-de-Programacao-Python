vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
frase = input()
for i in frase:
    if i in vogais:
        vogais.update({i: +1})
print(vogais)
