n = int(input())
for i in range(n):
    pav = input()  ## armazena a palavra em pav
    num1 = pav[2:4]  ## como os numeros são alocados no mesmo indice sempre, então é so usar a repartição de string nas devidas posicoes da palavra, a primeira ocorre no indice: 2,3
    num2 = pav[5:8]  ## ja o segundo numero, ocorre no indice: 5 a 7, lembrando que o ultimo sempre tem que adicionar +1 da posição desejada.
    num3 = pav[11:13]  ## ja o terceiro e ultimo numero ocorre no indice: 11 e 12
    num1 = int(num1)  ## depois que armazena os numeros, basta tranformar cada um pra inteiro e printar no final
    num2 = int(num2)
    num3 = int(num3)
    print(num1 + num2 + num3)
