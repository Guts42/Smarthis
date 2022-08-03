#Importei a biblioteca para poder usar comandos do sistema
import os

#Importei a função de gerar numeros inteiros aleatórios
from random import randint

#Função para limpar a tela (funciona no windows)
def clear():
    os.system('cls')

#Função para ler os limiter informados pelo jogador
def readLimit(word):
    while True:
        i = input('\nDigite o limite {} do intervalo --> '.format(word))

#Caso o jogador digite algum caractere que não seja um número o programa pede que ele entre com o valor novamente
        if not i.isdigit():
            print('Limite inválido. Tente novamente.')
        else:
            return int(i)

#Função para ler o palpite do jogador
def readUser():
    while True:
        i = input('Qual é o número? ')

#Caso o jogador digite algum caractere que não seja um número o programa pede que ele entre com o valor novamente
        if not i.isdigit():
            clear()
            print('Entrada inválida. Tente novamente.')
        else:
            return int(i)

#Função para verificar se o limite inferior é maior que o superior
#Caso seja ela inverte os limites
def checkLimit(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
    return a, b

#op é a váriavel de controle para iniciar/continuar/parar o jogo
op = ''
while op != 'S' or op != 'N':
    clear()

#Caso o jogador digite n/N o jogo exibe a mensagem e para de rodar
    if op == 'N':
        print('~'*40)
        print(':(\nAté a próxima...')
        print('~'*40)
        break

#Caso o jogador digite s/S o jogo começa e exibe as regras
    elif op == 'S':
        print('O jogo funciona assim:\n--> Você deve escolher dois números para que eu pense em um número entre eles.')
        print('--> Você ganha se adivinhas o número em que pensei.\n\nPode tentar quantas vezes quiser. ^^')
        a = readLimit('inferiror')
        b = readLimit('superior')
        clear()
        a, b = checkLimit(a, b)

#Gerando um número aleátorio entre os limites fornecidos
        n_rand = randint(a,b)
        
#cont é um contador para as tentativas do jogador
        cont = 0

#Enquanto o jogador não acertar o número o jogo continua e incrementa o contador de tentativas
        while True:
            cont += 1
            n = readUser()
            clear()

#Verificando se o palpite do jogador é menor/maior/igaul ao número gerado
            if n < n_rand:
                print('O número em que pensei é maior que esse...')
            elif n > n_rand:
                print('O número em que pensei é menor que esse...')
            elif n == n_rand:
                clear()
                print('~'*40)
                print('Você acertou!!!\nO número era', n, '\nTentativas: ', cont)
                print('~'*40)
                break

#Opção para continuar jogando
        print('~'*40)
        print('Vamos jogar de novo?')
        print('~'*40)
        op = input('[S/N] --> ').upper()

#Caso o jogador digite um valor diferente de S/N o jogo continua perguntando    
    else:
        clear()
        print('~'*40)
        print('Vamos jogar um jogo?')
        print('~'*40)
        op = input('[S/N] --> ').upper()
