n = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

while True:
    try:
        entrada = input()
        if len(entrada) == 1:
            print(n[int(entrada)])
        else:
            print(n.index(entrada))
    except EOFError:
        break
