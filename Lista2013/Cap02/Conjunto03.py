#21. Faça um programa que ler uma temperatura em graus Celsius e convertê-la para Kelvin.

def celsiusParakelvin(x):
    x = int(input("Digite uma temperatura em Celsius: "))
    kelvin = x + 273.15
    print("A temperatura digitada em Kelvin é: ", kelvin)
    return kelvin

#22. Faça um programa que converta uma temperatura em Kelvin para Celsius.

def kelvinParacelsius(x):
    x = int(input("Digite uma temperatura em Kelvin: "))
    celsius = x - 273.15
    print("A temperatura digitada em Celsius é: ", celsius)
    return celsius

#23. Faça um programa para converter de graus Fahrenheit para Kelvin.

def fahrParakelvin(x):
    x = int(input("Digite uma temperatura em Fahrenheit: "))
    kelvin = ((x-32)/1.8) + 273.15
    print("A temperatura digitada em Kelvin é: ", kelvin)
    return kelvin

#24. Faça um programa para converter de Kelvin para graus Fahrenheit.

def kelvinParafarhenheit(x):
    x = int(input("Digite uma temperatura em Kelvin: "))
    farhenheit = ((x - 273.15) * 1.8) + 32
    print("A temperatura digitada em Fahrenheit é: ", farhenheit)
    return farhenheit

#25. Faça um programa que leia uma temperatura em graus Celsius e mostre seu valor em graus 
# Fahrenheit e Kelvin.

def celsiusParafahrEkelvin(x):
    x = int(input("Digite uma temperatura em Celsius: "))
    fahrenheit = (x * 1.8) + 32
    kelvin = x + 273.15
    print("A temperatura digitada em Fahrenheit é: ", fahrenheit)
    print("A temperatura digitada em Kelvin é: ", kelvin)
    return fahrenheit, kelvin

#26. Faça um programa para ler um ângulo em graus e convertê-lo em radianos.

def grausParaRadianos(g):
    rad = 3.14159265359 * (g / 180)
    print("O ângulo digitado em radianos é: ", format(rad, '.2f'))
    return rad

#27. Faça um programa para ler um ângulo em radianos e convertê-lo em graus.

def radianosParaGraus(r):
    graus = (r * 180) / 3.14159265359
    print("O ângulo digitado em graus é: ", format (graus, '.2f'))
    return graus

#28. Faça um programa que leia um número e exiba o seu antecessor e sucessor.

def antecessorESucessor(x):
    x = int(input("Digite um número: "))
    antecessor = x - 1
    sucessor = x + 1
    print("O antecessor do número digitado é: ", antecessor)
    print("O sucessor do número digitado é: ", sucessor)
    return antecessor, sucessor

#29. Faça um programa para calcular a área de um quadrado. O tamanho do lado  # deve ser informado
# pelo usuário.

def areaQuadrado(x):
    x = int(input("Digite o tamanho do lado do quadrado: "))
    area = x * x
    print("A área do quadrado é: ", area)
    return area

#30. Faça um programa para calcular a área de um retângulo. O tamanho dos lados devem ser informados 
# pelo usuário.

def areaTriangulo(b,h):
    b = int(input("Digite o tamanho da base do triângulo: "))
    h = int(input("Digite o tamanho da altura do triângulo: "))
    area = b * h
    print("A área do triângulo é: ", area)
    return area