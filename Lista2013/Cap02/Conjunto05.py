from datetime import datetime, timedelta
import math

#41. Uma empresa contrata um encanador a R$ 30,00 por dia. Crie um programa que solicite o 
# número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, 
# sabendo-se que são descontados 8% para pagamento # de impostos e taxas devidas.

def pagamento(dt):
    dt = int(input("Digite o número de dias trabalhados: "))
    pagamento = dt * 30
    desconto = pagamento * 0.08
    liquido = pagamento - desconto
    print("O pagamento é: ", liquido)
    return liquido

#42. Leia os valores de dois catetos de um triângulo e calcule e mostre o valor # da hipotenusa.

def calcHipotenusa(c1,c2):
    c1 = int(input("Digite o valor do primeiro cateto: "))
    c2 = int(input("Digite o valor do segundo cateto: "))
    x = (c1**2) + (c2**2)
    hipotenusa = math.sqrt(x)
    print("A hipotenusa é: ", hipotenusa)
    return hipotenusa

#43. Faça um programa que leia um caractere e imprima esse caractere como se fosse um número inteiro. 
# Que número é esse que foi exibido pelo programa?

def letra(x):
    x = input("Digite um caractere: ")
    print(ord(x))
# O número exibido pelo programa é o valor do caractere digitado de acordo # com a tabela ASCII.

#44. Faça um programa que converta uma letra maiúscula em letra minúscula.

def maiusculaParaMinusculas(x):
    x = input("Digite uma letra maiúscula: ")
    print(x.lower())

#45. Faça um programa que leia um número inteiro, positivo e de três dígitos, calcule o número formado
# pelos dígitos invertidos do número lido.
# Exemplo:
# Número lido: 123
# Número Obtido: 321

def inverter(x):
    x = int(input("Digite um número inteiro positivo de três dígitos: "))
    x = str(x)
    x = x[::-1]
    print(x)
    return x

#46. Faça um programa para ler um horário (hora:minuto:segundo) de início e a # duração de uma experiência 
# biológica. O programa deve informar o horário (hora:minuto:segundo) de término da mesma.

def horario(inicio, duracao):
    inicio = input("Digite o horário de início: ")
    duracao = input("Digite a duração da experiência: ")
    h_inicio = datetime.strptime(inicio, '%H:%M:%S')
    horas, minutos, segundos = map(int, duracao.split(':'))
    duracao = timedelta(hours=horas, minutes=minutos, seconds=segundos)
    fim = h_inicio + duracao
    print("O horário de término é: ", fim)
    return fim

#47. Faça um programa que calcule a média ponderada das notas de três provas. A primeira e a segunda prova 
# têm peso 1 e a terceira prova tem peso 2. O programa deve mostrar a média obtida pelo aluno.

def calcPonderada(n1, n2, n3):
    n1 = float(input("Digite a nota da primeira prova: "))
    n2 = float(input("Digite a nota da segunda prova: "))
    n3 = float(input("Digite a nota da terceira prova: "))
    media = (n1/1) + (n2/1) + (n3/2)
    print("A média é: ", media)
    return media

#48. Faça um programa que leia o valor da hora de trabalho (em reais), o número de dias trabalhados no mês
# de janeiro deste ano, e mostre na tela o valor a ser pago ao funcionário, adicionando 10% sobre o valor 
# calculado. Considere que a carga de trabalho é de segunda a sexta-feira, das 08:00 às 12:00 e as 14:00 
# às 18:00; aos sábados, das 08:00 às 12:00. Considere que o funcionário teve folga em dias de feriados.

def calcPagamento(valHora,diaSeman, sab):
    pg = valHora * ((diaSeman * 10) + (sab * 4))
    pgf = pg * 1.1
    return pgf

def pagamento2(vh,ds,s):
    vh = float(input("Digite o valor da hora de trabalho: "))
    ds = int(input("Digite o número de dias trabalhados no mês: "))
    s = int(input("Digite o número de sábados trabalhados: "))
    final = calcPagamento(vh,ds,s)
    print("O pagamento é: ", final)
    return final

#49. Escreva um programa que leia as coordenadas x e y de um ponto no plano cartesiano e calcule a sua 
# distância ao ponto de origem.

def cartesiano(x,y):
    x = int(input("Digite a coordenada x: "))
    y = int(input("Digite a coordenada y: "))
    distancia = math.sqrt(x**2 + y**2)
    print("A distância é: ", distancia)
    return distancia

#50. Escreva um programa que leia as coordenadas x e y de dois pontos no plano e calcule a distância entre eles.

def pontoCartesiano(xa,ya,xb,yb):
    xa = int(input("Digite a coordenada x do primeiro ponto: "))
    ya = int(input("Digite a coordenada y do primeiro ponto: "))
    xb = int(input("Digite a coordenada x do segundo ponto: "))
    yb = int(input("Digite a coordenada y do segundo ponto: "))
    distancia = math.sqrt((xb-xa)**2 + (yb-ya)**2)
    print("A distância é: ", distancia)
    return distancia