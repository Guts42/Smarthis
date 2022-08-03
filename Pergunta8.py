#Importei a biblioteca para gerar números aleatórios
from random import randint

#Inicialização do contador e das listas
count = 0
lista1 = []
lista2 = []

#Laço que se repete 1000x
while count < 1000:

#Guardando o valor aleatório em uma váriavel
    n = randint(1, 10)

#Verificando se o número gerado é maior que 5
    if n > 5:

#Adicionando o numero a lista1
#O erro de Daniel estava nessa parte.
#Em seu código ele gerava um novo número toda vez que tentava adicionar
#o número gerado anteriormente, com a condição de ser maior que 5
        lista1.append(n)

#Caso o número seja menor que 5 ele é adicionado na lista2
    else:
        lista2.append(n)
    
#Incrementando o contador
    count += 1