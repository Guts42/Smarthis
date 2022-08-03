#Importei a função de gerar numeros inteiros aleatórios
from random import randint

#Criei um array para guardar os valores gerados
numeros = []

#Criei um contador para controlar o loop while
cont = 0

#Loop infinito para gerar numeros até que as condições sejam atendidas
while True:

#Usei a função randint para gerar um numero entre 1 e 60
    n = randint(1,60)

#Verificação para saber se o numero gerado não está na lista
    if n not in numeros:

#Caso o numero não esteja na lista o programa adiciona ele e soma um valor no contador
        numeros.append(n)
        cont += 1

#O loop é interrompido quando o contador chega/ultrapassa 6
    if cont >= 6:
        break

#Usei a função sort para organizar em ordem crescente os numeros
numeros.sort()

#Exibindo o resultado
print('Os numeros sorteados são', numeros)