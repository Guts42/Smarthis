#Lendo a entrada do problema
adesivos = int(input('Digite o numero de adesivos: '))

#j representa o número máximo de algarismos presentes nas caixas
j = 0

#max é o número máximo de adesivos para j número(s) de algarismo(s) na(s) caixa(s)
max = 0

while(max < adesivos):
    max += (j+1) * 9 * 10**j
    j += 1

#Calculando a quantidade de caixas com j-1 algarismos
quantidade = sum((9*10**i for i in range(j)))

#Calculando a quantidade restante de adesivos para colar nas caixas
adesivos -= sum(((i+1)*9*10**i for i in range(j)))

#Somando a quantidade de caixas com j-1 algarismos + a quantidade de caixas
#que foi possivel completar com o restante dos adesivos
quantidade += adesivos//j

#Exibindo o resultado
print('A quantidade de caixas é', quantidade)