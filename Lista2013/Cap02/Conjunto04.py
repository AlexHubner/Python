#31. Faça um programa para calcular a área de um triângulo retângulo. O tamanho da base e altura
# do triângulo devem ser informados pelo usuário.

def areaTrianguloRetangulo(b,h):
    b = int(input("Digite o tamanho da base: "))
    h = int(input("Digite o tamanho da altura: "))
    area = (b * h) / 2
    print("A área do triângulo é: ", format(area, '.2f'))
    return area

#32. Faça um programa para calcular a área de um triângulo qualquer. O tamanho dos lados devem ser 
# informados pelo usuário.

def areaTriangulo(b,h):
    b = int(input("Digite o tamanho da base: "))
    h = int(input("Digite o tamanho da altura: "))
    area = (b * h) / 2
    print("A área do triângulo é: ", format(area, '.2f'))
    return area 

#33. Faça um program que leia três valores e apresente, como resultado final, a soma dos quadrados 
# dos três valores lidos.

def somaDosQuadrados(x,y,z):
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    z = int(input("Digite mais um número: "))
    sq = (x**2) + (y**2) + (z**2)
    print("A soma dos quadrados é: ", sq)
    return sq

#34. Faça um programa que leia quatro notas de um aluno e calcule a sua média obtida.

def calculaMedia(x,y,z,w):
    x = int(input("Digite a primeira nota: "))
    y = int(input("Digite a segunda nota: "))
    z = int(input("Digite a terceira nota: "))
    w = int(input("Digite a quarta nota: "))
    media = (x + y + z + w) / 4
    print("A média do aluno é: ", format(media, '.2f'))
    return media

#35. Faça um programa que leia o valor do salário de um funcionário, calcule e mostre seu novo salário, 
# sabendo que o mesmo recebeu um aumento de 21,3%.

def calculaSalario(sal):
    sal = float(input("Digite o salário: "))
    sal = sal + (sal * 0.213)
    print("O salário com aumento é: ", format(sal, '.2f'))
    return sal

#36. Faça um programa que receba a altura do degrau de uma escada e a altura que #o usuário deseja alcançar 
# subindo a escada. Calcular e mostrar quantos degraus o usuário deverá subir para atingir seu objetivo, sem
# se preocupar com a altura do usuário.

def calculaDegraus(ad,af):
    ad = int(input("Digite a altura do degrau: "))
    af = int(input("Digite a altura que deseja alcançar: "))
    degraus = af / ad
    print("Você deverá subir ", format(degraus, '.0f'), "degraus")
    return degraus

#37. Leia o valor do raio de um círculo e calcule a área deste círculo.

def areaCirculo(r):
    r = float(input("Digite o raio: "))
    area = 3.1416 * (r**2)
    print("A área do círculo é: ", format(area, '.2f'))
    return area

#38. Leia o valor do raio de um círculo e calcule a sua circunferência.

def calcCircunferencia(r):
    r = float(input("Digite o raio: "))
    circunferencia = (2 * 3.1416) * (r**2)
    print("A circunferência do círculo é: ", format(circunferencia, '.2f'))
    return circunferencia

#39. Leia o valor do raio de uma esfera e calcule a área de sua superfície e o volume da esfera.

def esfera(r):
    r = float(input("Digite o raio: "))
    area = 4 * 3.1416 * (r**2)
    volume = (4/3) * 3.1416 * (r**3)
    print("A área da esfera é: ", format(area, '.2f'))
    print("O volume da esfera é: ", format(volume, '.2f'))
    return area, volume

#40.  A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que
# da quantia total:
# >> O primeiro ganhador receberá 46%;
# >> O segundo receberá 32%;
# >> O terceiro receberá o restante.
# Calcule e imprima a quantia ganha por cada um dos ganhadores.

def premio(p):
    p = float(input("Digite o valor do premio: "))
    p1 = (p * 0.46)
    p2 = (p * 0.32)
    p3 = (p * 0.046)
    print("O primeiro ganhador receberá: ", format(p1, '.2f'))
    print("O segundo ganhador receberá: ", format(p2, '.2f'))
    print("O terceiro ganhador receberá: ", format(p3, '.2f'))
    return p1, p2, p3