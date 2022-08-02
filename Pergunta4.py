#Lendo a entrada do problema

saque = int(input('Qual o valor do seu saque? '))

#O programa será executado até que o usuário consiga relaizar seu saque

while(saque>=5):

#Verificando se a entrada é válida

    if(saque%5 != 0):
        print('Só é possivel sacar notas de 5, 20 e 50 reais.')
        saque = int(input('Qual o valor do seu saque? '))

#Executando a exibição de quantas notas serão sacadas

    else:
        print('Notas de R$ 50,00:', int(saque/50))
        saque -= 50 * int(saque/50)
        print('Notas de R$ 20,00:', int(saque/20))
        saque -= 20 * int(saque/20)
        print('Notas de R$ 5,00:', int(saque/5))
        saque -= 5 * int(saque/5)