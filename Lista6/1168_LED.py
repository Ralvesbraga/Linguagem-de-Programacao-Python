valores = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  ## crio um vetor que armazena a quantidade de leds que tem em cada número (usando os indices de cada um)
n = int(input())
for i in range(n):
    led = 0  ## conta os leds
    nums_digitados = [0] * 10  ## crio um vetor que vai armazenar a quantidade de vezes que o numero aparedeu quando foi digitado em nums
    nums = list(input()) ## uso o list para separar cada numero em um vertozao
    for j in nums: ## faço um for para rodar o vetor nums e usar eles para adicionar no vetor quantidade de vezes  que o numero apareceu
        nums_digitados[int(j)] += 1 ## o indice é led e o que ele armazena é a quantidade de vezes que o num apareceu. ex1: [1,2,0,1,0,1,0,0,1,0]
    for j in range(10):
        led += nums_digitados[j] * valores[j]  ## multiplico pela quantidade de numeros que tem em cada indice pela quantidade de leds cada numero necessita e armazeno em led
    print(f'{led} leds')
