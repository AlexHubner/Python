#01. Faça um programa que exiba a mensagem "Olá Mundo!" para o usuário.

def olaMundo():
    print("Olá Mundo!")

#02. Faça um programa que declare uma variável inteira e mostre seu conteúdo para o usuário. 
# Execute o programa algumas vezes. Qual o significado do valor que está # sendo impresso pelo 
# programa?

def numero(x):
    x = 10
    print(x)

#03.  Faça um programa que declare uma variável real com precisão simples, atribua a essa variável 
# o valor do número Pi (3.1415) e mostre, para o usuário, o conteúdo dessa variável.

def pi():
    pi = 3.1415
    print(pi)

#04. Faça um programa que declare uma variável capaz de armazenar um caractere, # atribua a letra "a" 
# a essa variável e mostre na tela o conteúdo da variável.

def caractere():
    caractere = "a"
    print(caractere)

#05. Faça um programa que declare uma variável inteira, atribua a essa variável # o valor 2.97 e mostre
# na tela o conteúdo da variável. Que valor é mostrado # na tela? Por que isso acontece? Como pode ser 
# evitado esse tipo de problema?

def varInteira(x):
    x = int(2.97)
    print(x)

#06. Faça um programa que declare uma variável real com precisão dupla, atribua # a essa variável a expressão
# 123/456 e mostre o resultado que está armazenado na variável? Que valor é mostrado na tela? Por que isso 
# acontece? Como pode ser evitado esse tipo de problema?

def varReal(x):
    x = 0.00
    x = 123/456
    print(x)

# O valor mostrado é 0.26973684210526316. # Isso acontece porque não foi colocada o formato para a resposta.
# Uma das formas de evitar esse problema é colocando sinais de formatação, #por exemplo: print("%,2f" % x)

#07. Faça um programa capaz de ler um carectere, informado pelo usuário, e mostrar o caractere escolhido
# pelo usuário.

def lerCaractere(x):
    x = input("Digite um caractere: ")
    print("O caractere digitado foi: ", x)

#08. Faça um programa que leia um número inteiro e um número real de precisão simples. Mostre na tela ambos 
# os valores.

def intEreal(x,y):
    x = int(input("Digite um número inteiro: "))
    y = float(input("Digite um número real: "))
    print("O número inteiro digitado foi: ", x)
    print("O número real digitado foi: ", y)

#09. Faça um program que leia um valor inteiro e mostre este mesmo valor nas # bases hexadecimal e octal.

def hexaEocta(x):
    x = int(input("Digite um número inteiro: "))
    print("O número inteiro digitado em hexadecimal é: ", hex(x))
    print("O número inteiro digitado em octal é: ", oct(x))

#10. Ler um valor real e exibir este valor com a precisão de duas cadas decimais (nem mais nem menos).

def realDois(x):
    x = float(input("Digite um número real: "))
    print("O número real digitado com duas casas decimais é: ", format(x, '.2f'))