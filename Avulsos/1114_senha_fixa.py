senha = '2002'
while True:
    senha_digitada = input()
    if senha_digitada == senha:
        break
    else:
        print('Senha Invalida')
print('Acesso Permitido')
