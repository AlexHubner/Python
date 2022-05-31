#11. Ler um valor inteiro e exibir este valor com pelo menos três dígitos.
# Exemplo:
# * valor lido:7 -> valor exibido:007 
# * valor lido:17 -> valor exibido: 017
# * valor lido:1024 -> valor exibido: 1024

def inteiroDigitos(x):
    x = int(input("Digite um número inteiro: "))
    print("O número inteiro digitado com pelo menos três dígitos é: ", format(x, '03d'))

#12. Faça um programa que leia uma data no formato (dd/mm/aaaa) e mostre a data fornecida no 
# formato (aaaa/mm/dd).

def formataData(x):
    x = input("Digite uma data no formato (dd/mm/aaaa): ")
    print("A data digitada no formato (aaaa/mm/dd) é: ", x[6:] + "/" + x[3:5] + "/" + x[0:2])

#13. Faça um programa que leia um número inteiro, calcule o seu quadrado e exiba o resultado.

def quadrado(x):
    x = int(input("Digite um número inteiro: "))
    quad = x**2
    print("O quadrado do número digitado é: ", quad)
    return quad

#14. Faça um programa que leia um número inteiro, calcule a décima parte deste # número e exiba 
# o resultado.

def decimaParte(x):
    x = int(input("Digite um número inteiro: "))
    dec = x/10
    print("A décima parte do número digitado é: ", dec)
    return dec

#15. Faça um programa que leia dois números, some estes números e exiba o resultado.

def somaDois(x,y):
    x = int(input("Digite um número inteiro: "))
    y = int(input("Digite outro número inteiro: "))
    soma = x + y
    print("A soma dos números digitados é: ", soma)
    return soma

#16. Faça um programa capaz de multiplicar dois números fornecidos pelo usuário.

def multDois(x,y):
    x = int(input("Digite um número inteiro: "))
    y = int(input("Digite outro número inteiro: "))
    mult = x * y
    print("O produto dos números digitados é: ", mult)
    return mult

#17. Faça um programa que leia dois números inteiros e calcule sua soma, subtração, multiplicação
# e divisão.

def todasOperacoes(x,y):
    x = int(input("Digite um número inteiro: "))
    y = int(input("Digite outro número inteiro: "))
    soma = x + y
    sub = x - y
    mult = x * y
    div = x / y
    print("A soma dos números digitados é: ", soma)
    print("A subtração dos números digitados é: ", sub)
    print("O produto dos números digitados é: ", mult)
    print("A divisão dos números digitados é: ", div)
    return soma, sub, mult, div

#18. Faça um programa para calcular a soma de três valores informados pelo usuário.

def somaTres(x,y,z):
    x = int(input("Digite um número inteiro: "))
    y = int(input("Digite outro número inteiro: "))
    z = int(input("Digite mais um número inteiro: "))
    soma = x + y + z
    print("A soma dos números digitados é: ", soma)
    return soma

#19. Faça um programa para ler uma temperatura em graus Celsius e mostrar seu valor convertido para
# graus Fahrenheit.

def celsiusParaFahrenheit(x):
    x = float(input("Digite uma temperatura em graus Celsius: "))
    fahrenheit = (x * 1.8) + 32
    print("A temperatura digitada em Fahrenheit é: ", fahrenheit)
    return fahrenheit

#20. Faça um programa para ler uma temperatura em graus Fahrenheit e apresentar seu valor convertido para
# graus Celsius.

def fahrenheitParaCelsius(x):
    x = float(input("Digite uma temperatura em graus Fahrenheit: "))
    celsius = (x - 32) / 1.8
    print("A temperatura digitada em Celsius é: ", celsius)
    return celsius