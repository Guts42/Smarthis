#Código em python
#Link para o repositório https://github.com/Guts42/Smarthis
#Array com exemplos de valores para as notas
notas = [0, 8560, 210, 0, 23368, 14560, 4000]

#Contador de notas com valor 0
zeros = 0

#Array para guardar os valores que vão ser inseridos no banco de dados
auto = []

#Percorrendo os elementos da lista
for i in notas:

#Testando se os elementos são iguais a 0. Se sim o contador é incrementado
    if i == 0:
        zeros += 1

#Testando se os elementos são maiores ou iguais a 5000. Se sim uma mensagem é exibida para representar um e-mail
    elif i >= 5000:
        print('Nota enviada para o centro de custo.\nValor R$ {},00'.format(i))
    
#Adicionando os elementos menores que 5000 na lista auto
    else:
        auto.append(i)

#E-mail com quantidade total de notas processadas
print('A lista de notas possui:', len(notas), 'notas.')

#E-mail com quantidade de notas com valor zerado
print('A quantidade de notas com valor zerado é {}.'.format(zeros))

#post para o banco de dados com as notas de valor inferior a R$ 5.000
print('Notas com valor inferiro a R$ 5.000 inseridas no banco com sucesso.\nValores', auto)